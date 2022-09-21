print("naam_van_mijn_list")

# List of games
popular_games =["Player's Unknown Battleground (PUBG) 50 Million 2018",
                "Fortnite Battle Royale 39 Million 2017",
                "Apex Legends 50 Million (1 Month) 2019",
                "League of Legends (LOL) 27 Million 2009",
                "Counter Strike; Global Offensive 32 Million 2014",
                "Hearthstone 29 Million 2012",
                "Minecraft 91 Million 2011",
                "DOTA 2 5 million 2015",
                "The Division 2 N/A 2019",
                "Splatoon 2"]

print(popular_games)
print(f"5] {popular_games[4]}")
print(popular_games)

# b]
dota_game = popular_games[7]
characters_in_name = len(dota_game)
print(f"The game{dota_game} has {characters_in_name} characters.")
print(popular_games)

# c]
number_of_games = len(popular_games)
print(f"Er zitten {number_of_games} games in de lijst.")
print(popular_games)

# d]
popular_games.insert(1, "Snake")
print(popular_games)

# e]
index_of_splatoon = popular_games.index("Splatoon 2")
splatoon = popular_games.pop(index_of_splatoon)
print(f"Helaas heeft de game {splatoon} het niet gered om in de top 10 te blijven. We nemen waardig afscheid van {splatoon}")
print(popular_games)

# f]
index_of_hearthstone = popular_games.index("Hearthstone 29 Million 20120")
popular_games[index_of_hearthstone] = "Hearthstone 29 Million 2012"
print(popular_games)

# Tuple
computer_suppliers = ("Apple",
                      "Asus",
                      "Dell",
                      "Lenovo",
                      "Acer",
                      "Samsung",
                      "MSI",
                      "Hewlett-Packard",
                      "Toshiba",
                      "Microsoft",
                      "Chuwi",
                      "Sony",)
print(computer_suppliers)
print()

# a]
number_of_computer_supplies = len(computer_suppliers)
print (f"De tuple bevat {number_of_computer_supplies} computer leveranciers.")

# b]
computer_supplier = computer_suppliers[7]
characters_in_name = len(computer_supplier)
print(f"De naam van {computer_supplier} bestaat uit {characters_in_name} karakters.")
print(computer_suppliers)
print()

# c]
index_of_computer_suppliers = computer_suppliers.index("Samsung")
print(f"De index van computer leverancier {computer_suppliers[index_of_computer_suppliers]} is {index_of_computer_suppliers}.")
print(computer_suppliers)
print()

# Dictionary

# a]

telephone_numbers = {"The Simpsons": "636-555-3226",
                    "Vegas Vacation": "555-0100",
                    "Ghostbusters": "555-23678",
                    "Billy Madison": "555-0840",
                    "Swingers": "213-555-4679",
                    "Bruce Almighty": "555-0123",
                    "Seinfeld": "555-FILK",
                    "Arrested Development":"555-0113",
                    "Die Hard With a Vengeance": "555-0001",
                    "The A-Team":"555-6162"}
print(telephone_numbers)
print()

print(f"Het telefoonnummer van Bruce Almighty is {telephone_numbers['Bruce Almighty']}.")

# b]
telephone_numbers["Harry Potter"] = "605-475-6961"
print(telephone_numbers)
print()

# c]
old_telephone_number = telephone_numbers["Ghostbusters"]
new_telephone_number = "555-2368"
print(f"Het telefoonnummer{old_telephone_number} is gewijzigd naar {new_telephone_number}.")
print(telephone_numbers)
print()

# d]
phone_number = telephone_numbers.pop("Seinfeld")
print(f"Telefoonnummer {phone_number} van Seinfeld is verwijderd.")
print(telephone_numbers)
print()

# e]
number_of_telephone_numbers = len(telephone_numbers)
print(f"In de dictionary zitten {number_of_telephone_numbers} telefoonnummers.")
print(telephone_numbers)
print()


