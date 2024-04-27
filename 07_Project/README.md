# LING-L545

http://cl.indiana.edu/~ftyers/courses/2020/Autumn/L-545/

Programmed by: Anthony Bucco

This project is a grapheme-to-phoneme transliterator for the Chuvash language, which processes a Cyrillic Chuvash string into the International Phonetic Alphabet (IPA). It has support for segmental phonological rules, standard stress assignment, and palatalization of the final [t] for a selection of front-vowel harmony verbs when inflected into their third-person singular present forms (which is not reflected in the orthography as with back-vowel harmony verbs).

## Setup

This software uses the Helsinki Finite-State Transducer (HFST) toolkit, which you can download using this tutorial:
https://cl.indiana.edu/~ftyers/courses/2024/Spring/L-545/practicals/morphology/

## Usage

Schema:

```bash
python3 l545_final.py [Cyrillic Chuvash string]
```

Example:

```bash
python3 l545_final.py ӗҫлет

# returns the IPA transliteration of the string with syllable boundaries, primary stress, and palatalization of the final [t] as the third-person singular present form of a front-vowel harmony verb
ɘɕ.ˈletʲ
```

If an infelicitous string is inputted, an error will show:

```bash
python3 l545_final.py ттӗҫлет

This string cannot be processed:
ттӗҫлет+?
```

## Troubleshooting

A proper encoder for the input text is still under development. If the Chuvash string returns an error, try to replace the characters in the string with their equivalents in the following list:

Аа Ӑӑ Ее Ёё Ӗӗ Ии Оо Уу Ӳӳ Ыы Ээ Юю Яя
Бб Вв Гг Дд Жж Зз Йй Кк Лл Мм Нн Пп Рр
Сс Ҫҫ Тт Фф Хх Цц Чч Шш Щщ Ьь

## License

[MIT](https://choosealicense.com/licenses/mit/)