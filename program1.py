
def ask_Name_Age_Address():
    Name_ = input("what is your name? ") 
    Age_ = int(input("what is your age? ")) 
    Address_ = input("what is your address? ")
    return Name_, Age_, Address_,

def display(NameF, AgeF, AddressF):
    print(f"Hi, my name is {NameF}. I am {AgeF} years old and I live in {AddressF}.")

name, age, address = ask_Name_Age_Address()

display(name, age, address)