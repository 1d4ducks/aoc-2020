'''
PUZZLE 1
For this Puzzle I turned the input into a list of dictionaries and then checked for the presence of the necessary keys.
I probably overthought the whole conversion process from puzzle input to list of dicts, but it works and I am happy with that.
'''

from utils import input_reader
import re

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

def from_nested_to_dict(lst_of_lsts_of_lsts):
    result = []

    for item in lst_of_lsts_of_lsts:
        d = dict()
        for field in item:
            d[field[0]] = field[1]
        result.append(d)
    return result

def validate_passports_keys(lst):
    necessary_keys = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    valid_passports = []
    for passport in passports:
        if all(necessary_key in passport for necessary_key in necessary_keys):
            valid_passports.append(passport)
        else:
            False
    return valid_passports

passports = from_nested_to_dict(passports_items)
valid_passports = validate_passports_keys(passports)
d4_p1_solution = len(valid_passports)

def validate_passport_values(lst):
    def validate_byr():
        passed_byr_validation = []
        for item in lst:
            if int(item['byr']) in range(1920, 2003):
                passed_byr_validation.append(item)
        print('NUMBER OF PASSPORTS WITH VALID BYR: ', len(passed_byr_validation))
        return passed_byr_validation
    
    def validate_iyr():
        passed_iyr_validation = []
        passed_byr = validate_byr()
        for item in passed_byr:
            if int(item['iyr']) in range(2010, 2021):
                passed_iyr_validation.append(item)
        print('NUMBER OF PASSPORTS WITH VALID BYR AND EYR: ', len(passed_iyr_validation))
        return passed_iyr_validation

    def validate_eyr():
        passed_eyr_validation = []
        passed_iyr = validate_iyr()
        for item in passed_iyr:
            if int(item['eyr']) in range(2020, 2031):
                passed_eyr_validation.append(item)
        print('NUMBER OF PASSPORTS WITH VALID BYR, IYR AND EYR: ', len(passed_eyr_validation))
        return passed_eyr_validation

    def validate_hgt():
        passed_hgt_validation = []
        passed_eyr = validate_eyr()
        for item in passed_eyr:
            if item['hgt'].endswith('cm'):
                if int(item['hgt'][:-2]) in range(150, 194):
                    passed_hgt_validation.append(item)
            elif item['hgt'].endswith('in'):
                if int(item['hgt'][:-2]) in range(59, 77):
                    passed_hgt_validation.append(item)
        print('NUMBER OF PASSPORTS WITH VALID BYR, IYR, EYR AND HGT: ', len(passed_hgt_validation))
        return passed_hgt_validation
    
    def validate_hcl():
        passed_hcl_validation = []
        passed_hgt = validate_hgt()
        regex = "^#([a-f0-9]{6})$"
        p = re.compile(regex)
        for item in passed_hgt:
            if re.search(p, item['hcl']):
                passed_hcl_validation.append(item)
        print('NUMBER OF PASSPORTS WITH VALID BYR, IYR, EYR, HGT AND HCL: ', len(passed_hcl_validation))
        return passed_hcl_validation

    def validate_ecl():
        passed_ecl_validation = []
        passed_hcl = validate_hcl()
        accepted_ecl = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
        for item in passed_hcl:
            if item['ecl'] in accepted_ecl:
                passed_ecl_validation.append(item)
        print('NUMBER OF PASSPORTS WITH VALID BYR, IYR, EYR, HGT, HCL AND ECL: ', len(passed_ecl_validation))
        return passed_ecl_validation

    def validate_pid():
        passed_pid_validation = []
        passed_ecl = validate_ecl()
        regex = "^(0\d{8}|\d{9})$"  
        p = re.compile(regex)    
        for item in passed_ecl:
            if re.search(p, item['pid']):
                passed_pid_validation.append(item)
        print('NUMBER OF PASSPORTS WITH VALID BYR, IYR, EYR, HGT, HCL, ECL AND PID: ', len(passed_pid_validation))
        return passed_pid_validation


    passed_pid_validation = validate_pid()
    print('Total number of fully valid passports: ', len(passed_pid_validation))
    return passed_pid_validation

validation = validate_passport_values(valid_passports)
# print(valid_byr_iyr_eyr)