import math

def all_calculations():
   _amount_money = float(input("Enter the amount of money you have: ₱"))
   _apple_price = float(input("How much will you pay for an apple? ₱"))
   return _amount_money, _apple_price

def display(amount_money, apple_price):
   apple_stock = 10
   Calculation= amount_money - (apple_stock * apple_price)
   print(f"You can buy {apple_stock} apples and your change is ₱{Calculation:.2f}.") 

AMOUNT_MONEY, APPLE_PRICE = all_calculations()

display(AMOUNT_MONEY, APPLE_PRICE)