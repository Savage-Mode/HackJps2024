from flask import Flask, render_template, request, jsonify
import random
import json
import os
from AI import sendMessage
from topics import topics
from leaderboard import getLeaderboard, updateLeaderboard

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/play", methods=["GET", "POST"])
def play():
    if request.method == "POST":
        num_players = int(request.form["num_players"])
        players = []
        for i in range(num_players):
            players.append({"name": f"Player {i+1}", "score": 0})
        topic = random.choice(topics)
        return render_template("play.html", topic=topic, players=players, current_player=0)
    else:
        return "Error: Invalid request method"

@app.route("/submit", methods=["POST"])
def submit():
    if "topic" in request.form and "sentence" in request.form and "players" in request.form and "current_player" in request.form:
        topic = request.form["topic"]
        sentence = request.form["sentence"]
        players = json.loads(request.form["players"])
        current_player = int(request.form["current_player"])
        response = sendMessage(sentence)
        score = int(response["Score"].split("/")[0])
        players[current_player]["score"] += score
        current_player = (current_player + 1) % len(players)
        return jsonify({"response": response["Explanation"], "scores": players, "current_player": current_player})
    else:
        return jsonify({"error": "Topic, sentence, and players are required"}), 400

@app.route("/leaderboard")
def leaderboard():
    leaderboard_data = getLeaderboard()
    ranked_data = [(i+1, x["user"], x["score"]) for i, x in enumerate(leaderboard_data)]
    return render_template("leaderboard.html", leaderboard_data=ranked_data)

if __name__ == "__main__":
    app.run(debug=True)