def rgb(r, g, b):

    # if r < 0:
    #     r = 0
    # if g < 0:
    #     g = 0
    # if b < 0:
    #     b = 0
    # if r > 255:
    #     r = 255
    # if g > 255:
    #     g = 255
    # if b > 255:
    #     b = 255
    # r, g, b = hex(r)[2:].upper(), hex(g)[2:].upper(), hex(b)[2:].upper()
    # if len(r) < 2:
    #     r = '0'+r
    # if len(g) < 2:
    #     g = '0'+g
    # if len(b) < 2:
    #     b = '0'+b
    # return '{}{}{}'.format(r, g, b)

    func = lambda x: min(255, max(x, 0))
    return '{:02X}{:02X}{:02X}'.format(func(r), func(g), func(b))



dict_values = {
    (0, 0, 0): '000000', # testing zero values
    (1, 2, 3): '010203', # testing near zero values
    (255, 255, 255): 'FFFFFF', # testing max values
    (254, 253, 252): 'FEFDFC', # testing near max values
    (-20, 275, 125): '00FF7D', # testing out of range values
}


for number in dict_values:
    print(f'Для числа {number}: функция вернула {rgb(*number)}, а в словаре {dict_values[number]}')