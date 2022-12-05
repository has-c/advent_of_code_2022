import pandas as pd

def check_overlapping(
    assignment_1_min,
    assignment_1_max,
    assignment_2_min,
    assignment_2_max):

    if (assignment_1_min <= assignment_2_min) and (assignment_1_max >= assignment_2_max):
        # overlapping 
        return "Assignment 1 overlapping"
    elif (assignment_2_min <= assignment_1_min) and (assignment_2_max >= assignment_1_max):
        # overlapping
        return "Assignment 2 overlapping"   
    else:
        return "Not Overlapping"

def check_no_overlap(
    assignment_1_min,
    assignment_1_max,
    assignment_2_min,
    assignment_2_max
):

    if assignment_1_max < assignment_2_min or assignment_2_max < assignment_1_min:
        return "No overlap"
    else:
        return "Any overlap"

filename = r"D:\Projects\advent_of_code_2022\Day 4\day_4_puzzle.txt"
raw_assignment_data = pd.read_csv(filename, sep=",", names=['assignment_1', 'assignment_2'])
assignment_1_min_max_values = raw_assignment_data["assignment_1"].str.split("-", expand=True).copy().astype(int)
assignment_2_min_max_values = raw_assignment_data["assignment_2"].str.split("-", expand=True).copy().astype(int)
assignment_1_min_max_values.columns = ["min_value_1", "max_value_1"]
assignment_2_min_max_values.columns = ["min_value_2", "max_value_2"]
assignment_values = pd.concat([raw_assignment_data,
                                assignment_1_min_max_values, 
                                assignment_2_min_max_values],
                                axis=1
                            )

## PART 1
# Check assignment pairs are contained
assignment_values["overlapping"] = assignment_values.apply(lambda x: check_overlapping(
    x["min_value_1"],
    x["max_value_1"],
    x["min_value_2"],
    x["max_value_2"]),axis=1)

num_pairs_overlapping = assignment_values[assignment_values["overlapping"] != "Not Overlapping"].shape[0]
print("Pairs overlapping ", num_pairs_overlapping)

## PART 2
# Find all pairs that are overlapping
assignment_values["any_overlap"] = assignment_values.apply(lambda x: check_no_overlap(
    x["min_value_1"],
    x["max_value_1"],
    x["min_value_2"],
    x["max_value_2"]),axis=1)

num_overlap_pairs = assignment_values[assignment_values["any_overlap"] != "No overlap"].shape[0]
print("Pairs overlapping ", num_pairs_overlapping)