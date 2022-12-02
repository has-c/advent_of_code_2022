import pandas as pd

filename = r"D:\Projects\advent_of_code_2022\Day 2\day_2_puzzle_input.txt"
shapes = ['A', 'B','C','X','Y','Z']
scores = [1,2,3] * 2
shape_scores = pd.DataFrame({'shape':shapes, 'scores':scores})

## PART 1
game_data = pd.read_csv(filename, sep=" ", names=['elf_response',  'my_response'])

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