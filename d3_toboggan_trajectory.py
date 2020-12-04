'''
Day 3 - Puzzle 1

'''

from utils import input_reader

toboggan_map = input_reader('d3_data.txt')

print(toboggan_map)

x_coord = 0
y_coord = 0

starting_point = toboggan_map[x_coord][y_coord]
result = []

right = x_coord + 3
down = y_coord + 1


