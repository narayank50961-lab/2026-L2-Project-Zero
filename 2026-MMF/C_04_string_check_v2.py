# Functions go here
def string_check(question,valid_answers=('yes','no'),
                  num_letters=1):
 """check that users enter the full word
 or the 'n'  letter of a word from a list of valid responses"""
 while  True:

      response = input(question). lower()

      for item in valid_answers:

       # check if the response is the entire word
        if response == item:
          return item

        # check if it's the first letter
        elif response == item[:num_letters]:
          return item

      print(f"Please choose an option from {valid_answers}")

# Main routine goes here

payment_list = ['cash','credit']

want_instructions  = string_check("Do you want to see the interactions? " )
print(f"you chose {want_instructions}")
pay_method =string_check("payment method:", payment_list, 2)
print(f"you chose {pay_method}")