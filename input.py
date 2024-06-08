from topics import topics
from random import randint

print("""

█░█░█ █▀▀ █░░ █▀▀ █▀█ █▀▄▀█ █▀▀   ▀█▀ █▀█   ▀█▀ █░█ █▀▀   █▀ █▀▀ █▄░█ ▀█▀ █▀▀ █▄░█ █▀▀ █▀▀   █▀▀ ▄▀█ █▀▄▀█ █▀▀
▀▄▀▄▀ ██▄ █▄▄ █▄▄ █▄█ █░▀░█ ██▄   ░█░ █▄█   ░█░ █▀█ ██▄   ▄█ ██▄ █░▀█ ░█░ ██▄ █░▀█ █▄▄ ██▄   █▄█ █▀█ █░▀░█ ██▄
""")

plrs = input("How many players will be playing: " )
plrStats = {}

while not type(plrs) == int:
    if plrs.isnumeric():
        plrs = int(plrs)
        break
    else:
        print("Please type a valid number!")
        plrs = input("How many players will be playing: " )

for index in range(plrs):
    index = str(index + 1)
    plrFirstName = input("Enter Player " + index + " first name: ")
    plrLastName = input("Enter Player " + index + " last name: ")
    print("")
    
    # Account for same first and last name
    c = 0
    plrKey = plrFirstName + "_" + plrLastName

    while plrKey in plrStats:
        c += 1
        plrKey = plrFirstName + "_" + plrLastName + str(c)

    plrStats[plrKey] = []

print(plrStats)

topicLen = len(topics)