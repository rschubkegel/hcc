'''
- Create a dictionary of 2+ commands
- Use a loop to print all commands & instructions
- Get command from user and perform relevant action

https://hcc.rschubkegel.com/2024/fall/computer-science/slides/python-dictionaries/
'''

purr_command = "purr"
purr_message = '''
 |\\__/,|   (`\\
 |_ _  |.--.) )
 ( T   )     /
(((^_(((/(((_/
'''

meow_command = "meow"
meow_message = '''
 _._     _,-'""`-._
(,-.`._,'(       |\\`-/|
    `-.-' \\ )-`( , o o)
          `-    \\`_`"'-
'''

trap_command = "trap"
trap_message = '''
  ,-.       _,---._ __  / \\
 /  )    .-'       `./ /   \\
(  (   ,'            `/    /|
 \\  `-"             \\'\\   / |
  `.              ,  \\ \\ /  |
   /`.          ,'-`----Y   |
  (            ;        |   '
  |  ,-.    ,-'         |  /
  |  | (   |            | /
  )  |  \\  `.___________|/
  `--'   `--'
'''

descriptions = {
    purr_command: "Makes biscuits",
    meow_command: "Gets the zoomies",
    trap_command: "Succumbs to the cat trap",
}

messages = {
    purr_command: purr_message,
    meow_command: meow_message,
    trap_command: trap_message,
}

# Print the "welcome" banner
print("Welcome to...")
print()
print("/-----------------\\")
print("|  CAT COMMANDER  |")
print("\\-----------------/")
print()

# Print commands and descriptions to user
for command in descriptions:
    description = descriptions[command]
    print(f"- {command}\t: {description}")

# Get user's command
print()
command = input("Enter a command: ").strip().lower()
print()

# If command is valid, print the corresponding message,
# otherwise print an error message
if command in messages:
    print(messages[command])
else:
    print(f'Invalid command "{command}"')
