# LING-L545

http://cl.indiana.edu/~ftyers/courses/2020/Autumn/L-545/

Programmed by: Anthony Bucco

The program for this module inputs a Chuvash corpus and outputs a cleaner version without lines containing invalid characters. 

## Usage

Schema:

```bash
# inputs wiki.txt, outputs encoded_text.txt
cat wiki.txt | python3 encoding.py
```

Output:

```bash
# split words in line
['Шыв', 'ресурсĕсен', 'федераци', 'агентстви', 'хатĕрленĕ', 'РФ', 'территорин', 'шыв', 'хуçалăх', 'районĕсен', 'геоинформаци', 'системин', 'хыпарĕпе', ':']

# validity of words (Valid/Invalid); lines with Invalids are excluded from encoded_text.txt
Valid:Шыв
Valid:ресурсĕсен
Valid:федераци
Valid:агентстви
Valid:хатĕрленĕ
Valid:РФ
Valid:территорин
Valid:шыв
Valid:хуçалăх
Valid:районĕсен
Valid:геоинформаци
Valid:системин
Valid:хыпарĕпе
Valid::

...

Original line count:  135012
Cleaned line count:  125585

# histogram of permitted characters
Matching characters: {'Ч': 16663, 'ă': 354472, 'в': 219254, ... }

# histogram of nonpermitted characters
Eliminated characters: {'L': 648, 't': 3565, 'i': 4803, 'n': 4189, ... }

# Characters both permitted and nonpermitted (should be empty)
Common characters []

# Unicode Character Properties for permitted characters
Unicode categories:
Ч :  Lu
ă :  Ll
в :  Ll
а :  Ll
...

```

## License

[MIT](https://choosealicense.com/licenses/mit/)