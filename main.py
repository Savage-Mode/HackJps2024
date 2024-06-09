from topics import topics
from random import randint
from AI import sendMessage
import json

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
        continue
    elif (sen.count("!")) > 1:
        print("This sentence has too many exclamation marks! You get a 0!")
        plrStats[plrName].append(0)
        continue
    elif (sen.count("?")) > 1:
        print("This sentence has too many question marks! You get a 0!")
        plrStats[plrName].append(0)
        continue
    
    print(plrStats)
    sentenceFinal = "[topic: %s] %s" % (randTopic, sen)
    
    try:
        responseText = sendMessage(sentenceFinal)
        print(responseText)
    except:
        print("oof, the AI's free resources ran out")
        break
    try:
        responseDict = json.loads(responseText)
        print(responseDict)
        score = responseDict["Score"]
        explanation = responseDict["Explanation"]
    except: 
        print("Ai is too lazy to repsond, try another time!")
        plrStats[plrName].append(0)
        continue
    
    print("Reasoning: " + explanation)
    print("Grade: " + str(score) + "%")
    print("")

    plrStats[plrName].append(score)

standingsValues = [plrStats[plrName][0] for plrName in plrStats]
print(standingsValues)
standingsValues = sorted(standingsValues, reverse=True)
standingsNames = ['' for plr in plrStats]
for index in range(len(standingsValues)):
    val = standingsValues[index]
    for plrName in plrStats:
        print(plrName)
        if plrStats[plrName][0] == val and not plrName in standingsNames:
            standingsNames[index] = plrName
            break
print(standingsNames)
print(standingsValues)
print("The Game has ended!")
print("Here are the standings")

for index in range(len(standingsValues)):
    val = standingsValues[index]
    name = standingsNames[index]
    sentenceFinal = "[topic: %s] %s" % (randTopic, sen)
    print()
    print("[%s] %s with a %s percent" % (index + 1, name, val))

# for plrName in plrStats:
#     plrGrade = plrStats[plrName][0]
#     plrGradeStandings

# standings = {}

# for plr in plrStats:
#     plr[]