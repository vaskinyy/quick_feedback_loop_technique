# https://stackoverflow.com/questions/63993139/how-to-split-a-list-into-two-random-parts


import random

all_players = set(range(12))

team1 = set(random.sample(all_players, 6))
team2 = all_players - team1

print(team1)
print(team2)
