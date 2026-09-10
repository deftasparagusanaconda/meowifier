chars = ' etaoinshrdlcumwfgypbvkjxqzETAOINSHRDLCUMWFGYPBVKJXQZ0123456789.,()!?\'":;#$%&+-*/<=>@[\\]^_`{|}~'

meows = [
'meow',
'*cuddles*',
'*tail wiggles*',
'bonk',
'-w-',
'silly willy',
'omg!!',
'eepy~',
'*smoochies*',
'*zoomies*',
'wuvwy',
':}',
'*head pats*',
'>.<',
'*zzz*',
'nyaa~',
';D',
'awooo',
'^o^',
'*poke*',
'weee!!',
':P',
'RAWRRR',
'^.^',
'*pets*',
'mroww',
':)',
'*hug*',
'^v^',
'luvly',
'smol.',
'fren.',
'bean.',
':3',
'pookie',
'owo',
'eepy weepy',
'uwu',
'^w^',
'*head rubs*',
'>w<',
'squee',
'hehe',
'UwU',
'>//<',
'=w=',
'floof',
'=u=',
':>',
'>v<',
';3',
'*ear scritchies*',
'^~^',
'ily <3',
'*chin rubs*',
'cutie',
'wooo!!',
'OwO',
'eep!!',
'yayy!!',
';)',
'blep',
'XD',
'*mwah*',
'mrrp',
'heart <3',
'nomnom',
'-u-',
'*scritchies*',
'*nuzzles*',
'*kissies*',
'^-^',
'yippee!!',
'mlem',
'>o<',
'-v-',
'^u^',
'*hisss*',
'*snuggles*',
'mew',
'=v=',
'*belly rubs*',
'*wiggles*',
'*boop*',
'honeybun',
'teehee',
':D',
'>\\\\<',
'>u<',
'*purr*',
'*pat*',
'good kitty',
'qt3.14',
'wawa',
'wiwi']

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
