import pandas
from tabulate import tabulate


def num_check(question, num_type="float", exit_code=None):
    """checks users enter an integer / float that is more than
    zero (or the optional exit code)"""

    if num_type == "float":
        error = "Oops - please enter a number more than 0."

    else:
        error = "Oops - please enter an integer more than 0."

    while True:

        response = input(question)
        # check for exit code and return it if entered
        if response == exit_code:
            return response

        # check datatype is correct and that number
        # is more than zero
        try:
            if num_type == "float":
                response = float(response)
            else:
                response = int(response)

            if response > 0:
                return response
            else:
                print(error)

        except ValueError:
            print(error)


def not_blank(question):
    """Checks that a user response is not blank"""

    while True:
        response = input(question)

        if response != "":
            return response

        print("Sorry, this can't be blank. Please try again. \n")


def get_expenses(exp_type, how_many=1):
    """Gets variable / fixed expenses and outputs
    panda (as a string) and a subtotal of the expenses"""

    # Lists for panda
    all_items = []
    all_amounts = []
    all_dollar_per_item = []

    # Expenses dictionary
    expenses_dict = {
        "Item": all_items,
        "Amount": all_amounts,
        "$ / Item": all_dollar_per_item
    }

    # default for fixed expenses
    amount = how_many  # how_many defaults to 1
    how_much_question = "How much? $"

    # loop to get expenses
    while True:
        item_name = not_blank("Item Name: ")

        if (exp_type == "variable" and
            item_name == "xxx") and len(all_items) == 0:
            print("Oops - you have not entered anything. "
                  "You need at least one item")
        # Check users enter at least one variable expense

            continue

        elif item_name == "xxx":
            break

        # get item amount <enter> defaults to number of+
        # Products being made.
        if exp_type == "Variable":

            amount= num_check(f"How many <enter for {how_many}>: ",
                           "integer","")

            if  amount == "":
                 amount = how_many

            how_much_question = "Price for one? $"

        # Get price for item (question customised depending on expense type)
        price_for_one = num_check(how_much_question,"float")

        all_items.append(item_name)
        all_amounts.append(amount)
        all_dollar_per_item.append(price_for_one)

    # make panda
    expense_frame = pandas.DataFrame(expenses_dict)

    # Calculate Cost Column
    expense_frame['Cost'] =  expense_frame['Amount'] * expense_frame['$ / Item']

    # calculate subtotal
    subtotal = expense_frame['Cost'].sum()

    # Apply currency formatting to currency columns.
    add_dollars = ['Amount', '$ / Item', 'Cost']
    for var_item in add_dollars:
        expense_frame[var_item] = expense_frame[var_item].appy(currency)

    # make expense frames into strings with the desired columns
    if exp_type == "variable":
        expense_string = tabulate(expense_frame, headers='keys',
                                  tablefmt='psql', showindex=False)
    else:
        expense_string = tabulate(expense_frame[['Item', 'Cost']], headers='keys',
                                  tablefmt='psql', showindex=False)

    # return all items for now so we can check loop
    return expense_string, subtotal

# currency formatting function
def currency(x):
    """Formats numbers as currency ($#.##)"""
    return "${:.2f}".format(x)


# Main routine starts here

quantity_made = num_check("Quantity being made: ", "integer")

print()

print("Getting Variable Costs...")
variable_expenses = get_expenses("variable", quantity_made)
print()
variable_panda = variable_expenses[0]
variable_subtotal = variable_expenses[1]

print("Getting Fixed Costs...")
fixed_expenses = get_expenses("fixed")
print()
fixed_panda = variable_expenses[0]
fixed_subtotal = variable_expenses[1]



# Temporary output area (for easy testing)

print("=== Variable Expenses ===")
print(variable_panda)
print(f"Variable subtotal: ${variable_subtotal:.2f}")
print()

print("=== Fixed Expenses ===")
print(fixed_panda)
print(f"Fixed Subtotal: ${fixed_subtotal:.2f}")

print()
total_expenses = variable_subtotal + fixed_subtotal
print(f"Total Expenses: ${total_expenses:.2f}")
