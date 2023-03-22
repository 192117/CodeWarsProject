# def get_middle(s):
#     length = len(s)
#     if length % 2 == 0:
#         return s[length//2-1:length//2+1]
#     else:
#         return s[length//2]
#     return s


def get_middle(s):
    index, odd = divmod(len(s), 2)
    return s[index] if odd else s[index - 1:index + 1]


print(get_middle("test"))
print(get_middle("testing"))
print(get_middle("middle"))
print(get_middle("A"))