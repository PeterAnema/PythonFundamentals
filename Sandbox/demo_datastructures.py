
# s = input('Geef tekst: ')

text = "Welcome! Are you completely new to programming? If not then we presume you will be looking for information about why and how to get started with Python. Fortunately an experienced programmer in any programming language (whatever it may be) can pick up Python very quickly. It's also easy for beginners to use and learn, so jump in!"

text = text.lower().translate(str.maketrans('', '', '.,!?()[]'))

words = text.split()

unique_words = set(words)

d = dict()
for word in sorted(unique_words):
    n = words.count(word)
    d[word] = n

for item in d.items():
    print('%-15s : %3d' % item)

