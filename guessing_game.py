#!/usr/bin/env python3

# Created by: Michael Clermont
# Created on: Mar 2022
# This program is a guessing game

import random


def main():
    # this function shows formatting output

    counter = 0
    # input
    random_number = random.randint(0, 9)
    # process & output
    while True:
        try:
            number_from_user = int(input("Enter a number between 0-9: "))
            counter = counter + 1
            if number_from_user == random_number:
                print("\nYou guessed correctly in {0} times!".format(counter))
                break
            elif random_number > number_from_user:
                print("\nNext time guess higher")
            elif random_number < number_from_user:
                print("\nNext time guess lower")
        except Exception:
            print("\nThat is not an integer, guess again.")
        finally:
            print("")


if __name__ == "__main__":
    main()
