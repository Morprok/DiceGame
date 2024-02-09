print("🎲🎲 Roll it 13 🎲🎲")

while True:
    want_instructions = input("Do you want to read the instructions?  ").lower()

    if want_instructions == 'yes' or 'y':
         print("You chose yes")
    elif want_instructions == 'no' or 'n':
        print("you chose no")
    else:
        print("You did not choose a valid response")
