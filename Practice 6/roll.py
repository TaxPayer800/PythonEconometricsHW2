import random

def roll_the_dice(n_rolls,win_num=6):
    score = 0
    for roll in range(n_rolls):
        d1 = random.randint(1,6)
        d2 = random.randint(1,6)
        d3 = random.randint(1,6)
        if d1==d2==d3==win_num:
          score = score + 1
        else:
             continue
             return score
