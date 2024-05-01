import re
import unicodedata
import sys

line = sys.stdin.readlines()
pattern = r'^[0-9\u0400-\u04FF\u2000-\u206FAaBEeËëKMHOoPpCcTXxАаӐӑБбВвГгДдЕеЁёӖӗЖжЗзИиЙйКкЛлМмНнОоПпРрСсҪҫТтУуӲӳФфХхЦцЧчШшЩщЪъЫыЬьЭэЮюЯяAaBEeËëKMHOoPpCcTXxĂăĔĕÇçŸÿ!%"()\[\].?:,-;«»-]+$'

newline = []
matching_chars = {}
bad_chars = {}

for lines in line:
   words = lines.split()
   print(words)
   do_append = True
   for thing in words:
      if re.match(pattern, thing):
         print ('Valid:' + thing)
      else:
         print ('Invalid:' + thing)
         do_append = False
      for letter in thing:
            if re.match(pattern, letter):
               if letter not in matching_chars.keys():
                  matching_chars[letter] = 1
               else:
                  matching_chars[letter] += 1
            else:
               if letter not in bad_chars.keys():
                  bad_chars[letter] = 1
               else:
                  bad_chars[letter] += 1
   if do_append is True:
      newline.append(lines)
   else:
      print('Invalid line: ', lines)
      
print('Original line count: ', len(line))
print('Cleaned line count: ', len(newline))
with open('encoded_text.txt', 'w') as f:
   for line in newline:
      f.write(line)
   f.close()

commonchars = list(set(matching_chars).intersection(bad_chars))

print('Matching characters: ', matching_chars)
print('Eliminated characters:', bad_chars)
print('Common characters', commonchars)

print('Unicode categories:')
for char in matching_chars.keys():
   print(char,": ", unicodedata.category(char))
   