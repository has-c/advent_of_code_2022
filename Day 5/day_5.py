filename = r"D:\Projects\advent_of_code_2022\Day 5\day_5_test.txt"
# Create list of lists to hold the stacking data
num_stacks = 3
stacks = [[]]*num_stacks
# Create list to hold instructions
instructions = []

with open(filename,'r') as file:
    raw_stacks = [i.rsplit(',') for i in file.read().split('\n')]

moves = [idx for idx in raw_stacks if 'move' in idx[0]]
raw_stacks = [idx[0].split("[") for idx in raw_stacks if 'move' not in idx[0]][:-2]
raw_stacks = [stack for stack in raw_stacks if stack() != ""]
# fill stacks


print()