def abbrev_name(name):
    return '.'.join([letter[0].capitalize() for letter in name.split(' ')])


print(abbrev_name("Sam Harris"))