import re
import unicodedata
import sys

lines = sys.stdin.readlines()

with open('segd_wiki.txt', 'w') as f:
    for line in lines:
        print('new line')
        matcharr = []
        exception_indices = []

        for c in '!?':
            line = line.replace(c, c + '\n')
        for letts in re.findall(r"(\.[^\s\.]+\.|\s[^\s\.]\.|\.\.\. [aeëopcxаӑбвгдеёӗжзийклмнопрсҫтуӳфхцчшщъыьэюяaeëopcxăĕçÿ])", line):
            matcharr.append(letts)
        # print(matcharr)
        if matcharr != []:
            for entry in matcharr:
                res = [i for i in range(len(line)) if line.startswith(entry, i)]
                print(res)
                if res != []:
                    for match in res:
                        for x in range(match, match + len(entry) + 1):
                            # print(x)
                            exception_indices.append(x)
            
        print(set(exception_indices))
        for count, value in enumerate(line):
            if value == '.' and count not in set(exception_indices):
                print(exception_indices)
                print('found period that does not exist in exception')
                print(line)
                line = line[:count + 1] + '\n' + line[count + 1:]

        f.write(line)
f.close()