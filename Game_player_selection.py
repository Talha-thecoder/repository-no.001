# Total number of stats.
strenght = ""
speed = ""
agility = ""
genius = ""
mana = ""

# There are 3 Levels to each attribute.
print("Lv.1 (-), Lv.2(+), Lv.3(*).")

human = (
    strenght == "-" and speed == "+" and 
    agility == "-" and genius == "*" and mana == "-"
         )
elf = (
    strenght == "-" and speed == "+" and 
    agility == "-" and genius == "*" and mana == "*"
        )
orc = (
    strenght == "*" and speed == "+" and 
    agility == "-" and genius == "-" and mana == "-"
        )
ogre = (
    strenght == "*" and speed == "-" and 
    agility == "-" and genius == "-" and mana == "-"
        )
goblin = (
    strenght == "-" and speed == "-" and 
    agility == "-" and genius == "-" and mana == "-"
          )

# Recommending species based on the user's input.
s_type = input(
                "What kind of stats would you like " 
              + " (Choose from agility, genius, power, magic and numbers): "
            )

if s_type == "agility" or s_type == "Agility":
    print("We recommend Human, Elf and Goblin types.")
elif s_type == "genius" or s_type == "Genius":
    print("We recommend Human and Elf types.")
elif s_type == "power" or s_type == "Power":
    print("We recommend Orc and Ogre types.")
elif s_type == "magic" or s_type == "Magic":
    print("We recommend Elf types")
elif s_type == "numbers" or s_type == "Numbers":
    print("We recommend Orc and Goblin types")
else:
    print("Species not found.")

# Choosing playable species.
species = input("Enter you desired species: ")
if species == "human" or species == "Human":
     if species == "human" or species == "Human":
      print(
        "your stats are lv.1 strenght, lv.2 speed, lv.1 agility," 
        + "lv.3 genius and lv.2 mana"
    )
     print("You've choosen a Human.")
elif species == "elf" or species == "Elf":
     if species == "elf" or species == "Elf":
      print(
        "your stats are lv.1 strenght, lv.2 speed, lv.2 agility," 
        + "lv.3 genius and lv.3 mana"
    )
     print("You've choosen an Elf.")
elif species == "orc" or species == "Orc":
     if species == "orc" or species == "Orc":
      print(
        "your stats are lv.3 strenght, lv.2 speed, lv.1 agility," 
        + "lv.1 genius and lv.1 mana"
    )
     print("You've choosen an Orc.")
elif species == "ogre" or species == "Ogre":
     if species == "ogre" or species == "Ogre":
      print(
        "your stats are lv.3 strenght, lv.2 speed, lv.1 agility," 
        + "lv.1 genius and lv.1 mana"
    )
     print("You've choosen an Ogre.")
elif species == "goblin" or species == "Goblin":
     if species == "goblin" or species == "Goblin":
      print(
        "your stats are lv.1 strenght, lv.1 speed, lv.1 agility," 
        + "lv.1 genius and lv.1 mana"
    )
     print("You've choosen a Goblin.")
else:
     print("Species doesn't exist. Retry.")
