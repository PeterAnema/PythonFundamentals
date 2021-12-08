def f(s):
    return s[::-1]


f = lambda s: s[::-1]


sentence = 'this is a story about a couple of kids walking through the woods'

words = sentence.split()

print( sorted(words, key = lambda s: s[::-1]) )

print( list(filter(lambda word:word.startswith('w'), words)) )

print( list(map(lambda word: word.upper(), words)) )

def how_many_vowels(word):
    return sum([word.count(v) for v in 'aeiou'])

print( sorted(words, key = how_many_vowels) )

print( sorted(words, key = lambda word: sum([word.count(v) for v in 'aeiou'])) )
