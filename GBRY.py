# import random
# from typing import List, Type
#
# element_list: list = ['G', 'R', 'B', 'Y']
#
#
# def generate_code() -> list[str]:
#     code = [random.choice(element_list) for i in range(4)]
#     print(code)
#     return code
#
#
# def ask_guess() -> Type[list]:
#     string = input("This is just the testing zone. Pick 4 characters of {G, R, B, Y}, "
#                    "they can be repeated.\n -> ")
#     string = string.upper().strip()
#     ignored_chars = [' ', '-']
#     for char in ignored_chars:
#         string = string.replace(char, '')
#     code = List[string]
#     return code
#
#
# def evaluation(final) -> bool:
#     red = 0
#     white = 0
#     code = [random.choice(element_list) for i in range(4)]
#     string = input("This is just the testing zone. Pick 4 characters of {G, R, B, Y}, "
#                    "they can be repeated.\n -> ")
#     if (code[i]) == (string[i]):
#         print("Correct!")
#
#
#
# if __name__ == '__main__':
#     generate_code()
#     ask_guess()


# There are 4 Elements comprised of {G, R, B, Y}, that are used to create a
# randomly generate a code for a user to guess.

import random
from typing import List, Tuple

Character_List: list = ["G", "R", "B", "Y"]


def decide_the_code() -> List[str]:
    """
    Generate a code of the 4 characters R, G, B, Y.
    """
    final_code = [None, None, None, None]
    for i in range(4):
        random_character: str = random.choice(Character_List)
        final_code[i] = random_character
    return final_code

# def ask_guess() -> List[str]:
#     """
#     Asking for a guess from the user, also adjusting the input to make the
#     user experience easier for minute differences in the code.
#     """
#     while True:
#         guess = input("This is just the testing zone. Pick 4 characters of {G, R, B, Y}, "
#                        "they can be repeated.\n -> ")
#         # cleaning the guess: all-capitals, remove spaces from sides (strip)
#         guess = guess.upper().strip()
#         ignored_chars = [' ', '-']
#         for char in ignored_chars:
#             guess = guess.replace(char, '')
#         # end of cleaning
#         final_code = list(guess)
#         if validation(final_code):
#             return final_code


def validation(final_code: List[str]) -> bool:
    """
    This checks whether or not there are a correct number of characters.
    """
    if len(final_code) != 4:
        if len(final_code) < 4:
            print("You put", (len(final_code)), "characters - that's too low.\n")
        elif len(final_code) > 4:
            print("You put", (len(final_code)), "characters - that's too high.\n")
        print("Code has to have only 4 characters")
        return False

    for character in final_code:
        if character not in Character_List:
            print("This", character, "is not one of the characters - G, B, R and Y.")
            return False
        print("This", character, "is accepted.")
    return True


def evaluation(final_code: List[str], guess: List[str]) -> Tuple[int, int]:
    """
    Outputting 2 values that indicate to the user how accurate their guess is compared to the actual answer.
    """
    red = 0
    white = 0

    if final_code[0] == guess[0]:
        red += 1
        # final_code.pop(0)

    if final_code[1] == guess[1]:
        red += 1
        # final_code.pop(1)

    if final_code[2] == guess[2]:
        red += 1
        # final_code.pop(2)

    if final_code[3] == guess[3]:
        red += 1
        # final_code.pop(3)

    if final_code[0] == guess[1] or guess[2] or guess[3]:
        white += 1

    if final_code[1] == guess[0] or guess[2] or guess[3]:
        white += 1

        if final_code[0] == guess[0] and final_code[1] == guess[0]:
            white -= 1
        if final_code[0] == guess[1] and final_code[1] == guess[1]:
            white -= 1
        if final_code[0] == guess[2] and final_code[1] == guess[2]:
            white -= 1
        if final_code[0] == guess[3] and final_code[1] == guess[3]:
            white -= 1

    if final_code[2] == guess[0] or guess[1] or guess[3]:
        white += 1
        if final_code[0] == guess[0] and final_code[2] == guess[0]:
            white -= 1
        if final_code[0] == guess[1] and final_code[2] == guess[1]:
            white -= 1
        if final_code[0] == guess[2] and final_code[2] == guess[2]:
            white -= 1
        if final_code[0] == guess[3] and final_code[2] == guess[3]:
            white -= 1

        if final_code[1] == guess[0] and final_code[2] == guess[0]:
            white -= 1
        if final_code[1] == guess[1] and final_code[2] == guess[1]:
            white -= 1
        if final_code[1] == guess[2] and final_code[2] == guess[2]:
            white -= 1
        if final_code[1] == guess[3] and final_code[2] == guess[3]:
            white -= 1

    if final_code[3] == guess[0] or guess[1] or guess[2]:
        white += 1
        if final_code[0] == guess[0] and final_code[3] == guess[0]:
            white -= 1
        if final_code[0] == guess[1] and final_code[3] == guess[1]:
            white -= 1
        if final_code[0] == guess[2] and final_code[3] == guess[2]:
            white -= 1
        if final_code[0] == guess[3] and final_code[3] == guess[3]:
            white -= 1

        if final_code[1] == guess[0] and final_code[3] == guess[0]:
            white -= 1
        if final_code[1] == guess[1] and final_code[3] == guess[1]:
            white -= 1
        if final_code[1] == guess[2] and final_code[3] == guess[2]:
            white -= 1
        if final_code[1] == guess[3] and final_code[3] == guess[3]:
            white -= 1

        if final_code[2] == guess[0] and final_code[3] == guess[0]:
            white -= 1
        if final_code[2] == guess[1] and final_code[3] == guess[1]:
            white -= 1
        if final_code[2] == guess[2] and final_code[3] == guess[2]:
            white -= 1
        if final_code[2] == guess[3] and final_code[3] == guess[3]:
            white -= 1

    if red == 4 or red == 3:
        white = 0

    return red, white


if __name__ == '__main__':
    # final_code = decide_the_code()
    #
    # print('final code:', final_code)
    # print("example: ['R', 'G', 'B', 'Y']")

    # guess = input("Great now that we have established you can count it's time for your official guess "
    #                "- guess the order that the 4 characters 'GBRY' are in, repetitions of letters are allowed.\n -> ")

    examples = [
        (['R', 'G', 'G', 'B'], ['G', 'G', 'G', 'G'], (2, 0)),
        # W
        (['R', 'G', 'G', 'B'], ['G', 'G', 'Y', 'Y'], (1, 1)),
        # L
        (['R', 'G', 'G', 'B'], ['G', 'G', 'Y', 'G'], (1, 1)),
        # W
        (['R', 'G', 'G', 'B'], ['B', 'G', 'Y', 'R'], (1, 2)),
        # L
        (['R', 'G', 'G', 'B'], ['B', 'G', 'Y', 'Y'], (1, 1)),
        # L
        (['R', 'G', 'G', 'B'], ['B', 'Y', 'Y', 'B'], (1, 0)),
        # L
        (['R', 'G', 'G', 'B'], ['B', 'G', 'G', 'B'], (3, 0)),
        # L
        (['R', 'G', 'G', 'B'], ['Y', 'Y', 'Y', 'Y'], (0, 0)),
        # L
        (['R', 'G', 'G', 'B'], ['B', 'R', 'R', 'R'], (0, 2)),
        # L
        (['R', 'G', 'G', 'B'], ['R', 'G', 'G', 'B'], (4, 0)),
        # L
        (['R', 'G', 'G', 'B'], ['B', 'R', 'B', 'G'], (0, 3)),
        # W
        (['R', 'G', 'G', 'B'], ['Y', 'B', 'Y', 'Y'], (0, 1)),
        # L
    ]
    for (code1, code2, expected_value) in examples:
        found_value = evaluation(code1, code2)
        print('----------------------')
        print('-> expected:', expected_value)
        print('-> found:   ', found_value)
    # ask_guess()
    # evaluation()
