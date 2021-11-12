import math

def ask_apple_orange():
    APPLE = int(input("How many apples do you want to buy? "))
    ORANGE = int(input("How many oranges do you want to buy? "))
    return APPLE, ORANGE

def display(apple, orange):
    NumberOfApple_X_ApplePrice= apple*20
    print(f"₱20 X {apple} = ₱{NumberOfApple_X_ApplePrice}")
    NumberOfOrange_X_OrangePrice= orange*25
    print(f"₱25 X {orange} = ₱{NumberOfOrange_X_OrangePrice}")
    
    total_amount = NumberOfApple_X_ApplePrice + NumberOfOrange_X_OrangePrice
    print(f"The total amount is ₱{total_amount}.")

apple_, orange_ = ask_apple_orange()

display(apple_, orange_)