import re

filename = r"D:\Projects\advent_of_code_2022\Day 5\day_5_test.txt"
num_stacks = 3

with open(filename,'r') as file:
    raw_stacks = [i.rsplit(',') for i in file.read().split('\n')]

moves = [idx for idx in raw_stacks if 'move' in idx[0]]
raw_stacks = [idx[0].split("[") for idx in raw_stacks if 'move' not in idx[0]][:-2]
raw_stacks = [[chr.strip("] ") for chr in stack] for stack in raw_stacks]
# fill stacks
raw_stacks.reverse()
# cut off blank first stacks
raw_stacks = [[stack[item_idx] for item_idx in range(len(stack)) if item_idx > 0 ] for stack in raw_stacks]

stacks = [[]]*num_stacks
for level in raw_stacks:
    print(level)
    for stack_idx in range(len(level)):
        print(level[stack_idx])
        stacks[stack_idx].append(level[stack_idx])
    print(stacks)

working_stacks = stacks.copy()
# Perform moves
for move in moves:
    # Extract move
    item_move_values = re.findall(r'\d+', move[0])
    item_move_values = list(map(int, item_move_values))

    # Extract values
    qty_moved = item_move_values[0]
    from_stack = item_move_values[1] - 1 #-1 to convert to index
    to_stack = item_move_values[2] -1 #-1 to convert to index
    print(move)
    print(working_stacks)

    items_being_shifted = [working_stacks[from_stack].pop() for num_items in range(qty_moved)] 
    working_stacks[to_stack] += items_being_shifted

    print(working_stacks)
    print()

print()


    