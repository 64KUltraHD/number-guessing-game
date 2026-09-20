import random

high_scores = {
    "1": None,
    "2": None,
    "3": None,
    "4": None,
    "5": None,
    "6": None,
    "7": None,
    "8": None,
    "9": None
}

difficulty_names = {
    "1": "simple",
    "2": "peaceful",
    "3": "breezy",
    "4": "easy",
    "5": "medium",
    "6": "hard",
    "7": "challenging",
    "8": "difficult",
    "9": "extreme"
}


play_again = "Y"

while play_again.upper() == "Y":
    num_of_tries = 0

    print("choose your game difficulty:")
    print("1. simple (1-5)")
    print("2. peaceful (1-10)")
    print("3. breezy (1-50)")
    print("4. easy (1-100)")
    print("5. medium (1-1000)")
    print("6. hard (1-10000)")
    print("7. challenging (1-100000)")
    print("8. difficult (1-1000000)")
    print("9. extreme (1-10000000)")
    while True:
        difficulty = input("enter your choice (1-9): ")
        if difficulty == "1":
            max_number = 5
            break
        elif difficulty == "2":
            max_number = 10
            break
        elif difficulty == "3":
            max_number = 50
            break
        elif difficulty == "4":
            max_number = 100
            break
        elif difficulty == "5":
            max_number = 1000
            break
        elif difficulty == "6":
            max_number = 10000
            break
        elif difficulty == "7":
            max_number = 100000
            break
        elif difficulty == "8":
            max_number = 1000000
            break
        elif difficulty == "9":
            max_number = 10000000
            break
        else:
            print("choose difficulty level 1-9 to begin")
   
    if high_scores[difficulty] is not None:
        print("your current high score for " + difficulty_names[difficulty] + " is: " + str(high_scores[difficulty]))
    else:
        print("no high score on this difficulty yet")

    secret_number = random.randint(1, max_number)

    print("hello, please guess a number between 1 and " + str(max_number))
    

    while True:
        try:
            guess = int(input("type your guess here: "))

            if guess < 1 or guess > max_number:
                print("the number must be between 1 and " + str(max_number))
                continue
            break
        except ValueError:
            print("only enter a valid number.")

    while guess != secret_number:
        num_of_tries = num_of_tries + 1
        if guess < secret_number:
            print("guess higher")
        elif guess > secret_number:
            print("guess lower")
        while True:
            try:
                guess = int(input("type your guess here: "))

                if guess < 1 or guess > max_number:
                    print("the number must bebetween 1 and " + str(max_number))
                    continue
                break
            except ValueError:
                print("only enter a valid number.")

    if guess == secret_number:
        num_of_tries = num_of_tries + 1
        print("good job, you guessed the number in " + str(num_of_tries) + " tries.")
        if high_scores[difficulty] is None or num_of_tries < high_scores[difficulty]:
            high_scores[difficulty] = num_of_tries
            print("your new high score is: " + str(high_scores[difficulty]))
        else:
            print("your current high score is: " + str(high_scores[difficulty]))
        play_again = input("would you like to play again? Y/N: ")
