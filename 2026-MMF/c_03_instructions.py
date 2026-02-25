# Functions go here
def make_statement(statement, decoration):...



def string_check(question, valid_answers=('yes', 'no'),
                 num_letters=1):...


def instructions():...
make_statement("instructions", "🍿")

print('''
    
For each ticket holder enter ...
- Their name
- Their age
- The payment method (cash / credit)
 
The program will record the ticket sale and calculate the 
ticket cost (and the profit).
 
Once you have either sold all of the tickets or entered the 
exit code ('xxx'), the program will display the ticket
sales information and write the data to a text file.
 
It will also choose one lucky ticker holder who wins the draw (their ticket is free).''')


# Main routine goes here

make_statement("mini-Movie Fundraiser Program", "🍕")

print()
want_instructions = string_check("Do you want to see the instructions?")

if want_instructions == "yes":
    instructions()

print()
print("program continues...")
















