import random

rand_num = random.randint(1, 10)
guessed_nums = []
allowed_guesses = 4

while len(guessed_nums) < allowed_guesses:
    guess = input("Guess a number between 1 and 10: ")
    try:
        player_num = int(guess)
    except:
        print("Thats not a whole number")
        break
    if not player_num > 0 or not player_num <11:
        print("Number is not in allowable range")
        break
    guessed_nums.append(player_num)
    if player_num == rand_num:
        print("Correct! The number was {}.".format(rand_num))
        print("It took you {} tries.".format(len(guessed_nums)))
        break
    else:
        if rand_num > player_num:
            print("Too low, my number is higher than {}. Guess # {}.".format(player_num, len(guessed_nums)))
        else:
            print ("Too high, my number is lower than {}. Guess # {}.".format(player_num, len(guessed_nums)))
            continue
if not rand_num in guessed_nums:
    print("Sorry :(, the number was {}.".format(rand_num))
