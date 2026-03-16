import pandas

import random

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

    return f"{decoration * 3} {statement} {decoration * 3}"


def instructions():
    print(make_statement("instructions", "🍿"))

    print(''' 

For each ticket holder enter ...
- Their name 
- Their age
- The payment method (cash / credit)

The program will record the ticket sale and calculate the ticket cost (and the profit)

Once you have either sold all of the tickets or entered the exit code ('xxx'), 
the program will display the ticket sales
information and write the data to a text file

''')


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

# Program main heading
print(make_statement("Mini-Movie Fundraiser Program", "🍿"))

#Ask user if they want to see instructions
# and display them if necessary
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

# choose random winner
winner = random.choice(all_names)

# find index of winner (ie: position in list)
winner_index = all_names.index(winner)


# retrieve winner Ticket Price and Profit (so we can adjust
# Profit numbers so that the winning ticket is excluded
ticket_won = mini_movie_frame.at[winner_index, 'Total']
profit_won = mini_movie_frame.at[winner_index, 'Profit']

# Currency Formatting (uses currency function)
add_dollars = ['Ticket Price','Surcharge','Total','Profit']
for var_item in add_dollars:
    mini_movie_frame[var_item] = mini_movie_frame[var_item].apply(currency)

#Output movie fram without index
mini_movie_string = mini_movie_frame.to_string(index=False)

total_paid_string = f"Total Paid: ${total_paid:.2f}"
total_profit_string = f"Total Profit: ${total_profit:.2f}"


# winner announcement
lucky_winner_string = (f"The lucky winner is {winner}. "
                       f"Their ticket worth ${ticket_won:.2f} is free!")
final_total_paid_string = f"Total Paid is now ${total_paid - ticket_won:.2f}"
final_profit_string = f"Total Profit is now ${total_profit - profit_won:.2f}"

if tickets_sold == MAX_TICKETS:
    num_sold_string = make_statement(f"You have sold all tickets "
                                     f"(ie: {MAX_TICKETS} tickets)", "-")
else:
 num_sold_string = make_statement(f"You sold {tickets_sold} / "
                                  f"{MAX_TICKETS} tickets", "-")

# Additional strings / Headings
heading_string = make_statement("Mini Movie Fundraiser","=")
Ticket_details_heading = make_statement("Ticket Details","-")
raffle_heading = make_statement("--- Raffle Winner ---","-")
adjusted_sales_heading = make_statement("Adjusted Sales & Profit",
                                        "-")
adjusted_explanation = (f"We have give away a ticket worth ${ticket_won:.2f} which means \nour"
                        f"sales have decreased by ${ticket_won:.2f} and our profit"
                        f"decreased by ${profit_won:.2f}")

# List of strings to be outputted / written to file
to_write = [heading_string, "\n" ,
            Ticket_details_heading,
            mini_movie_string, "\n",
            total_paid_string,
            total_profit_string, "\n",
            raffle_heading,
            lucky_winner_string, "\n",
            adjusted_sales_heading,
            adjusted_explanation, "\n",
            final_total_paid_string,
            final_profit_string, "\n",
            num_sold_string]

# Print area
print()
for item in to_write:
    print(item)

# create file to hold data (add .txt extension)
file_name = "MMF_data"
write_to = "{}.txt".format(file_name)

text_file = open(write_to, "w+")

# write the item to file
for item in to_write:
    text_file.write(item)
    text_file.write("\n")