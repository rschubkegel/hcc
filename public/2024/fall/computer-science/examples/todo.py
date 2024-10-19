'''
Author:       Rylan
Date:         2024-09-26
Description:  A simple to-do list program.
              Created for week 4 assignment (see slide deck for specs).
Reference:    https://hcc.rschubkegel.com/2024/fall/computer-science/slides/python-lists
'''

# Setup variables
SEPARATOR_WIDTH = 24
list = []

# Print welcome
message = 'TO DO TRACKER'
print('-' * SEPARATOR_WIDTH)
print(message.rjust(SEPARATOR_WIDTH // 2 + len(message) // 2))
print('-' * SEPARATOR_WIDTH)

# Until user quits, keep looping
should_continue = True
while should_continue:
  # Print instructions
  print("\nPlease select a command:")
  print("\tl\tPrint my todo list")
  print("\ta\tAdd an item")
  print("\tr\tRemove an item")
  print("\tq\tQuit the program")

  # Get input
  command = input("\n>>\t").strip().lower()
  print()

  # If user types "l" print the list
  if command == "l":
    if len(list) == 0:
      print('List is empty!')
    else:
      for item in list:
        print(f'- {item}')
  
  # If user types "a" add to the list
  elif command == "a":
    print('What do you need to do?')
    item = input("\n>>\t").strip().lower()
    list.append(item)
  
  # If user types "r" or "d" remove from the list
  elif command == "r":
    print('What did you accomplish?')
    item = input("\n>>\t").strip().lower()
    list.remove(item)
  
  # If user types "q" exit the loop
  elif command == "q":
    should_continue = False

  # If user did not type a valid command, let them know
  else:
    print('Invalid command! Please select from one the listed options.')
    print()

# Print farewell
message = 'GOODBYE!'
print('-' * SEPARATOR_WIDTH)
print(message.rjust(SEPARATOR_WIDTH // 2 + len(message) // 2))
print('-' * SEPARATOR_WIDTH)