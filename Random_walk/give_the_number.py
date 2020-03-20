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


def a_smart_fool(funds, initial_wager, game_count):
    wager = initial_wager
    x = []
    y = []
    current_game_count = 1
    previous_game = "win"
    previous_game_wager = initial_wager

    while current_game_count <= game_count:
        if previous_game == "win":
            print("The samrt fool win the last game~ Play more~")
            if give_the_number():
                funds += wager
                print(funds)
                x.append(current_game_count)
                y.append(funds)
            else:
                funds -= wager
                previous_game = "loss"
                print(funds)
                previous_game_wager = wager
                x.append(current_game_count)
                y.append(funds)

                if funds < 0:
                    print("The samrt fool went broke in {} games.".format(current_game_count))
                    break

        elif previous_game == "loss":
            print("The smart fool lost the last one, but he is smart, and he will double up!")
            if give_the_number():
                wager = previous_game_wager * 2
                print("The fool won", wager)
                funds += wager
                previous_game = "win"
                wager = initial_wager
                x.append(current_game_count)
                y.append(funds)
            else:
                wager = previous_game_wager * 2
                print("The fool lost", wager)
                funds -= wager
                print(funds)
                previous_game = "loss"
                previous_game_wager = wager
                x.append(current_game_count)
                y.append(funds)
                if funds < 0:
                    print("The smart fool went broke in", current_game_count, "games")
                    break
        current_game_count += 1
    print(funds)
    plt.plot(x, y)


n = 0
while n < 100:
    a_smart_fool(10000, 1000, 1000)
    n += 1

plt.xlabel("How many games the fool played")
plt.ylabel("Funds")
plt.show()