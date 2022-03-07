"""A Magic 8 Ball Oracle of Truth About the Future"""

from random import randint

input("Ask a yes or no question: ")

response: int = randint(0,3)

if response == 0:
    print("Yes, definitely!")
elif response == 1:
        print("Looking hopeful.")
elif response == 2:
    print("Ask again later.")
elif response == 3:
    print("No way. Not a chance.")

# Can also use elif rather than if and else statements.
