import random

def random_walk(n):
    x = 0
    y = 0
    for i in range(n):
        step = random.choice(['N','S','W','E'])
        if step == 'N':
            y = y + 1
        elif step == 'S':
            y = y - 1
        elif step == 'W':
            x = x - 1
        else:
            x = x + 1
    return (x, y)


for i in range(50):
    one_walk = random_walk(100)
    how_far = int(one_walk[0]) ** 2 + int(one_walk[1]) ** 2
    if how_far >= 50:
        print(one_walk, 'It is too far away from home~ Taxi~~~')
    else:
        print(one_walk, "emmmmm, I haven't drunk, give me more drink!")
