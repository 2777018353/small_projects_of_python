import random
import matplotlib
import matplotlib.pyplot as plt 


def give_the_number():
    number = random.randint(1, 100)
    if number <= 51:
#        print(number, "The number is 1~51. You lose. Play again.")
        return False
    else:
#        print(number, "The number is 52~100. You win. Good Luck.")
        return True


def a_fool(funds, wager, game_count):
    current_game_count = 0
    x = []
    y = []
    while current_game_count < game_count:
        if give_the_number():
            funds += wager
            x.append(current_game_count)
            y.append(funds)
        else:
            funds -= wager
            x.append(current_game_count)
            y.append(funds)
        current_game_count += 1
    if funds <= 0:
        funds = "Penny less"
    plt.plot(x, y)

n = 0
while n < 100:
    a_fool(1000000, 100000, 10000)
    n += 1
plt.xlabel("How many games does the fool played")
plt.ylabel("Funds")
plt.show()
