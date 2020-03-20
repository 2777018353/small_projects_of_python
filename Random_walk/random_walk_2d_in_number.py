import random

def random_walk_v2(n):
    x, y = (0, 0)
    for i in range(n):
        (dx, dy) = random.choice([(0,1),(0,-1),(-1, 0),(1, 0)])
        x += dx
        y += dy

    return (x, y)

for i in range(100):
    one_walk = random_walk_v2(20)
    print(one_walk, 'How far away from (0, 0): ', abs(one_walk[0]) + abs(one_walk[1]))