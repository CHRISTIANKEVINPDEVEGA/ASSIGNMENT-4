import math

def all_calculations():
   amount_money = float(input("Enter the amount of money you have: ₱"))
   apple_price = float(input("How much will you pay for an apple? ₱"))
   apple_stock = 10
   Calculation= amount_money - (apple_stock * apple_price)
   return Calculation


def display(calculation_):
   print(f"You can buy 10 apples and your change is ₱{calculation_:.2f}.") 

Calculation_ = all_calculations()

display(Calculation_)