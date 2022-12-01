filename = r"D:\Projects\advent_of_code_2022\Day 1\day_1_part_1_puzzle_input.txt"
with open(filename) as file:
    puzzle_input = file.readlines()
    elves_calories = [] #index represent elf number
    calorie_count=0
    for line in puzzle_input:
        line = line.strip("\n")
        if line != "":
            #its a number 
            calorie_count += float(line)
        else:
            # reset calorie count and add calorie_count to list
            elves_calories.append(calorie_count)
            calorie_count = 0

    print("Highest calorie count: ", max(elves_calories))