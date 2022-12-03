import pandas as pd

filename = r"D:\Projects\advent_of_code_2022\Day 2\day_2_puzzle_input.txt"
raw_game_data = pd.read_csv(filename, sep=" ", names=['elf_response',  'my_response'])

## PART 1
shapes = ['A', 'B','C','X','Y','Z']
scores = [1,2,3] * 2
shape_scores = pd.DataFrame({'shape':shapes, 'scores':scores})
game_data = raw_game_data.copy()

# Determine if game was won
# If score is the same then draw 
# If difference between scores is -2 or 1 then win
# Else loss
game_data = game_data.join(shape_scores.set_index("shape"), on="my_response")
game_data = game_data.join(shape_scores.set_index("shape"), on="elf_response", rsuffix="_elf")
game_data["score_diff"] = game_data["scores"] - game_data["scores_elf"]

game_data["outcome_score"] = 0
game_data.loc[game_data["score_diff"] == 0, "outcome_score"] = 3
game_data.loc[(game_data["score_diff"] == 1) | (game_data["score_diff"] == -2), "outcome_score"] = 6

# Determine score per game
game_data["total_score"] = game_data["scores"] + game_data["outcome_score"]
total_score = game_data["total_score"].sum()

print(total_score)

## PART 2
game_data_p2 = raw_game_data.copy()

# Determine outcome score 
game_data_p2.loc[game_data_p2["my_response"] == 'X', "outcome_score"] = 0
game_data_p2.loc[game_data_p2["my_response"] == 'Y', "outcome_score"] = 3
game_data_p2.loc[game_data_p2["my_response"] == 'Z', "outcome_score"] = 6

# Determine shape score 
game_data_p2 = game_data_p2.join(shape_scores.set_index("shape"), on="elf_response", rsuffix="_elf")
possible_score_combinations = game_data[["scores", 'scores_elf',"outcome_score"]].drop_duplicates()
game_data_p2 = game_data_p2.join(possible_score_combinations.set_index(["outcome_score", "scores_elf"]), on=["outcome_score", "scores"], rsuffix="_my")
game_data_p2["total_score"] = game_data_p2["outcome_score"] + game_data_p2["scores_my"]

total_score = game_data_p2["total_score"].sum()
print(total_score)

