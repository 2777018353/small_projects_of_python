import random


def give_the_number():
    number = random.randint(1, 100)
    if number <= 51:
        print(number, "The number is 1~51. You lose. Play again.")
        return False
    else:
        print(number, "The number is 52~100. You win. Good Luck.")
        return True


def a_fool(funds, wager, game_count):
    current_game_count = 0
    while current_game_count < game_count:
        if give_the_number():
            funds += wager
        else:
            funds -= wager
        current_game_count += 1
    if funds <= 0:
        funds = "Penny less"
    
    print("How rich the fool is:", funds)


a_fool(1000000, 100000, 100)
