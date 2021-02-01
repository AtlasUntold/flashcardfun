from sys import exit
from os import system
import random
import sys
import time
import re

def clear():
    _ = system('clear')

########## Terms and definitions
Terms_and_definitions = '''

'''

# Assigning terms and definitions to variables
T1 = "This is term 1"
T2 = "This is term 2"

D1 = "This is definition 1"
D2 = "This is definition 2"

# define dict
flashcards = {
    T1: D1,
    T2: D2
}

# define list = [flashcard_dictionary]
flashcard_list = [{T1: D1}, {T2: D2}]

# inverts flashcard list to allow the term to be called upon without the definition
flashcards_inverted = {
    v: k for k, v in flashcards.items()
}

switch = False
count = 0

def read_loop():
    global count
    print(f"Flashcard #{count} of {len(flashcard_list)}")
    print("\n")
    print("*" * len(flashcards_inverted[D1]) + "**")
    print("*" + flashcards_inverted[D1] + "*")
    print("*" * len(flashcards_inverted[D1]) + "**")
    print("\n \tYour response:")
    input()
    print(f"\tAnswer: \n {flashcards[T1]}")
    print("\n\n[Press return to continue]"); input()
    call_()

def call_():
    global count
    random.shuffle(flashcard_list)
    if count < len(flashcard_list):
        count += 1
        read_loop()
    elif count == len(flashcard_list):
        print("You've reached the end of the stack! Good job!")
        time.sleep(5)
        exit()
def start_():
    clear()
    print("Do you wish to start learning?")
    print("Type 'Y' or 'N'")
    choice = input("> ")
    if choice == 'Y' or choice == 'y':
        clear()
        call_()
    elif choice == 'N' or choice == 'n':
        clear()
        quit()
    else:
        clear()
        print("Sorry, I don't understand.")
        time.sleep(1)
        start_()
        



start_()
