import re

# def pig_it(text):
#     return ' '.join(['{}{}ay'.format(word[1:], word[0]) if word.isalpha() else word for word in text.split()])


def pig_it(text):
    pattern = r'(\b\w)(\w*)'
    return re.sub(pattern, r'\2\1ay', text)


pig_it('Pig latin is cool') # igPay atinlay siay oolcay
pig_it('Hello world !')     # elloHay orldway !