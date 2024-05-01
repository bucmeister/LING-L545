import sys

lines = sys.stdin.readlines()
token_dict = open("dictionary.txt", "r")


matcharr = []
finalsentencearr = []

for term in token_dict:
    matcharr.append(term[:-1])


# lines_max = len(lines)
lines_max = len(lines)
for k in range(0, lines_max):
    print('!! line', k)
    
    print('lines[k]', lines[k])
    words = lines[k].split()

    word_count = 0
    sentence_arr = []

    for word in words:
        word_count += 1
        print('word_count', word_count)

        m = 0
        split_indices = []

        while m < len(word):
            # print('word length', len(word))
            # print(m)
            instance_indices = []

            for x in reversed(range(m,len(word))):
                # print('---at index', x)
                if word[m:x] in matcharr:
                    # print(word[m:x], "has a match")
                    instance_indices.append(x)
                # else:
                #     print(word[m:x], "does not have a match")
                #     instance_indices

            if instance_indices != []:
                split_indices.append(instance_indices[0])
                m = split_indices[-1]
            else:
                # print('no indexes found')
                m = m + 1
                split_indices.append(m)

        print(split_indices)
        parts = [word[v1:v2] for v1, v2 in zip([0]+split_indices, split_indices+[None])]
        sentence_arr.append(' '.join(parts))
        print('input:',lines[k])
        print('output:',parts)

    print('final:', ' '.join(sentence_arr))
    finalsentencearr.append(' '.join(sentence_arr))

with open('output.test.txt', 'w') as f:
    for line in finalsentencearr:
        f.write(line+'\n')
f.close()