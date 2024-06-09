import json
import os

def getLeaderboard():
    leaderboard_data = []
    if os.path.exists("leaderboard.json"):
        with open("leaderboard.json", "r") as f:
            leaderboard_data = json.load(f)
    else:
        with open("leaderboard.json", "w") as f:
            json.dump([], f)
    return leaderboard_data

def updateLeaderboard(user, score):
    leaderboard_data = getLeaderboard()
    leaderboard_data.append({"user": user, "score": score})
    leaderboard_data.sort(key=lambda x: x["score"], reverse=True)
    with open("leaderboard.json", "w") as f:
        json.dump(leaderboard_data, f)