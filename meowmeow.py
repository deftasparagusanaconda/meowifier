letter_to_meow = dict(zip('etaoinshrdlcumwfgypbvkjxqz', [
    # U
    # :3
    'meow','meoww','mmeow', 
    'mreow','mreoww','mmreow',

    # I
    # you got heart, kid
    'mew','meww',
    'mrew','mreww','mmrew',

    # E
    # hewwpp :(
    'meu','meuu','mmeu',
    'mreu','mreuu','mmreu',

    # A
    # how is a nigga gon borrow a fry? nigga is u gon give it back?
    'mao','maoo','mmao',
    # eyebrow, drown
    'mrow','mroww','mmrow',

    # O
    # row row row ur boat
    'mow','moww','mmow', 
]))

meow_to_letter = {value: key for key, value in letter_to_meow.items()}

import re
'''
word_lexer = re.compile(r'[a-z]+|[^a-z]+')
meow_lexer = re.compile(r'[a-z]+|[^a-z]+')

def words_to_meows(words):
    return ''.join('-'.join(letter_to_meow[letter] for letter in token) if token.isalpha() else token for token in word_lexer.findall(words.lower().replace('-', '--')))

def meows_to_words(meows):
    return ''.join(''.join(meow_to_letter[meow] for meow in token.split('-')) if token.isalpha() else token for token in meow_lexer.findall(meows.lower().replace('--', '-')))
'''
word_lexer = re.compile(r'[a-z]+|[^a-z]+')
meow_lexer = re.compile(r'[a-z]+(?:-[a-z]+)*|--|[^a-z-]+|-')

def words_to_meows(words):
    return ''.join('-'.join(letter_to_meow[letter] for letter in token) if token.isalpha() else token.replace('-', '--') for token in word_lexer.findall(words.lower()))

def meows_to_words(meows):
    return ''.join(''.join(meow_to_letter[meow] for meow in token.split('-')) if token[0].isalpha() else '-' if token == '--' else token for token in meow_lexer.findall(meows.lower()))
