'''
PUZZLE 1
For this Puzzle I turned the input into a list of dictionaries and then checked for the presence of the necessary keys.
I probably overthought the whole conversion process from puzzle input to list of dicts, but it works and I am happy with that.
'''

from utils import input_reader

raw_data = input_reader('d4_data.txt')

def split(sequence, sep):
    chunk = []
    for val in sequence:
        if val == sep:
            yield chunk
            chunk = []
        else:
            chunk.append(val)
    yield chunk

raw_passports = list(split(raw_data, ''))
passports_sublists = [' '.join(passport).split() for passport in raw_passports]
passports_items = [[item.split(':') for item in passport] for passport in passports_sublists]

def from_nested_to_dict(lst_of_lists_of_lsts):
    passports = []

    for item in passports_items:
        d = dict()
        for field in item:
            d[field[0]] = field[1]
        passports.append(d)
    return passports

passports = from_nested_to_dict(passports_items)

necessary_keys = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']

valid_passports = 0
for passport in passports:
    if all(necessary_key in passport for necessary_key in necessary_keys):
        valid_passports += 1
    else:
        False

print(valid_passports)