import random

player = {
    "name": "Hana",
    "level": 1,
    "exp": 0,
    "health": 100,
    "max_health": 100,
    "damage": 10
}

enemies = [
    {
        "name": "Goblin",
        "level": 1,
        "exp": 50,
        "health": 60,
        "damage": 5
    },

    {
        "name": "Snake",
        "level": 1,
        "exp": 50,
        "health": 50,
        "damage": 7
    },

    {
        "name": "Rat",
        "level": 1,
        "exp": 50,
        "health": 40,
        "damage": 6
    },

    {
        "name": "Orc",
        "level": 2,
        "exp": 100,
        "health": 80,
        "damage": 15
    }

]

boss = {
    "name": "Goose",
    "level": 5,
    "exp": 500,
    "health": 300,
    "damage": 30
}


inventory = {
            "Potion": 2, 
            "Gold" : 100
            }

def attack(attacker, target):
    target["health"] -= attacker["damage"]

    print(attacker["name"] + " attacks " + target["name"] + "!")
    print(target["name"] + " has " + str(target["health"]) + " health remaining.")


def heal(player, inventory):
    if "Potion" in inventory and inventory["Potion"] > 0:

        player["health"] += 25
        
        if player["health"] > player["max_health"]:
            player["health"] = player["max_health"]

        inventory["Potion"] -= 1

        print(player["name"] + " uses a Potion and heals 25 health!")
        print(player["name"] + " now has " + str(player["health"]) + " health.")

    else:
        print(player["name"] + " has no Potions left!")

def gain_exp(player, exp):

    player["exp"] += exp

    print(player["name"] + " gains " + str(exp) + " experience points!")

    if player["exp"] >= 100:
        level_up(player)

def level_up(player):
    player["level"] += 1
    player["exp"] = 0

    player["max_health"] += 10 * player["level"]
    player["health"] = player["max_health"]

    player["damage"] += 5

    print(player["name"] + " leveled up to level " + str(player["level"]) + "!")
    print("Health increased to " + str(player["health"]) + " and damage increased to " + str(player["damage"]) + ".")


while player["health"] > 0:

    enemy = random.choice(enemies).copy()

    print("\nA wild " + enemy["name"] + " appears!")

    while player["health"] > 0 and enemy["health"] > 0:

        print("\nWhat will you do?")
        print("1. Attack")
        print("2. Heal")
        print("3. Show inventory")

        choice = input("Choose an action: ")

        if choice == "1":
            attack(player, enemy)

        elif choice == "2":
            heal(player, inventory)

        elif choice == "3":
            print("Inventory:", inventory)

        else:
            print("Invalid choice. Please try again.")

        if enemy["health"] > 0:
            attack(enemy, player)

        if player["health"] <= 0:
            print("\n" + player["name"] + " has been defeated! Game Over.")

        elif enemy["health"] <= 0:
            print("\n" + enemy["name"] + " has been defeated! You win!")

            gain_exp(player, enemy["exp"])

            if player["level"] == 10:
                print("A boss appears! It's " + boss["name"] + "!")

                boss = boss.copy()

                while boss["health"] > 0 and player["health"] > 0:

                    print("\nWhat will you do?")
                    print("1. Attack")
                    print("2. Heal")
                    print("3. Show inventory")

                    choice = input("Choose an action: ")

                    if choice == "1":
                        attack(player, boss)

                    elif choice == "2":
                        heal(player, inventory)

                    elif choice == "3":
                        print("Inventory:", inventory)

                    else:
                        print("Invalid choice. Please try again.")

                    if boss["health"] > 0:
                        attack(boss, player)

                if boss["health"] <= 0:
                    print("\n" + boss["name"] + " has been defeated! You win the game!")
                    exit()

                else:
                    print("\n" + player["name"] + " has been defeated by the boss! Game Over.")
                    exit()
                
                break
                

            loot = random.choice(["Gold", "Gold", "Gold", "Potion", "Nothing"])
            
            print("You found a " + loot + " on the " + enemy["name"] + "!")

            if loot != "Nothing":
                
                if loot in inventory:
                    inventory[loot] += 1

                else:
                    inventory[loot] = 1

            print("Inventory:", inventory)
