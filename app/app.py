from flask import Flask, jsonify, render_template
import socket
import os

app = Flask(__name__)

# In-memory vote store (resets on restart — we'll add persistence later)
votes = {
    "Mumbai Indians": 0,
    "Chennai Super Kings": 0,
    "Royal Challengers Bengaluru": 0,
    "Kolkata Knight Riders": 0,
    "Delhi Capitals": 0,
    "Rajasthan Royals": 0,
    "Sunrisers Hyderabad": 0,
    "Punjab Kings": 0,
    "Lucknow Super Giants": 0,
    "Gujarat Titans": 0
}

@app.route("/")
def home():
    return jsonify({
        "app": "IPL Team Voter",
        "pod": socket.gethostname(),
        "version": os.getenv("APP_VERSION", "1.0.0"),
        "total_votes": sum(votes.values()),
        "teams": list(votes.keys())
    })

@app.route("/vote/<team_name>", methods=["POST"])
def vote(team_name):
    matched = next((t for t in votes if t.lower().replace(" ", "-") == team_name.lower()), None)
    if not matched:
        return jsonify({"error": f"Team '{team_name}' not found", "valid_teams": list(votes.keys())}), 404
    votes[matched] += 1
    return jsonify({"message": f"Vote cast for {matched}!", "total_votes_for_team": votes[matched]}), 200

@app.route("/ui")
def ui():
    return render_template("index.html")

@app.route("/results")
def results():
    sorted_teams = sorted(votes.items(), key=lambda x: x[1], reverse=True)
    winner = sorted_teams[0][0] if sorted_teams[0][1] > 0 else "No votes yet!"
    return jsonify({
        "winner": winner,
        "leaderboard": [{"team": t, "votes": v} for t, v in sorted_teams]
    })

@app.route("/health")
def health():
    return jsonify({"status": "ok"}), 200

@app.route("/ready")
def ready():
    return jsonify({"status": "ready"}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)