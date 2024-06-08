from topics import topics
from random import randint

#How does the game work: 
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

# Select random topic
topicLen = len(topics)
randTopic = topics[randint(0, topicLen - 1)]

for plrName in plrStats:
    print("It is " + plrName + "'s turn\n")
    sen = input("Write a sentence on the topic of " + randTopic + ": ")
    if sen.count(".") > 1:
        print("This sentence has too many periods! You get a 0!")
        plrStats[plrName].append(0)
    elif (sen.count("!")) > 1:
        print("This sentence has too many exclamation marks! You get a 0!")
        plrStats[plrName].append(0)
    elif (sen.count("?")) > 1:
        print("This sentence has too many question marks! You get a 0!")
        plrStats[plrName].append(0)
    print(plrStats)
