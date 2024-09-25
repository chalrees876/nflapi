from flask import Flask, jsonify, request

app = Flask(__name__)

players = [
    {"id": 1, "name": "Tom Brady", "team": "Tampa Bay Buccaneers", "position": "QB"},
    {"id": 2, "name": "Patrick Mahomes", "team": "Kansas City Chiefs", "position": "QB"},
    {"id": 3, "name": "Aaron Donald", "team": "Los Angeles Rams", "position": "DE"},
    {"id": 4, "name": "Derrick Henry", "team": "Tennessee Titans", "position": "RB"}
]

@app.route('/players', methods=['GET'])
def get_players():
    return jsonify(players)

@app.route('/players/<int:id>', methods=['GET'])
def get_player(id):
    for p in players:
        if p['id'] == id:
            return jsonify(p)
    return None

@app.route('/players', methods=['POST'])
def add_player():
    new_player = request.get_json()
    if new_player and 'name' in new_player and 'team' in new_player and 'position' in new_player:
        new_player["id"] = len(players) + 1
        players.append(new_player)
        return jsonify(new_player), 201
    else:
        return jsonify({"error": "Invalid data"}), 400
    
@app.route('/players/<int:id>', methods=['PUT'])
def update_player(id):
    player = next((p for p in players if p["id"] == id), None)
    if player:
        data = request.json
        player.update(data)
        return jsonify(player)
    
@app.route('/players/<int:id>', methods=['DELETE'])
def delete_player(id):
    player = next((p for p in players if p["id"] == id), None)
    if player:
        players.remove(player)
        return players, 201

if __name__ == '__main__':
    app.run(debug=True)