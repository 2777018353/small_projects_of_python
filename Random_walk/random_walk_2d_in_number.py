import random

def random_walk_v2(n):
    x, y = (0, 0)
    for i in range(n):
        (dx, dy) = random.choice([(0,1),(0,-1),(-1, 0),(1, 0)])
        x += dx
        y += dy

    return (x, y)

taking_a_taxi_counter = 0
how_many_simulations = 1000
how_many_steps = 500
leg_limit = 1000

for i in range(how_many_simulations):
    one_walk = random_walk_v2(how_many_steps)
    how_far = int(one_walk[0]) ** 2 + int(one_walk[1]) ** 2
    if how_far >= leg_limit:
        taking_a_taxi_counter += 1

print(taking_a_taxi_counter / how_many_simulations * 100, "% of taking a taxi home.")