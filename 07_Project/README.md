# LING-L545

http://cl.indiana.edu/~ftyers/courses/2020/Autumn/L-545/

Programmed by: Anthony Bucco

This project is a grapheme-to-phoneme transliterator for the Chuvash language, which processes a Cyrillic Chuvash string into the International Phonetic Alphabet (IPA).

## Setup

This software uses the Helsinki Finite-State Transducer (HFST) toolkit, which you can download using this tutorial:
https://cl.indiana.edu/~ftyers/courses/2024/Spring/L-545/practicals/morphology/

## Usage

```bash
python3 l545_final.py {Cyrillic Chuvash string}
```

Example:

```bash
python3 l545_final.py ӗҫлет

# returns the IPA transliteration of the string with syllable boundaries and primary stress
ɘɕ.ˈletʲ
```

## Troubleshooting

A proper encoder for the input text is still under development. If the Chuvash string returns an error, try to replace the characters in the string with their equivalents in the following list:

Аа Ӑӑ Ее Ёё Ӗӗ Ии Оо Уу Ӳӳ Ыы Ээ Юю Яя
Бб Вв Гг Дд Жж Зз Йй Кк Лл Мм Нн Пп Рр
Сс Ҫҫ Тт Фф Хх Цц Чч Шш Щщ Ьь
