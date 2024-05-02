# LING-L545

http://cl.indiana.edu/~ftyers/courses/2020/Autumn/L-545/

Programmed by: Anthony Bucco

This module writes a constraint grammar that disambiguates sentences.

## Usage

Input:

```bash
# outputs results of the grammar made in eng.cg3 into test.txt, as the rules apply to train.txt 
cat train.txt | vislcg3 --trace --grammar eng.cg3 > test.txt
```

## License

[MIT](https://choosealicense.com/licenses/mit/)