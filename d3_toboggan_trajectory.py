'''
Day 3 - Puzzle 1

My idea for the solution is to treat the right/down directives as an increment in the index of the each char that
composes the map. This way I do not have to worry about the width of the map.
Since the map may have a different width each time, i first find the idx_interval (so what increment does 3 right/ 1 down mean in relation to the map width)
I then split the map into a list of chars.
Now i simply count which chars appear at the relevant index, moving my cursor by a to_next_idx value.
I save them to a result list and remove the first item manually because i have not figured out yet a better way.

Issue: my solution is wrong and i think the issue resides in the way i am dealing with the IndexError. I feel
like I am missing a few trees that would appear right before that error occurs.
'''

from utils import input_reader

toboggan_map = input_reader('d3_data.txt')

def find_idx_interval(l):
    return len(l[0])

def lines_to_chars(l):
    return list(''.join(l))

def remove_first_value_from_result(l):
    l.pop(0)
    return l

def count_trees(l, item):
    return l.count(item)

def find_trajectory(input_map):
    result = []
    idx = 3
    char_map = lines_to_chars(input_map)
    to_next_idx = find_idx_interval(input_map)

    for char in char_map:
        try:
            result.append(char_map[idx])
            idx += to_next_idx
        except IndexError:
            break
        
    result = remove_first_value_from_result(result)
    number_of_trees = count_trees(result, '#')
    print(number_of_trees)
    return number_of_trees

find_trajectory(toboggan_map)

