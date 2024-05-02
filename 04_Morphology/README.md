# LING-L545

http://cl.indiana.edu/~ftyers/courses/2020/Autumn/L-545/

Programmed by: Anthony Bucco

This project implements basic morphotactics for 20 Uzbek nouns and outputs all possible combinations into a text file. It includes the seven case suffixes, plural suffixes, possessive suffixes, and diminutive and profession noun-to-noun derivational suffixes. 

## Setup

This software uses the Helsinki Finite-State Transducer (HFST) toolkit, which you can download using this tutorial:
https://cl.indiana.edu/~ftyers/courses/2024/Spring/L-545/practicals/morphology/

## Usage

Input:

```bash
# outputs to uzbek_noun_morpho.txt
hfst-fst2strings uzb.lexc.hfst > uzbek_noun_morpho.txt
```

## License

[MIT](https://choosealicense.com/licenses/mit/)