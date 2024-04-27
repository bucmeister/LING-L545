import re
import sys

line = sys.stdin.readlines()
option_arr = []

for lines in line:
    try:
        option_arr.append(lines.strip('\n').split()[1])
    except:
        continue

# print(option_arr)

if option_arr[-1][-1] == '?':
    print('\nThis string cannot be processed:')
    print(option_arr[-1])
    exit()

chuv_str = '.' + option_arr[-1]

full_vowels = 'ɐeiouyɯa'
reduced_vowels = 'əɘ'

result = [chars in chuv_str for chars in full_vowels]
if True not in result:
    chuv_str = chuv_str[1:]
    chuv_str = 'ˈ'+ chuv_str
    print(chuv_str)
else:
    dot_arr = [m.start() for m in re.finditer(r'\.', chuv_str)]
    dot_arr.insert(0,0)
    fullv_arr = [m.start() for m in re.finditer(r'[ɐeiouyɯa]', chuv_str)]
    cut_list = [x for x in dot_arr if x < fullv_arr[-1]]
    chuv_str = chuv_str[:cut_list[-1]+1] + 'ˈ' + chuv_str[cut_list[-1]+1:]
    chuv_str = chuv_str[1:]
    print(chuv_str)