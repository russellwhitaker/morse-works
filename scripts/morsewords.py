#!/usr/bin/env python

from argparse import ArgumentParser
from itertools import chain
from random import shuffle
from string import Template

import sys

class MorseWriter():

    def __init__(self, farnsworth_reduction, speed, sstep, frequency, fstep, unique):
        self.speeds = [speed + (sstep*i) for i in range(6)]
        self.farnsworth_reduction = farnsworth_reduction
        self.frequencies = [frequency - (fstep*i) for i in range(5)]
        self.templates = self.gen_templates(self.frequencies)
        self.unique = unique

    def gen_templates(self, frequencies):
        """Generate templates for output lines"""
        return [[Template("|w$s |f" + f + " |e$f $w  \n"),
                 Template("|w$s |f" + f + " |e$f $w  \n"),
                 Template("|w$s |f" + f + " |e$f $w  \n"),
                 Template("|w$s |f" + f + " |e$f $w  \n"),
                 Template("|w$s |f" + f + " |e$f $w  \n"),
                 Template("|w$s |f" + f + " |e$f $w   \n \n")] for f in map(str, frequencies)]

    def read_words(self, f):
        """Read input words file, optionally removing duplicates"""
        fh = open(f, "r")

        if self.unique:
            lines = set(fh.read().splitlines())
        else:
            lines = fh.read().splitlines()

        fh.close()

        return list(filter(None, lines))

    def sort_by_size(self, words):
        """Sort words by ascending size,
           but scrambling lexical (alphabetical) ordering within
           size groups to avoid grouping of similar words in sequence.
        """
        shuffle(words)
        return sorted(words, key=len)

    def partition_words(self, words, n=5):
        """Partition words into frequency cycle size"""
        return [words[i * n:(i + 1) * n] for i in range((len(words) + n - 1) // n )]

    def gen_stanza(self, pattern_group):
        """Generate sequence of increasing WPM speed"""
        return [t.substitute(w = pattern_group[1],
                             s = str(self.speeds[i]),
                             f = str(self.speeds[i] - self.farnsworth_reduction))
                  for i, t in enumerate(pattern_group[0])]

    def process_word_list(self, words):
        """Apply template generator to all words in list"""
        pairs = [list(zip(self.templates, ws)) for ws in words]
        processed = [self.gen_stanza(i) for i in chain(*pairs)]

        return list(chain(*processed))

    def write_morse_file(self, filename, words):
        """Write out processed words to file which
           can be consumed by a sound-generation program
        """
        outfile = open(filename, 'w')
        outfile.writelines(words)
        outfile.close()

def main(argv):
    parser = ArgumentParser(description='Convert a list of words into Ebooks to CW format')

    parser.add_argument('-u', '--unique', action="store_true",
                        default=False,
                        help='Remove duplicate words (default: false)')
    parser.add_argument('-i', '--infile',
                        default='in.txt',
                        help="input file (defaults to 'in.txt')")
    parser.add_argument('-o', '--outfile',
                        default='out.txt',
                        help="output file (defaults to 'out.txt')")
    parser.add_argument('-fw', '--farnsworth', type=int,
                        choices=[1,2,3,4,5,6,7,8,9,10],
                        default=0,
                        help='# of WPM to reduce nominal rate to effective rate')
    parser.add_argument('-s', '--speed', type=int,
                        default=15,
                        help='starting WPM speed (defaults to 15)')
    parser.add_argument('-ss', '--sstep', type=int,
                        default=5,
                        help='WPM speed increase step size (defaults to 5)')
    parser.add_argument('-f', '--frequency', type=int,
                        default=600,
                        help='starting audio frequency in Hz (defaults to 600)')
    parser.add_argument('-fs', '--fstep', type=int,
                        default=25,
                        help='audio frequency reduction step size in Hz (defaults to 25)')
    args = parser.parse_args()

    mw = MorseWriter(args.farnsworth, args.speed, args.sstep, args.frequency, args.fstep, args.unique)

    if args.unique:
        print("Eliminating duplicate words")
    if args.farnsworth:
        print("Reducing effective rate by {} WPM".format(args.farnsworth))

    try:
        words = mw.read_words(args.infile)
    except IOError as ioe:
        print("Error: {}".format(ioe))
        sys.exit(2)

    ordered_words = mw.sort_by_size(words)
    partitioned_words = mw.partition_words(ordered_words)

    mw.write_morse_file(args.outfile, mw.process_word_list(partitioned_words))

    sys.exit("Wrote {} words to {}".format(len(words), args.outfile))

if __name__ == "__main__":
    main(sys.argv[1:])
