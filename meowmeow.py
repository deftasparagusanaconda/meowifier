chars = ' etaoinshrdlcumwfgypbvkjxqz0123456789ETAOINSHRDLCUMWFGYPBVKJXQZ.,()!?\'":;#$%&+-*/<=>@[\\]^_`{|}~'

meows = [
# S tier
'meow',
'*purr*',
'nyaa~',

':3',
':D',
'^w^',

'mroww',
'*nuzzles*',
'>w<',

'RAWRRR',
'*zoomies*',
'mrrp',
'>//<',

'*hug*',
'UwU',
'mew',

'ily <3',
'pookie',
'*pets*',

'*pat*',
'*snuggles*',
'XD',

# A tier
'*cuddles*',
'*tail wiggles*',
'eepy~',
'*boop*',
'*head pats*',
'*poke*',
'weee!!',
':)',
'owo',
'uwu',
'hehe',
'>\\\\<',
'blep',
'yippee!!',

# B tier
'*smoochies*',
':P',
'^.^',
'squee',
'*head rubs*',
':>',
'^~^',
'*chin rubs*',
'cutie',
'OwO',
'*belly rubs*',
'yayy!!',
'heart <3',
'>u<',

# C tier
'omg!!',
'>.<',
'*zzz*',
'^o^',
'*hisss*',
'=w=',
'>v<',
'*ear scritchies*',
'*mwah*',
'*kissies*',
'mlem',
'*wiggles*',
'nomnom',

# D tier
'-w-',
'wuvwy',
'>o<',
';D',
'awooo',
'^v^',
'eepy weepy',
'eep!!',
'*scritchies*',
';)',
'=v=',
'^-^',
'^u^',

# E tier
'silly willy',
'-u-',
':}',
'luvly',
'floof',
'=u=',
';3',
'wooo!!',
'-v-',

# F tier
'bonk',
'smol.',
'qt3.14',
'bean.',
'good kitty',
'fren.',
'honeybun',
'teehee',
'wiwi',
'wawa']

char_to_meow = dict(zip(chars, meows, strict=True))
meow_to_char = dict(zip([meow.replace('*', '') for meow in meows], chars, strict=True))

def chars_to_meows(chars: str) -> str:
    return ' '.join(char_to_meow.get(char, char) for char in chars)

def meows_to_chars(meows: str) -> str:
    meows = meows.replace('*', '')
    meows += ' ' # so the last next(it) wont trigger a StopIteration
    output = ''
    buffer = ''

    it = iter(meows)  
    for char in it:
        buffer += char

        # deliberately hard-coded space special case
        if buffer == ' ':
            output += ' '
            buffer = ''
            next(it)    # skip next char since every meow (except the last) is followed by a space

        elif buffer in meow_to_char:
            output += meow_to_char[buffer]
            buffer = ''
            next(it)    # skip next char since every meow (except the last) is followed by a space
    
    if buffer != '':
        raise Exception('could not decode', buffer)
    
    return output
