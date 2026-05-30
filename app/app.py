from flask import Flask, jsonify, render_template
from prometheus_flask_exporter import PrometheusMetrics
import sqlite3
import os
import socket

app = Flask(__name__)
metrics = PrometheusMetrics(app)

DB_PATH = os.getenv("DB_PATH", "votes.db")

TEAMS = [
    "Mumbai Indians",
    "Chennai Super Kings",
    "Royal Challengers Bengaluru",
    "Kolkata Knight Riders",
    "Delhi Capitals",
    "Rajasthan Royals",
    "Sunrisers Hyderabad",
    "Punjab Kings",
    "Lucknow Super Giants",
    "Gujarat Titans"
]

def init_db():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS votes (
            team TEXT PRIMARY KEY,
            count INTEGER DEFAULT 0
        )
    ''')
    for team in TEAMS:
        c.execute("INSERT OR IGNORE INTO votes (team, count) VALUES (?, 0)", (team,))
    conn.commit()
    conn.close()

def get_votes():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("SELECT team, count FROM votes ORDER BY count DESC")
    rows = c.fetchall()
    conn.close()
    return {row[0]: row[1] for row in rows}

def increment_vote(team_name):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("UPDATE votes SET count = count + 1 WHERE team = ?", (team_name,))
    conn.commit()
    conn.close()

init_db()

@app.route("/")
def home():
    votes = get_votes()
    return jsonify({
        "app": "IPL Team Voter",
        "pod": socket.gethostname(),
        "version": os.getenv("APP_VERSION", "1.0.0"),
        "total_votes": sum(votes.values()),
        "teams": list(votes.keys())
    })

@app.route("/vote/<team_name>", methods=["POST"])
def vote(team_name):
    votes = get_votes()
    matched = next((t for t in votes if t.lower().replace(" ", "-") == team_name.lower()), None)
    if not matched:
        return jsonify({"error": f"Team '{team_name}' not found", "valid_teams": list(votes.keys())}), 404
    increment_vote(matched)
    updated = get_votes()
    return jsonify({"message": f"Vote cast for {matched}!", "total_votes_for_team": updated[matched]}), 200

@app.route("/results")
def results():
    votes = get_votes()
    sorted_teams = sorted(votes.items(), key=lambda x: x[1], reverse=True)
    winner = sorted_teams[0][0] if sorted_teams[0][1] > 0 else "No votes yet!"
    return jsonify({
        "winner": winner,
        "leaderboard": [{"team": t, "votes": v} for t, v in sorted_teams]
    })

@app.route("/ui")
def ui():
    return render_template("index.html")

@app.route("/health")
def health():
    return jsonify({"status": "ok"}), 200

@app.route("/ready")
def ready():
    return jsonify({"status": "ready"}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)