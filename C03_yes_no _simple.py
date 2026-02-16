#funtions go here...
def yes_no(question):
    """Checkes that users enter yes / y or no/ n toa question"""

    while True:
        response = input(question).lower()

        if response == "yes" or response == "y":
            return "yes"
        elif response == "no" or response == "n":
            return "no"
        else:
            print("Please enter yes (y) or no (n) . \n")


#main routine goes here

#loop for testing purposes...
while True:
    want_instructions = yes_no("do you want to read the instructions? ")
    print(f"You chose {want_instructions}\n")



# Main routine goes here