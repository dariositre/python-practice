print("Welcome to Band Name Generator Project!")
user_name = input("What's your name?\n")
print("Hello " + user_name + "!")
place_origin = input("What city are you from " + user_name + "?\n")
pet_name = input("What's your pet name?\n")
favorite_food = input("What's your favorite food?\n")
print("Generating your legendary band name...")
print("   =============\n"
      "Band Name Generator\n"
      "   =============\n")
print("1. " + place_origin + " " + pet_name + " " + favorite_food + '\n'
      "2. " + pet_name + " " + favorite_food + " " + place_origin + '\n'
      "3. " + favorite_food + " " + place_origin + " " + pet_name + '\n')

bill_amount = float(input("What is the total bill amount? $\n"))
tip_amount = int(input("What percentage tip would you like to give? %\n"))
people = int(input("How many people are splitting the bill?\n"))

tip_computation = bill_amount * (tip_amount/100)
bill_amount += tip_computation
people_each_pay = bill_amount/people
total_bill_conversion = bill_amount * 57.76
each_bill_conversion = people_each_pay * 57.76

print("Calculating your bill....")
print(f"Your total bill is {bill_amount: .2f}$ or {total_bill_conversion:.2f} in Philippine Peso")
print(f"Each person should pay: {people_each_pay:.2f}$ or {each_bill_conversion:.2f} in Philippine Peso")