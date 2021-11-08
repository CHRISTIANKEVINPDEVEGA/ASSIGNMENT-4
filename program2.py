import math

def ask_apple_orange():
    apple = int(input("How many apples do you want to buy? "))
    NumberOfApple_X_ApplePrice= apple*20
    print(f"₱20 X {apple} = ₱{NumberOfApple_X_ApplePrice}")

    orange = int(input("How many oranges do you want to buy? "))
    NumberOfOrange_X_OrangePrice= orange*25
    print(f"₱25 X {orange} = ₱{NumberOfOrange_X_OrangePrice}")
    
    total_amount = NumberOfApple_X_ApplePrice + NumberOfOrange_X_OrangePrice
    return total_amount

def display(total_amount):
    print(f"The total amount is ₱{total_amount}.")

total_AMOUNT_ = ask_apple_orange()

display(total_AMOUNT_)