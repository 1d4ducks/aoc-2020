from utils import input_reader

raw_passwords = input_reader('d2_data.txt')

passwords = [password.replace(':', ' ').replace('-', ' ').split() for password in raw_passwords] 

counter = 0

for password in passwords:
    low_constraint = password[0]
    high_constraint = password[1]
    target = password[2]
    full_pass = password[3]
    if target in full_pass:
        char_count = full_pass.count(target)
        if char_count in range(int(low_constraint), int(high_constraint)+1):
            counter += 1
        False
    False


