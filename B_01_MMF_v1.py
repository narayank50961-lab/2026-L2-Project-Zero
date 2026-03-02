# Functions go here
def int_check(question):
    """checks users enter an integer """

    error = "Oops - please enter an integer."

    while True:

        try:
            #change the response if it's an integer
            response = int(input(question))

            return response

        except ValueError:
            print(error)


def make_statement(statement, decoration):
    """Emphasises heading by adding decoration
    at the start and end"""

    print(f"{decoration * 3} {statement} {decoration * 3}")


def instructions():
    make_statement("instructions", "🍿")


def not_blank(question):
    """Checks that a user response is not blank"""

    while True:
        response = input(question)

        if response != "":
            return response

        print("Sorry, this can't be blank. Please try again. \n")

def string_check(question, valid_answers=("yes", "no"), num_letters=1):
    """check that users enter the fill word or the first
  letter of a word from a list of valid responses"""
    while True:

        response = input(question).lower()

        for item in valid_answers:
            if response == item:
                return item
            # check if it's the first letter
            elif response == item[:num_letters]:
                return item

        print(f"Please choose an option from {valid_answers}")


#Main Routine goes here
# Initialise ticket numbers
MAX_TICKETS = 5
tickets_sold = 0

make_statement("Mini-Movie Fundraiser", "🍿")

print()
want_instructions = string_check("Do you want ticket")

if want_instructions == "yes":
    instructions()

print()

# internalise variables / non-default options for string checker
payment_ans = ('cash', 'credit')

# loop for testing purposes...
while True:
    print()

    # ask user for their name (and check it's not blank)
    name = not_blank("Name: ")
    if name == "xxx":
        break

    # Ask for their age and check it's between 12 and 120
    Age = int_check("Age: ")

    # Output error message / success message
    if Age < 12:
        print(f"{name} is too young")
        continue
    elif Age > 120:
        print(f"{name} is too old")
        continue
    else:
        pass

    # ask user for payment method (cash / credit / ca / cr)
    pay_method = string_check("Payment method: ", payment_ans, 2)
    print(f"payed using {pay_method}")
