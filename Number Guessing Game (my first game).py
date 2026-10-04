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
    "9": None,
    "10": None,
    "11": None,
    "12": None,
    "13": None
}

difficulty_names = {
    "1": "simple",
    "2": "peaceful",
    "3": "breezy",
    "4": "easy",
    "5": "mild",
    "6": "medium",
    "7": "tough",
    "8": "hard",
    "9": "challenging",
    "10": "difficult",
    "11": "harsh",
    "12": "extreme",
    "13": "grueling",
    "14": "surprise"
}


difficulty_ranges = {
    "1": 5,
    "2": 10,
    "3": 50,
    "4": 100,
    "5": 500,
    "6": 1000,
    "7": 5000,
    "8": 10000,
    "9": 100000,
    "10": 1000000,
    "11": 10000000,
    "12": 100000000,
    "13": 1000000000
}

play_again = "Y"

while play_again.upper() == "Y":
    num_of_tries = 0

    print("choose your game difficulty:")
    print("1. simple (1-5) (one to five)")
    print("2. peaceful (1-10) (one to ten)")
    print("3. breezy (1-50) (one to fifty)")
    print("4. easy (1-100) (one to one hundred)")
    print("5. mild (1-500) (one to five hundred)")
    print("6. medium (1-1000) (one to one thousand)")
    print("7. tough (1-5000) (one to five thousand)")
    print("8. hard (1-10000) (one to ten thousand)")
    print("9. challenging (1-100000) (one to one hundred thousand)")
    print("10. difficult (1-1000000) (one to one million)")
    print("11. harsh (1-10000000) (one to ten million)")
    print("12. extreme (1-100000000) (one to one hundred million)")
    print("13. grueling (1-1000000000) (one to one billion)")
    print("14. surprise (random difficulty)")
    while True:
        difficulty = input("enter your choice (1-14): ")
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
            max_number = 500
            break
        elif difficulty == "6":
            max_number = 1000
            break
        elif difficulty == "7":
            max_number = 5000
            break
        elif difficulty == "8":
            max_number = 10000
            break
        elif difficulty == "9":
            max_number = 100000
            break
        elif difficulty == "10":
            max_number = 1000000
            break
        elif difficulty == "11":
            max_number = 10000000
            break
        elif difficulty == "12":
            max_number = 100000000
            break
        elif difficulty == "13":
            max_number = 1000000000
            break
        elif difficulty == "14":
            difficulty = str(random.randint(1, 13))
            max_number = difficulty_ranges[difficulty]
            print("your random difficulty is: " + difficulty_names[difficulty])
            print("guess a number between 1 and " + str(max_number))
            break
        else:
            print("choose a difficulty level 1-14 to begin")
   
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
                    print("the number must be between 1 and " + str(max_number))
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
        play_again = input("would you like to play again? please enter Y or N. Y/N: ")
print("thank you for playing")
