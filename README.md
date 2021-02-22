# morse-works
Utilities for manipulating Morse Code (CW) data streams

## morsewords.py
A commandline script for converting a file of words (one per line) to a form which [ebook2cw](https://fkurz.net/ham/ebook2cw.html) can take as input to generate MP3 files for ICR (instant character recognition) practice.

```code
usage: morsewords.py [-h] [-u] [-i INFILE] [-o OUTFILE]
                     [-fw {1,2,3,4,5,6,7,8,9,10}] [-s SPEED] [-ss SSTEP]
                     [-f FREQUENCY] [-fs FSTEP]

Convert a list of words into Ebooks to CW format

optional arguments:
  -h, --help            show this help message and exit
  -u, --unique          Remove duplicate words (default: false)
  -i INFILE, --infile INFILE
                        input file (defaults to 'in.txt')
  -o OUTFILE, --outfile OUTFILE
                        input file (defaults to 'in.txt')
  -fw {1,2,3,4,5,6,7,8,9,10}, --farnsworth {1,2,3,4,5,6,7,8,9,10}
                        WPM to reduce nominal rate
  -s SPEED, --speed SPEED
                        starting speed (defaults to 15)
  -ss SSTEP, --sstep SSTEP
                        speed increase step size (defaults to 5)
  -f FREQUENCY, --frequency FREQUENCY
                        starting audio frequency in Hz (defaults to 600)
  -fs FSTEP, --fstep FSTEP
                        audio frequency reduction step size in Hz (defaults to 25)
```
Sample output:

```code
|w15 |f600 |e15 relationship  
|w20 |f600 |e20 relationship  
|w25 |f600 |e25 relationship  
|w30 |f600 |e30 relationship  
|w35 |f600 |e35 relationship  
|w40 |f600 |e40 relationship   
 
|w15 |f575 |e15 organization  
|w20 |f575 |e20 organization  
|w25 |f575 |e25 organization  
|w30 |f575 |e30 organization  
|w35 |f575 |e35 organization  
|w40 |f575 |e40 organization   
 
|w15 |f550 |e15 particularly  
|w20 |f550 |e20 particularly  
|w25 |f550 |e25 particularly  
|w30 |f550 |e30 particularly  
|w35 |f550 |e35 particularly  
|w40 |f550 |e40 particularly   
 
|w15 |f525 |e15 international  
|w20 |f525 |e20 international  
|w25 |f525 |e25 international  
|w30 |f525 |e30 international  
|w35 |f525 |e35 international  
|w40 |f525 |e40 international   
 
|w15 |f500 |e15 environmental  
|w20 |f500 |e20 environmental  
|w25 |f500 |e25 environmental  
|w30 |f500 |e30 environmental  
|w35 |f500 |e35 environmental  
|w40 |f500 |e40 environmental 
```
__Written and maintained by Russell Whitaker__
