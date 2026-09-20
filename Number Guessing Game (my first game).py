import random

high_score = None

play_again = "Y"

while play_again.upper() == "Y":
    num_of_tries = 0

    secret_number = random.randint(1, 10000)

    print("hello, please guess a number between 1 and 100")
    guess = int(input("type your guess here: "))

    while guess != secret_number:
        num_of_tries = num_of_tries + 1
        if guess < secret_number:
            print("guess higher")
        elif guess > secret_number:
            print("guess lower")
        guess = int(input("type your guess here: "))

    if guess == secret_number:
        num_of_tries = num_of_tries + 1
        print("good job, you guessed the number in " + str(num_of_tries) + " tries.")
        if high_score is None or num_of_tries < high_score:
            high_score = num_of_tries
            print("your new high score is: " + str(high_score))
        else:
            print("your current high score is: " + str(high_score))    
        play_again = input("would you like to play again? Y/N: ")