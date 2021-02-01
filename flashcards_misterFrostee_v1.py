import sys
import os
import time
from os import system, name as os_name
import pandas as pd

# I use the 'pandas' library to read the CSV file containing the flashcards data
# This gives me the contents of a file in a pandas 'DataFrame'
# A 'DataFrame' is a special kind of table that can be sliced and diced using simple functions
fc_data = pd.read_csv("flashcard_data.csv")
# I then use the 'sample' function (part of the pandas library) to shuffle it
# The 'frac' argument specifies what fraction of the rows I want to sample
# Since I've specified frac = 1, it will return all rows, but in a random order
fc_data_shuf = fc_data.sample(frac = 1)

# I want to be able to run this on Windows AND Linux.
# On Windows, the command to clear the screen is 'clear'
# On Linux, the command to clear the screen is 'cls'
# When the clear() function is called, it will use the right command,
# depending on the operating system. I get the operating system name
# using the 'name' function from the 'os' library
def clear():
    if os_name == 'nt':
        _ = system('clear')
    else:
        _ = system('cls')

def start_practice():
    count = 0
    for term, defn in zip(fc_data_shuf['Term'], fc_data_shuf['Definition']):
        print(f"Flashcard #{count+1} of {len(fc_data_shuf)}")
        print("")
        print("*" * (len(term)+2) + "**")
        print("* " + term + " *")
        print("*" * (len(term)+2) + "**")
        print("\nYour response:")
        input()
        print("")
        print(f"Answer: \n{defn}")
        print("\n\n[Press return to continue]"); input()
        count += 1
    if count >= len(fc_data_shuf):
        print("You've reached the end of the stack! Good job!")
        time.sleep(5)
        exit()

def main():
    clear()
    print("Do you wish to start learning? (Y/N)")
    choice = input("> ")
    # Regardless of whether the user provides input in uppercase or lowercase,
    # I make the input lowercase so that I need to check only one condition
    if choice.lower() == 'y':
        clear()
        start_practice()
    elif choice.lower() == 'n':
        clear()
        quit()
    else:
        clear()
        print("Sorry, I don't understand.")
        time.sleep(1)
        main()

# When the Python interpreter reads a .py file, it sets some 'special variables'
# It does the equivalent of adding this line to the top of your code:
# __name__ = "__main__"
# So now, there's a special variable called __name__ which holds the value "__main__"
# The benefit of doing this is, I execute this program by simply writing this command:
# python flashcards_misterFrostee_v2.py
if __name__ == "__main__":
    main()
