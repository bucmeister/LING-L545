# LING-L545

http://cl.indiana.edu/~ftyers/courses/2020/Autumn/L-545/

Programmed by: Anthony Bucco

This project is a grapheme-to-phoneme transliterator for the Chuvash language, which processes a Cyrillic Chuvash string into the International Phonetic Alphabet (IPA).

## Setup

This software uses the Helsinki Finite-State Transducer (HFST) toolkit, which you can download using this tutorial:

## Usage

```bash
python3 l545_final.py {Cyrillic Chuvash string}
```

Example:

```bash
python3 l545_final.py эрешле

# returns the IPA transliteration of the string with syllable boundaries and primary stress
ɯ.ɾeʃ.ˈle
```

## Disclaimer

A proper encoder for the text is still under development. If the Chuvash string returns an error, try to replace the characters in the string with those in the following list:

