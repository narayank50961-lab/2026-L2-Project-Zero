import pandas
from tabulate import tabulate
from datetime import date
import math

def make_statement(statement, decoration):
    """Emphasises heading by adding decoration
    at the start and end"""

    return f"{decoration * 3} {statement} {decoration * 3}"

# Functions go here
def string_check(question, valid_ans_list, num_letters):
 """check that users enter the fill word or the first
  letter of a word from a list of valid responses"""
 while  True:

      response = input(question). lower()

      for item in valid_ans_list:
        if response == item:
          return item
        # check if it's the first letter
        elif response == item[0]:
          return item

      print(f"Please choose an option from {valid_ans_list}")

def yes_no_check(question):
    """Checks that users enter yes / y or no/ n to a question"""

    while True:
        response = input(question).lower()

        if response == "yes" or response == "y":
            return "yes"
        elif response == "no" or response == "n":
            return "no"
        else:
            print("Please enter yes (y) or no (n) . \n")

def instructions():
    print(make_statement("instructions", "🍿"))

    print(''' 

For each ticket holder enter ...
- How many questions
- Get coordinates

The program will allow usesrs to  (and the profit)

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

def round_up(amount, round_val):
    """Rounds amount to desired hole number"""
    return int(math.ceil(amount / round_val)) * round_val

# Heading

# Ask user if they want instructions

# How many questions / infinite mode

# Start loop here!

# Ask what they need to find?

# Ask for coordinates

# Do the calculation and output the answer