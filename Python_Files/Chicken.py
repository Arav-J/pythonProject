#!/usr/bin/env python
# encoding: utf-8
# Program by Arav
# Using a program to make a game, where one has to guess the randomly generated number between 1 and a 100;
import random

ASCII_DRAGON = """\
                 /           /                                               
                /' .,,,,  ./                                                 
               /';'     ,/                                                   
              / /   ,,//,`'`                                                 
             ( ,, '_,  ,,,' ``                                               
             |    /@  ,,, ;" `                                               
            /    .   ,''/' `,``                                              
           /   .     ./, `,, ` ;                                             
        ,./  .   ,-,',` ,,/''\,'                                             
       |   /; ./,,'`,,'' |   |                                               
       |     /   ','    /    |                                               
        \___/'   '     |     |                                               
THX 4    ',,'  |      /     `\                                              
PLAYING       /      |        ~\                                            
              '       (                                                      
             :                                                               
            ; .         \--                                                  
          :   \         ;
"""

stop_condition1: bool = False
while not stop_condition1:
    mistakes = 0
    lower_range: int = int(input("What is the minimum number of chickens on the farm?\n->"))
    upper_range: int = int(input("What is the maximum possible number of chickens on the farm?\n->"))
    if lower_range < 0:
        print(
            'Hmm, it seems you picked a lower value that is less than 0.\n Please make sure your lower value is '
            'positive :)\n You will now have to input both values again...')
        mistakes = mistakes + 1
        if mistakes == 2:
            print("Okay, okay mistakes happen, but 3rd time is the charm, right?")
        elif mistakes >= 3:
            print("You are a lost cause.")
    elif lower_range > upper_range:
        print(
            'Sorry, but can you please pick a lower value that is LOWER than the upper value. NOW, we are gonna have '
            'to go through all this again.\nSo...')
        mistakes = mistakes + 1
        if mistakes == 2:
            print("Okay, okay mistakes happen, but 3rd time's the charm, right?")
        elif mistakes >= 3:
            print("You are a lost cause.")
    elif lower_range == upper_range:
        print("IT'S NOT A RANGE IF YOU PICK THE SAME VALUE TWICE! Get it right this time.")
        mistakes = mistakes + 1
        if mistakes == 2:
            print("Okay, okay mistakes happen, but 3rd time is the charm, right?")
        elif mistakes >= 3:
            print("You are a lost cause.")
    else:
        stop_condition1 = True
    if mistakes >= 3:
        print("FINALLY WE DID IT! I ALWAYS KNEW YOU COULD DO IT!")


def colder():
    print("You are getting colder!")


def warmer():
    print("You are getting warmer!")


def neither():
    print("You are neither warmer nor colder ;)")


def ask_number(message: str) -> int:
    """Asks the user for a number, and asks again if the user gave an incorrect value.

    :param message: message to display when asking for a number
    :return: a valid integer provided by the user
    """
    global number
    assert isinstance(message, str), "message should be a string"
    stop_condition2 = False
    while not stop_condition2:
        try:
            number = int(input(message))
            if number < lower_range:
                print("Please pick a number within the range", lower_range, "and", upper_range, ".")
            elif number > upper_range:
                print("Please pick a number between", lower_range, "and", upper_range, ".")
            else:
                stop_condition2: bool = True
        except ValueError as ve:
            print("This is not a number.")
    return number


is_lower_range_valid = (lower_range >= 0)
is_upper_range_valid = (upper_range > lower_range)

if __name__ == '__main__':
    chicken: int = random.randint(lower_range, upper_range)
    n: int = 0
    # print(chicken)
    guess = ask_number('Please guess how many chickens you think there are on the farm?\n -> ')
    n += 1
    last_guess: int = guess
    while guess != chicken:
        if chicken - (0.1 * (upper_range - lower_range)) < guess < chicken:
            print('You are close! Try a little higher...')
            guess = ask_number('Please guess the number of chickens on the farm.\n -> ')
            print("Your guess was", guess, ". Your last guess was", last_guess, ".")
            if last_guess > chicken and guess > chicken:
                if ((last_guess - chicken) - (guess - chicken)) > 0:
                    print("You are getting colder!")
                elif ((last_guess - chicken) - (guess - chicken)) < 0:
                    print("You are getting warmer!")
            elif last_guess < chicken and guess < chicken:
                if ((last_guess - chicken) - (guess - chicken)) > 0:
                    print("You are getting colder!")
                elif ((last_guess - chicken) - (guess - chicken)) < 0:
                    print("You are getting warmer!")
            elif last_guess < chicken < guess:
                if (abs((last_guess - chicken) - (guess - chicken))) > 0:
                    print("You are getting warmer!")
                elif (abs((last_guess - chicken) - (guess - chicken))) > 0:
                    print("You are getting colder!")
                else:
                    print("You are neither warmer nor colder ;)")
            elif last_guess > chicken > guess:
                if (abs((last_guess - chicken) - (guess - chicken))) > 0:
                    print("You are getting colder")
                elif (abs((last_guess - chicken) - (guess - chicken))) < 0:
                    print("You are getting warmer")
                else:
                    print("You are neither warmer nor colder ;)")
            n += 1
            last_guess = guess
        elif chicken + (0.1 * (upper_range - lower_range)) > guess > chicken:
            print('You are close! Try a little lower...')
            guess = ask_number('Please guess the number of chickens on the farm.\n -> ')
            print("Your guess was", guess, ". Your last guess was", last_guess, ".")
            if last_guess > chicken and guess > chicken:
                if ((last_guess - chicken) - (guess - chicken)) > 0:
                    print("You are getting warmer!")
                elif ((last_guess - chicken) - (guess - chicken)) < 0:
                    print("You are getting colder!")
            elif last_guess < chicken and guess < chicken:
                if ((last_guess - chicken) - (guess - chicken)) > 0:
                    print("You are getting colder!")
                elif ((last_guess - chicken) - (guess - chicken)) < 0:
                    print("You are getting warmer!")
            elif last_guess < chicken < guess:
                if (abs((last_guess - chicken) - (guess - chicken))) > 0:
                    print("You are getting warmer!")
                elif (abs((last_guess - chicken) - (guess - chicken))) > 0:
                    print("You are getting colder!")
                else:
                    print("You are neither warmer nor colder ;)")
            elif last_guess > chicken > guess:
                if (abs((last_guess - chicken) - (guess - chicken))) > 0:
                    print("You are getting warmer")
                elif (abs((last_guess - chicken) - (guess - chicken))) < 0:
                    print("You are getting colder")
                else:
                    print("You are neither warmer nor colder ;)")
            n += 1
            last_guess = guess
        elif guess >= chicken + (0.1 * (upper_range - lower_range)):
            print('Pick a number a much lower then that!')
            guess = ask_number('Please guess the number of chickens on the farm.\n -> ')
            print("Your guess was", guess, ". Your last guess was", last_guess, ".")
            if last_guess > chicken and guess > chicken:
                if ((last_guess - chicken) - (guess - chicken)) > 0:
                    print("You are getting warmer!")
                elif ((last_guess - chicken) - (guess - chicken)) < 0:
                    print("You are getting colder!")
            elif last_guess < chicken and guess < chicken:
                if ((last_guess - chicken) - (guess - chicken)) > 0:
                    print("You are getting colder!")
                elif ((last_guess - chicken) - (guess - chicken)) < 0:
                    print("You are getting warmer!")
            elif last_guess < chicken < guess:
                if (abs((last_guess - chicken) - (guess - chicken))) > 0:
                    print("You are getting colder!")
                elif (abs((last_guess - chicken) - (guess - chicken))) > 0:
                    print("You are getting warmer!")
                else:
                    print("You are neither warmer nor colder ;)")
            elif last_guess > chicken > guess:
                if (abs((last_guess - chicken) - (guess - chicken))) > 0:
                    print("You are getting warmer")
                elif (abs((last_guess - chicken) - (guess - chicken))) < 0:
                    print("You are getting colder")
                else:
                    print("You are neither warmer nor colder ;)")
            n += 1
            last_guess = guess
        elif guess <= chicken - (0.1 * (upper_range - lower_range)):
            print('Pick a number much higher then that')
            guess = ask_number('Please guess the number of chickens on the farm.\n -> ')
            print("Your guess was", guess, ". Your last guess was", last_guess, ".")
            if last_guess > chicken and guess > chicken:
                if ((last_guess - chicken) - (guess - chicken)) > 0:
                    print("You are getting warmer!")
                elif ((last_guess - chicken) - (guess - chicken)) < 0:
                    print("You are getting colder!")
            elif last_guess < chicken and guess < chicken:
                if ((last_guess - chicken) - (guess - chicken)) > 0:
                    print("You are getting colder!")
                elif ((last_guess - chicken) - (guess - chicken)) < 0:
                    print("You are getting warmer!")
            elif last_guess < chicken < guess:
                if (abs((last_guess - chicken) - (guess - chicken))) > 0:
                    print("You are getting colder!")
                elif (abs((last_guess - chicken) - (guess - chicken))) < 0:
                    print("You are getting warmer!")
                else:
                    print("You are neither warmer nor colder ;)")
            elif last_guess > chicken > guess:
                if (abs((last_guess - chicken) - (guess - chicken))) > 0:
                    print("You are getting warmer")
                elif (abs((last_guess - chicken) - (guess - chicken))) < 0:
                    print("You are getting colder")
                else:
                    print("You are neither warmer nor colder ;)")
            n += 1
            last_guess = guess
    print("Congratulations! You have guessed correctly!")
    print(ASCII_DRAGON)
    if n <= 7:
        print('Wow! You are really good at this, it took you only', n, 'guesses!')
    else:
        print('You are bad at this XD, it took you', n, 'guesses!')
