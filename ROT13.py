import codecs

def rot13(message):
    return codecs.encode(message, encoding='rot-13')



print(rot13("EBG13 rknzcyr.")) # "ROT13 example."
print(rot13("This is my first ROT13 excercise!")) # "Guvf vf zl svefg EBG13 rkprepvfr!"





# def rot13(message):
#     def decode(char):
#         if 'A' <= char <= 'Z':
#             main = 'A'
#         elif 'a' <= char <= 'z':
#             main = 'a'
#         else:
#             return char
#         return chr((ord(char)-ord(main) + 13) % 26 + ord(main))
#     return ''.join(decode(char) for char in message)