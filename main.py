from pandas.core.internals.construction import to_arrays

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

#Choose Band
band_chosen = int(input("Which band name do you choose? (1/2/3):"))

#Check band name chose
final_band_name = ""
if band_chosen == 1:
    final_band_name = f"{place_origin} {pet_name} {favorite_food}"
elif band_chosen == 2:
    final_band_name = f"{pet_name} {favorite_food} {place_origin}"
else:
    final_band_name = f"{favorite_food} {place_origin} {pet_name}"

#Start Band Launch Party Packages
print("🎸 Choose your Band Launch Party Packages 🎸")

pick_party_package = input("Choose your package... A, B or C?\n")
pick_pizza_size = input("Choose pizza size... S, M, or L?\n")
add_pepperoni = input("Do you want to add pepperoni? Y or N\n")
add_cheese = input("Do you want to add extra cheese?Y or N\n")
tip = int(input("How much tip would you like to give? (Enter percentage, e.g. 10, 12, 15):"))
people = int(input("How many band members will split the total cost?"))
pizza_count = 0
pizza_price = 0
tip_computation = 0
total_bill = 0
each_person_bill = 0

#Pick what package
if pick_party_package == "A":
    pizza_count += 1
elif pick_party_package == "B":
    pizza_count += 2
elif pick_party_package == "C":
    pizza_count += 3
else:
    pizza_count += 1

#Pick pizza size
if pick_pizza_size == "S":
    pizza_price += 15 * pizza_count
elif pick_pizza_size == "M":
    pizza_price += 20 * pizza_count
else:
    pizza_price += 25 * pizza_count

#Add pepperoni?
if add_pepperoni == "Y":
    if pick_pizza_size == "S":
        pizza_price += pizza_count * 2
    elif pick_pizza_size == "M" or pick_pizza_size == "L":
        pizza_price += pizza_count * 3
    else:
        pizza_price

#Add cheese
if add_cheese == "Y":
    pizza_price += pizza_count * 1

tip_computation = pizza_price * (tip/100)
total_bill = pizza_price + tip_computation

each_person_bill = total_bill/people

#Final Summary
print("----- Final Band Launch Summary -----")
print(f"Band name chosen: ... {final_band_name}")
print(f"Price for one pizza: ${pizza_price/pizza_count: .2f}")
print(f"Pizza total (before tip): ${pizza_price: .2f}")
print(f"Tip amount: ${tip_computation: .2f}")
print(f"Grand total: ${total_bill: .2f}")
print(f"Each band member pays: ${each_person_bill: .2f} or {each_person_bill * 57.58: .2f} in Philippine Peso")
