from math import log, ceil

latin = {char: index for index, char in enumerate('abcdefghijklmnopqrstuvwxyz', start=1)}

meows = [
# you got heart, kid
'mew', 'meww',
'mrew', 'mreww', 'mmrew',

# :3
'meow', 'mmeow', 'meoww', 
'mreow', 'mreoww', 'mmreow',

# hewwpp :(
'meu', 'meuu', 'mmeu',
'mreu', 'mreuu', 'mmreu',

# how is a nigga gon borrow a fry? nigga is u gon give it back?
'mao', 'maoo', 'mmao',
# eyebrow, drown
'mrow', 'mroww', 'mmrow',

# row row row ur boat
'mow', 'moww', 'mmow', 
]

words = open('words.txt').read().split()

MEOW_COUNT = len(meows)
WORD_COUNT = len(words)
PREFIX_LEN = ceil(log(WORD_COUNT, MEOW_COUNT))

def word_to_meow(word):
    'find in words first. if not available, make from int construction. assumes word is word.lower().strip()'

    # stupid index == 0 edge case
    if word == 'the':
        return meows[0]

    meowdexes = []
    
    index = words.index(word) if word in words else MEOW_COUNT ** PREFIX_LEN + sum(latin[char] * MEOW_COUNT ** e for e, char in enumerate(reversed(word)))
    #index = sum(latin[char] * MEOW_COUNT ** e for e, char in enumerate(reversed(word)))
    
    while index > 0:
        meowdexes.append(index % MEOW_COUNT)
        index //= MEOW_COUNT
    
    return '-'.join(meows[meowdex] for meowdex in meowdexes)

#def meow_to_word(meow):

import re

nfa = re.compile(r'[a-z]+|[^a-z]+')

def words_to_meows(words):
    return ''.join(word_to_meow(token) if token.isalpha() else token for token in nfa.findall(words.lower()))
