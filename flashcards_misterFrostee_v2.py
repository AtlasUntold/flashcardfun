import sys
import os
import time
from os import system, name as os_name
import random
import csv
# I'm using open() to read the file 'flashcard_data.csv' in 'r'ead mode
# csv.DictReader maps every row of the file to a 'dict'ionary
# It's necessary to tell csv.DictReader what the delimiter is (comma in this case)
fc_data = csv.DictReader(open("flashcard_data.csv", mode = "r"), delimiter = ",")
# fc_data is not a regular Python dict; it's a 'DictReader' object
# We need a regular Python dict that we can get keys and values from
# So I create an empty dict as follows
fc_data_dict = {}
# Now I go over each row item in 'fc_data' and get the 'Term' and 'Definition'
# separately into two temporary variables, 'key' and 'value'. Because 'fc_data_dict'
# is a completely  empty dict, I can't directly append anything into it.
# So I first check whether 'key' exists in 'fc_data_dict' (which it obviously doesn't)
# and initialize 'key' with no value. Then I append 'val' to the empty 'key'.
for row in fc_data:
    key = row['Term']
    val = row['Definition']
    if key not in fc_data_dict:
        fc_data_dict[key] = []
    fc_data_dict[key].append(val)
# Now, I want to shuffle the values to 'mix things up' for the learner. 
# However, random.shuffle() doesn't work on dict objects. So, I first
# convert 'fc_data_dict' from a dict into a list
fc_data_items_list = list(fc_data_dict.items())
# Now I shuffle this list
random.shuffle(fc_data_items_list)
# And then turn the shuffled list back into a dict
fc_data_dict_shuf = dict(fc_data_items_list)

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
    for term, defn in fc_data_dict_shuf.items():
        print(f"Flashcard #{count+1} of {len(fc_data_dict_shuf)}")
        print("")
        print("*" * (len(term)+2) + "**")
        print("* " + term + " *")
        print("*" * (len(term)+2) + "**")
        print("\nYour response:")
        input()
        print("")
        print(f"Answer: \n{str(defn).strip('[]')}")
        print("\n\n[Press return to continue]"); input()
        count += 1
        if count >= len(fc_data_dict_shuf):
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
