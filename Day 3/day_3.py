import pandas as pd

# Generate priority values
lowercase_alphabet =  [chr(letter) for letter in range(97,123)]
uppercase_alphabet =  [chr(letter) for letter in range(65, 91)]
item_priorities = pd.DataFrame({'alphabet':lowercase_alphabet, 'priority':range(1,27)}).append(
    pd.DataFrame({'alphabet':uppercase_alphabet, 'priority':range(27,53)}),
    ignore_index=True
)

filename = r"D:\Projects\advent_of_code_2022\Day 3\day_3_puzzle_input.txt"
raw_packing_data = pd.read_csv(filename, sep=" ", names=['rucksacks'])

## PART 1

# Whats common between the two rucksacks
rucksack_data = raw_packing_data.copy()
# Split into compartments 
rucksack_data["total_capacity"] = rucksack_data["rucksacks"].str.len()
rucksack_data["rucksacks"] = rucksack_data["rucksacks"].astype(str)
rucksack_data["comp_1"] = rucksack_data['rucksacks'].apply(lambda x: x[0:len(x)//2])
rucksack_data["comp_2"] = rucksack_data['rucksacks'].apply(lambda x: x[len(x)//2:])

# Whats the same in each compartment 
rucksack_data["common"] = rucksack_data.apply(lambda x: list(set(x["comp_1"]).intersection(set(x["comp_2"])))[0],axis=1)
rucksack_data = pd.merge(
    rucksack_data,
    item_priorities,
    how='left',
    left_on="common",
    right_on="alphabet"
)
print("Total Priority Score ", rucksack_data["priority"].sum())

## PART 2

# Create elf groups
rucksack_data = raw_packing_data.copy()
member_1_idx = pd.RangeIndex(0,rucksack_data["rucksacks"].shape[0], step=3)
member_2_idx = pd.RangeIndex(1,rucksack_data["rucksacks"].shape[0], step=3)
member_3_idx = pd.RangeIndex(2,rucksack_data["rucksacks"].shape[0], step=3)
groups = pd.DataFrame({
    'member_1': list(raw_packing_data.loc[member_1_idx, "rucksacks"]),
    'member_2': list(raw_packing_data.loc[member_2_idx, "rucksacks"]),
    'member_3': list(raw_packing_data.loc[member_3_idx, "rucksacks"])
})

# Get common item badge per group
groups["common"] = groups.apply(
    lambda x: list(
        set(x["member_1"]).intersection(set(x["member_2"])).intersection(set(x["member_3"]))
        )[0]
    ,axis=1)
# Get priority scores
groups = pd.merge(
    groups,
    item_priorities,
    how='left',
    left_on="common",
    right_on="alphabet"
)
print("Total Priority Score ", groups["priority"].sum())

