# Carol Wong
# UPenn ID: 57485844
# Homework 2 - Pigs
# Statement of Work:
# Worked alone with help from the following resources:
# https://stackoverflow.com/questions/22596827/nameerror-name-random-is-not-defined
# https://stackoverflow.com/questions/24110282/python-error-unsupported-operand-types-for-int-and-nonetype
# https://stackoverflow.com/questions/21122540/input-error-nameerror-name-is-not-defined
# https://stackoverflow.com/questions/17534345/typeerror-missing-1-required-positional-argument-self
# https://careerkarma.com/blog/python-missing-required-positional-argument-self/
# https://github.com/projectmesa/mesa/issues/308
# https://stackoverflow.com/questions/43708541/python-typeerror-typeerror-not-supported-between-instances-of-nonetype
# https://stackoverflow.com/questions/38836795/typeerror-int-argument-must-be-a-string-a-bytes-like-object-or-a-number-not/38838589
# https://stackoverflow.com/questions/492387/indentationerror-unindent-does-not-match-any-outer-indentation-level
# https://poweruser.blog/setting-a-breakpoint-in-python-438e23fe6b28

import random


def instructions():
    """Tell the user the rules of the game."""
    print("****************************************************************************************")
    print("Welcome to the game of Pig.")
    print("In this game, there are two players: you vs. the computer.")
    print("On each turn, a player rolls a six-sided dice as many times as he wishes,")
    print("or until he rolls a 6.")
    print("Each number he rolls, except a 6, is added to the player's score this turn;")
    print("but if the player rolls a 6, his score for this turn is zero, and his turn ends.")
    print("At the end of each turn, the score for the turn is added to his total score.")
    print("The first player to reach or exceed 50 wins.")
    print("The first player has an advantage. To make the gamer more fair,")
    print("if the first player reaches or exceeds 50, the second player gets one additional turn.")
    print("****************************************************************************************")
    print(" ")


def roll():
    """Dice roll randomizer. There are 6 sides to this die."""
    return random.randint(1, 6)


def computer_move(computer_score, human_score):
    """This function rolls a dice for the computer some number of times, displays the result of each roll,
    and returns the total of rolls. In order to beat the human opponent, the computer continues to roll until
    it gets a 6 (which is equaled to 0). This function returns the computer score."""
    take_turn = True  # Sets a default value of True to take_turn, which indicates a turn can be taken
    while take_turn:  # While a turn is being taken
        x = roll()  # Rolls the dice using the roll() function
        if x == 6:  # If this roll is 6
            computer_score += 0  # The computer's score stays the same
            take_turn = False  # The computer's turn is over, changing take_turn to False
            print("The computer has rolled a " + str(x) + " which doesn't count, so its total score is now " + str(
                computer_score) + "! It's now your turn!")  # prints this dice roll result to the user
        else:  # If this roll is 1, 2, 3, 4, or 5
            computer_score += x  # This roll is added to the computer's score
            print("The computer has rolled a " + str(x) + ", so its total score is now " + str(computer_score) + "!")
            # ^ prints this dice roll result ot the user
    show_current_status(computer_score, human_score)
    return computer_score  # This while loop returns the computer_score to main


def human_move(computer_score, human_score):
    """This function rolls a dice for the human some number of times, displays the result of each roll, until
    the user says No to rolling again. Each roll is added to the human score, except a 6 (which is equaled to 0).
    This function returns the human score.
    """
    take_turn = True    # Sets of value to take_turn, which indicates that a turn will be taken, to True.
    while take_turn:
        if not ask_yes_or_no(take_turn):    # If the user says No to rolling again, break out of this loop.
            break
        else:                               # Otherwise, continue this loop
            x = roll()                      # Rolls the dice
            if x == 6:                      # If the roll is 6
                human_score += 0            # 0 is added to the human score and the loop does not continue
                print("You've rolled a " + str(x) + " which doesn't count , so your total score is now " + str(
                    human_score) + "! It's the computer's turn!")
            else:                           # If the roll is 1, 2, 3, 4, or 5
                human_score += x            # The roll is added to the human score and the loop continues to run
                print("You've rolled a " + str(x) + ", so your total score is now " + str(human_score) + "!")
                continue
        show_current_status(computer_score, human_score)
        return human_score                  # At the end of this loop, this function returns the human_score


def ask_yes_or_no(prompt):
    """Prints a question to the user asking whether he wants to roll again. If yes, return True.
    If no, return False. If something else, repeat the question."""
    while True:                             # Once this function is triggered, always ask
        a = input("Would you like to roll / roll again? Y/N: ")     # Display this question and gets the input
        if a[0] == "Y" or a[0] == "y":          # If yes, this function is true
            return True
        elif a[0] == "N" or a[0] == "n":        # If no, this function is false
            return False
        else:                                   # If something else is inputted, ask the question again
            continue


def is_game_over(computer_score, human_score):
    """Returns True if either player have score of 50 or more, and the players are not tied.
    Otherwise it returns False."""
    if (computer_score >= 50 or human_score >= 50) and computer_score != human_score:
        # if the first player (the computer)'s score is equal to or exceeds 50, and the scores are not tied,
        # the function returns True and the game is over
        return True
    else:
        return False    # otherwise return False and the game is not over


def show_current_status(computer_score, human_score):
    """Prints the user's current score and the computer's current score, how far behind (or ahead) the user is,
    or if there is a tie."""
    if human_score > computer_score:                # prints the status if human is winning
        print("********* CURRENT SCOREBOARD *********")
        print("Your score: " + str(human_score))
        print("Computer score: " + str(computer_score))
        print("You are winning by " + str(human_score - computer_score) + " points!")
        print("**************************************")

    elif human_score < computer_score:              # prints the status if computer is winning
        print("********* CURRENT SCOREBOARD *********")
        print("Your score: " + str(human_score))
        print("Computer score: " + str(computer_score))
        print("You are losing by " + str(computer_score - human_score) + " points!")
        print("**************************************")
    else:
        print("********* CURRENT SCOREBOARD *********")
        print("Your score: " + str(human_score))
        print("Computer score: " + str(computer_score))
        print("You are tied with the computer!")    # prints the status if players are tied
        print("**************************************")
        return computer_score and human_score


def show_final_results(computer_score, human_score):
    """Tells whether the human won or lost, and by how much. This function is called when the game ends."""
    if human_score > computer_score:                # prints the final result if human wins
        print("************ FINAL SCORE ************")
        print("Your score: " + str(human_score))
        print("Computer score: " + str(computer_score))
        print("You have won by " + str(human_score - computer_score) + " points!")
        print("*************************************")
    elif human_score < computer_score:              # prints the final result if computer wins
        print("************ FINAL SCORE ************")
        print("Your score: " + str(human_score))
        print("Computer score: " + str(computer_score))
        print("You have lost by " + str(computer_score - human_score) + " points!")
        print("*************************************")
    else:                                           # prints the final result if players tied
        print("************ FINAL SCORE ************")
        print("Your score: " + str(human_score))
        print("Computer score: " + str(computer_score))
        print("You are tied with the computer!")
        print("*************************************")

def main():
    """This function executes the game. It sets the default computer score and human score to 0,
    then executes the instructions function. After that, it checks if the game is over. If the game is not over,
    it will continue to tally the computer and human scores. If the game is over,
    it will show the final result."""
    computer_score = 0
    human_score = 0
    instructions()
    game_over = False
    while not game_over:
        computer_score = computer_move(computer_score, human_score)
        human_score = human_move(computer_score, human_score)
        if is_game_over(computer_score, human_score):
            show_final_results(computer_score, human_score)
            return True
        else:
            continue


if __name__ == '__main__':
    main()
