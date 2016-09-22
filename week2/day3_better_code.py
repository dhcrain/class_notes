# Inventory Tracker RPG


def add_item_to_inventory(player):
    item_name = input("What is the item name? ")
    item_quantity = int(input("How many? "))
    if item_name in player["inventory"].keys():
        # UPDATING QUANTITY OF EXISTING ITEM
        player["inventory"][item_name]["quantity"] += item_quantity
    else:
        # ADDING BRAND NEW ITEM TO INVENTORY w/ QUANTITY
        player["inventory"][item_name] = {"quantity": item_quantity}


def inspect_inventory(player):
    for item in player["inventory"].keys():
        quantity = player["inventory"][item]["quantity"]
        print("{} - {}".format(item, quantity))


def player_input(player, choice):
    if choice == 'a':
        add_item_to_inventory(player)
    elif choice == 'i':
        inspect_inventory(player)


def make_character():
    player = {"inventory": {"red potion": {"quantity": 20}}}
    player_name = input("Welcome Traveler! What is your name? ")
    player["name"] = player_name
    return player

####################################

player = make_character()

while True:
    choice = input("Would you like to (i)nspect your inventory? or (a)dd to your inventory?\n>")
    player_input(player, choice)















