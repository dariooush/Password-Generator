import random

# Items in Password ==========
uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUWXYZ"
lowercase_letters = uppercase_letters.lower()
digits = "0123456789"
symbols = "!@#$%&*/-"

# Checking which Items be in Password ==========
upper, lower, nums, syms = True, True, True, True

all = ""

if upper:
    all += uppercase_letters
if lower:
    all += lowercase_letters
if nums:
    all += digits
if syms:
    all += symbols

# # Length and Amount by User Choice ==========
length = int(input("What length would you like your password be? "))
amount = int(input("How many password would you like? "))


# Length and Amount of Generated Password ==========
# length = 8
# amount = 5


for x in range(amount):
    password = "".join(random.sample(all, length))
    print(password)