import random
from questions import glossary

def pick_number():
    top_number = input("Type the top number: ") #Input the highest possible number for the range

    if top_number.isdigit():
        top_number = int(top_number)

        if top_number <= 0:
            print("Type a number larger than zero")
    else:
        print("Type a number next time")
        quit()


    random_number = random.randint(0, top_number)
    guesses = 0

    while True:
        guesses += 1
        user_guess = input("Make a guess: ")
        if user_guess.isdigit():
            user_guess = int(user_guess)

            if user_guess >= top_number:
                print("Please type a number smaller than the top number.")
                continue
        else:
            print("Please type a number next time.")
            continue

        if user_guess == random_number:
            print("You got it!")
            break
        else:
            print("You got it wrong")

    print("You got it in " + str(guesses) + " guesses!")

def quiz_project():

    def check_ans(question, ans, attempts, score):
        """Takes the arguments, and confirms if the answer provided by user is correct.
        Converts all answers to lower case to make sure the glossary is not case sensitive."""

        if glossary[question]['answer'].lower() == ans.lower():
            print(f"Correct Answer! \nYour score is {score + 1}!")
            return True
        else:
            print(f"Wrong Answer :( \nYou have {attempts - 1} left! \nTry again...")
            return False

    def print_glossary():
        for question_id, ques_answer in glossary.items():
            for key in ques_answer:
                print(key + ':', ques_answer[key])

    print("Capital City Quiz!!")

    def intro_msg():
        # Introductory message for the game
        print("Welcome to this fun Capital City Quiz! \nLets see how many capitals of the world you know.")
        print("There are a total of 6 questions, you can skip at any time by typing 'skip.'")
        intro_answer = input("Press any key to play or type 'leave' to leave. ")
        intro_answer = intro_answer.lower()
        if intro_answer == "leave":
            quit()
        else:
            return True

    intro = intro_msg()
    while True:
        score = 0
        for question in glossary:
            attempts = 3
            while attempts > 0:
                print(glossary[question]['question'])
                answer = input("Enter Answer (To move to the next question, type 'skip') : ")
                answer = answer.lower()
                if answer == "skip":
                    break
                check = check_ans(question, answer, attempts, score)
                if check:
                    score += 1
                    break
                attempts -= 1

        break

    print(f"Your final score is {score}!\n")
    if score < 6:
        print("In case you want to know the correct answers, they will be below this message.")
        print_glossary()
    else:
        print("Congratulations!")
    print("Thanks for playing")

def games_picker(): #This is the function that will call all the other functions using dictionary

    print("Welcome to game chooser, we currently have two games available:\n 1. Number guesser\n 2. Capital Cities Quiz.")
    game = input("Enter the number of the game you want to play: " )
    function_dict = {'1': pick_number, '2': quiz_project}
    game = function_dict[game]()
    print(game)

games_picker()