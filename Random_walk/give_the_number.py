import random

def give_the_number():
    number = random.randint(1, 100)
    if number <= 50:
        print(number, "The number is 1~50. You lose. Play again.")
        return False
    else:
        print(number, "The number is 51~100. You win. Good Luck.")
        return True

x = 0
while x < 100:
    result = give_the_number()
    print(result)
    x += 1
