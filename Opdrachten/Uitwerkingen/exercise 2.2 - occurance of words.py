import string

s = r"""\
Slowly the hippos sank into the river
The water so cold that it gave them a shiver
(Hippos can't swim, like the pelicans think
They also can't float, they could easily sink)"""

# clean up
# s = s.lower().replace('.', '').replace(',', '').replace('(', '').replace(')', '')
# or
s = s.lower().translate(str.maketrans('', '', string.punctuation))
# or
# import re
# s = re.sub(r'[^a-zA-Z0-9 ]', '', s)

words = s.split()

unique_words = set(words)

d = dict()
for word in unique_words:
    n = words.count(word)
    d[word] = n

# or
d = {word: words.count(word) for word in set(words)}

for word, n in sorted(d.items(), key = lambda item: item[1], reverse=True):
    print(f'{word:20}: {n:3} {"*" * n}')

# def get_values(item):
#     return item[1]
#
# for word, n in sorted(d.items(), key=get_values, reverse=True):
#     # print(word, n)
#     # print('%-25s: %3d' % (word, n))
#     print(f'{word:<25}: {n:3}')
#     # or
#     print('%-15s: %3d %s' % (word, n, '*' * n))
