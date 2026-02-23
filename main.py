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