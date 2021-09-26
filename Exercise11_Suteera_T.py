"""Exercise 11 พิรามิด"""

# input = 5
# ----*
# ---***
# --*****
# -*******
# *********

userNumber = int(input("Please enter your number: "))
for x in range(userNumber):
    print(" " * (userNumber-(x+1)), "*" * (1+2*x))
