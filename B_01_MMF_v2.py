import pandas

# Functions go here
def int_check(question):
    """checks users enter an integer """

    error = "Oops - please enter an integer."
    print()

    while True:

        try:
            #change the response if it's an integer
            response = int(input(question))

            return response

        except ValueError:
            print(error)


def currency(x):
    """Formats numbers as currency ($#.##)"""
    return "${:.2f}".format(x)


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
        print()


#Main Routine goes here
# Initialise ticket numbers
MAX_TICKETS = 5
tickets_sold = 0

make_statement("Mini-Movie Fundraiser", "🍿")

print()
want_instructions = string_check("Do you want to read the instructions? ")


if want_instructions == "yes":
    instructions()

print()

# internalise variables / non-default options for string checker
payment_ans = ('cash', 'credit')

# Ticket Price List
CHILD_PRICE = 7.50
ADULT_PRICE = 10.50
SENIOR_PRICE = 6.50

# Credit card surcharge
CREDIT_SURCHARGE = 0.05

# lists to hold ticket details
all_names = []
all_ticket_costs = []
all_surcharges = []

mini_movie_dict = {
    'Name': all_names,
    'Ticket Price': all_ticket_costs,
    'Surcharge': all_surcharges
}



print()

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

        # Child ticket price is $7.50
    elif Age < 16:
        ticket_price = CHILD_PRICE

        # Adult ticket ($10.50)
    elif Age < 65:
        ticket_price = ADULT_PRICE

        # Senior Citizen ticket ($6.50)
    elif Age < 121:
        ticket_price = SENIOR_PRICE

    else:
        print(f"{name} is too old")
        continue

    # ask user for payment method (cash / credit / ca / cr)
    pay_method = string_check("Payment method: ", payment_ans, 2)
    print(f"payed using {pay_method}")

    if pay_method == "cash":
        surcharge = 0

    # if paying by credit, calculate surcharge
    else:
        surcharge = ticket_price * CREDIT_SURCHARGE

    # add name, ticket cost and surcharge to 'all_lists'
    all_names.append(name)
    all_ticket_costs.append(ticket_price)
    all_surcharges.append(surcharge)

    tickets_sold += 1

# End of Ticket Loop!

#create dataframe / table from directory
mini_movie_frame = pandas.DataFrame(mini_movie_dict)

# calculate the total payable and profit for each ticket
mini_movie_frame['Total']=  mini_movie_frame['Ticket Price'] + mini_movie_frame['Surcharge']
mini_movie_frame['Profit'] = mini_movie_frame['Ticket Price'] - 5

# Work out total paid and total profit...
total_paid = mini_movie_frame['Total'].sum()
total_profit = mini_movie_frame['Profit'].sum()

# Currency Formatting (uses currency function)
add_dollars = ['Ticket Price','Surcharge','Total','Profit']
for var_item in add_dollars:
    mini_movie_frame[var_item] = mini_movie_frame[var_item].apply(currency)

#Output movie fram without index
print(mini_movie_frame.to_string(index=False))

print()
print(f"Total Paid: ${total_paid:.2f}")
print(f"Total Profit: ${total_profit:.2f}")

if tickets_sold == MAX_TICKETS:
    print(f"You have sold all tickets")
else:
 print(f"You sold {tickets_sold} / {MAX_TICKETS} tickets")
