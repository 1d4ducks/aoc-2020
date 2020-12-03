from utils import input_reader

raw_passwords = input_reader('d2_data.txt')

passwords = [password.replace(':', ' ').replace('-', ' ').split() for password in raw_passwords] 

counter = 0

'''
Puzzle 1
I solved it by splitting the input into its 4 parts then checking whether the target letter
appeared in the password. 
If yes, count how many times it appears and compare check if it follows the constraint.
'''
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

'''
Puzzle 2
I solved it by using the same splitting idea from above and only working on the passwords 
i know contain the target letter
Here i find the index of where that letter appears in the password and then use boolean
logic to apply the puzzle rules
'''
second_counter = 0

for password in passwords:
    low_constraint = password[0]
    high_constraint = password[1]
    target = password[2]
    full_pass = password[3]
    if target in full_pass:
        idxs = [idx for idx, char in enumerate(full_pass) if char == target]
        if int(low_constraint)-1 in idxs and int(high_constraint)-1 in idxs:
            False
        elif int(low_constraint)-1 not in idxs and int(high_constraint)-1 not in idxs:
            False
        else:
            second_counter += 1

