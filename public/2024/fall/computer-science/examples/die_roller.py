'''
Simulates rolling a single die with user-specified number of faces.
The total number of rolls are stored in a file and accumulated between sessions.

Full specification:
https://hcc.rschubkegel.com/2024/fall/computer-science/assignments/dice-roll-sim/
'''

import os
import random

# Path to the file that will store the total number of dice rolls
FILE_PATH = "dice_rolls.txt"

# Store each roll (from this session) in a list
rolls = []

# Ask user how many faces for their die
faces = int( input("How many faces is your die? ") )
print()

# Loop until user decides to quit
command = None
while command != "q":

    # Get user input
    command = input('Press "r" to roll or "q" to quit: ').strip().lower()
    print()

    # Roll dice and add to list of rolls
    if command == "r":
        roll = random.randint(1, faces)
        rolls.append(roll)
        print(f"You rolled: {roll}")
        print()

    # Only other valid command is quit; if that is not entered,
    # print an error message
    elif command != "q":
        print(f'Invalid command "{command}"')
        print()

    # If command was quit, do nothing!
    # (while loop will break automatically because condition is false)

# If file exists, read the total number of rolls from previous sessions
if os.path.exists(FILE_PATH):

    # If file exists, open in "read text" mode
    # (and let Python automatically close the file)
    with open(FILE_PATH, "rt") as file:

        # Read the content of the file
        string = file.read()

        # Strip whitespace around digits
        string = string.strip()

        # Convert digits to an integer
        previous_roll_count = int(string)

# If file did not exist, there have been no previous sessions
# so previous rolls is 0
else:
    previous_roll_count = 0

# Add previous rolls to current rolls
total_roll_count = len(rolls) + previous_roll_count

# Print the highest roll, number of session rolls, and number of all-time rolls
print(f"Highest session roll         : {max(rolls)}")
print(f"Number of rolls this session : {len(rolls)}")
print(f"Number of all-time rolls     : {total_roll_count}")

# Save rolls to file
# (and let Python automatically close the file)
with open(FILE_PATH, "wt") as file:

    # Convert integer to string so we can write to text file
    string = str(total_roll_count)

    # Write to file!
    file.write(string)