__author__ = 'Eugene'

import random


def random_select(input_list: list, no_of_choices: int=1) -> list:
    output_list = []
    main_list = input_list.copy()
    for i in range(no_of_choices):
        output_list.append(main_list.pop(random.randint(0, len(main_list) - 1)))

    return output_list

character_abilities = []
purpose = ""
character_health = 0
character_mana = 0
health_to_mana = ""
character_class = ""

# Get character creation parameters
while True:
    try:
        purpose = ["attack", "balanced", "support"].index(
            input("Select main character purpose: attack/balanced/support ").lower()
        )

        purpose = ["attack", "balanced", "support"][purpose]

    except ValueError:
        print("Invalid selection, please try again.")
        continue

    break

while True:
    try:
        health_to_mana = ["health", "mana"].index(
            input("More health or mana? health/mana: ").lower()
        )

        health_to_mana = ["health", "mana"][health_to_mana]

    except ValueError:
        print("Invalid selection, please try again.")
        continue

    break

# Generate character stats
genders = ["Male", "Female", "Oddity", "Monster"]
character_gender = random.choice(genders)

# classes = ["Combatant", "Mage", "Healer", "Assassin", "Tank"] Unused
combatant_abilities = ["Spear", "Lunge", "Backhand", "Slice", "Damage boost", "Charge!", "Auto-Flank"]
mage_abilities = ["Freeze", "Trap", "Disarm", "Fireball", "Lightning", "Shockwave", "Mana Steal"]
healer_abilities = ["Overheal", "Shield", "Poison", "Sandvich", "Retreat Assist", "Insta-health"]
assassin_abilities = ["Dodge", "Decoy", "Invisibility", "Kidnap", "Teleport", "Blind", "Encircle"]
tank_abilities = ["Stomp", "Engulf", "Carrier", "Damage Transfer", "Slingshot", "Demolish", "Barrel-roll"]
ability_checksum = []

if health_to_mana is "health":
    if purpose is "attack":
        character_class = "Combatant"
        character_health = random.randint(500, 600)
        character_mana = 1000 - character_health
        character_abilities = random_select(combatant_abilities, 4)
        ability_checksum = [combatant_abilities.index(ability) for ability in character_abilities]

    if purpose is "balanced":
        character_class = "Tank"
        character_health = random.randint(700, 800)
        character_mana = 1000 - character_health
        character_abilities = random_select(tank_abilities, 4)
        ability_checksum = [tank_abilities.index(ability) for ability in character_abilities]

    if purpose is "support":
        character_class = "Tank"
        character_health = random.randint(800, 900)
        character_mana = 1000 - character_health
        character_abilities = [random.choice(tank_abilities) for i in range(4)]
        ability_checksum = [tank_abilities.index(ability) for ability in character_abilities]

else:
    if purpose is "attack":
        character_class = "Mage"
        character_health = random.randint(400, 500)
        character_mana = 1000 - character_health
        character_abilities = random_select(mage_abilities, 4)
        ability_checksum = [mage_abilities.index(ability) for ability in character_abilities]

    if purpose is "balanced":
        character_class = "Assassin"
        character_health = random.randint(300, 400)
        character_mana = random.randint(400, 450)
        character_abilities = random_select(assassin_abilities, 4)
        ability_checksum = [assassin_abilities.index(ability) for ability in character_abilities]

    if purpose is "support":
        character_class = "Healer"
        character_health = random.randint(300, 400)
        character_mana = random.randint(450, 500)
        character_abilities = random_select(healer_abilities, 4)
        ability_checksum = [healer_abilities.index(ability) for ability in character_abilities]

# Name Generation
# This is indeed a random name generator. Whether it's a MYSTICAL name generator is up to the user.
# I gave up trying to think of good name parts a long time ago. It's too hard.
# Instead, please do enjoy the random anime (Japanese animation), osu! (rhythm game) references and in-jokes.
# Most of all, please don't take this name generator seriously.
name_part1 = ["Arx", "Xi", "Bek", "Sha", "HoChi", "Ayy", "Hitagi", "Submarine", "KimitoNatsufes",
              "Toshino", "AiLaLa", "Eren", "Mikasa", "Akari", "Funami", "Shinobu", "Mashiro", "Nanami"]
name_part2 = ["bane", "crest", "-senpai", "-sensei", "-san", "-chan", "lmao", "Minh", "Senjougahara",
              "Spitfire", "rekt", "Kyoko", "Ackerman", "Jaeger", "IsBestGirl", "Oshino", "Yui"]

character_name = "".join([random.choice(name_part1), random.choice(name_part2)])

# Print out generated stats

print("Class: " + character_class)
print("Name: " + character_name)
print("Gender: " + character_gender)
print("Health: " + str(character_health))
print("Mana: " + str(character_mana))
print("Abilities: ")
for ability in character_abilities:
    print("\t" + ability)

# Save file
ability_checksum = [str(number) for number in ability_checksum]
ability_checksum = "_".join(ability_checksum)
filename = "_".join([character_class, character_name, character_gender, str(character_health), str(character_mana),
                     ability_checksum, ".txt"])
with open(filename, "w") as f:
    f.write("Class: " + character_class + "\n")
    f.write("Name: " + character_name + "\n")
    f.write("Gender: " + character_gender + "\n")
    f.write("Health: " + str(character_health) + "\n")
    f.write("Mana: " + str(character_mana) + "\n")
    f.write("Abilities: \n")
    for ability in character_abilities:
        f.write("    " + ability + "\n")
    f.flush()
