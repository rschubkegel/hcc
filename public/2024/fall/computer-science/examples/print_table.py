# Define a function that prints a horizontal line
def print_horizontal_line(table):
  for item in table:
    # Get the length of the item (string)
    item_length = len(item)
    # Add 4 since each item is printed with 2 bars and 2 spaces
    item_length = item_length + 4
    # Create a line of dashes that is x characters long
    line = '-' * item_length
    # Print the line
    print(line, end='')

# Define a function that prints table cells
def print_table(table):
  print_horizontal_line(table)
  print()

  # Print each item in list
  for item in table:
    print('|', end='')
    print(' ' + item + ' ', end='')
    print('|', end='')
  print()

  print_horizontal_line(table)
  print()

# Call your function!
print_table( ["Ava", "is", "cool"] )
print_table( ["Kylan", "is", "awesome"] )
