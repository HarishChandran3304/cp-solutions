with open("input.txt", "r") as f:
    rounds = f.read().split("\n")

plays = ("Rock", "Paper", "Scissors")
wins = dict(zip(plays, plays[1:]+plays[0:1])) # Val beats key
losses = dict(zip(plays[1:]+plays[0:1], plays)) # Val loses to key
opp_plays = dict(zip(("A", "B", "C"), plays))
my_plays = dict(zip(("X", "Y", "Z"), plays))
play_scores = {v: k for k, v in enumerate(plays, start=1)}


def play_score(my_play):
    return play_scores[my_play]

def to_play(opp_play, result):
    if result == "Z": # Win
        return wins[opp_play]
    
    elif result == "X": # Loss
        return losses[opp_play]
    
    else: # Draw
        return opp_play


def result_score(opp_play, my_play):
    if opp_play == my_play: # Draw
        return 3
    
    elif my_play == wins[opp_play]: # Win
        return 6
    
    else: # Loss
        return 0
    
def round_score(opp_play, my_play):
    return play_score(my_play) + result_score(opp_play, my_play)

total_score = 0
for round in rounds:
    opp_play, result = round.split()
    opp_play = opp_plays[opp_play]
    my_play = to_play(opp_play, result)
    total_score += round_score(opp_play, my_play)

print(total_score)