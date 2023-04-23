import requests
import json

player_username = 'sleepysidney'
def chess_elo_getter(player_username):
    url = f"https://api.chess.com/pub/player/{player_username}/stats"

    response = requests.get(url)

    if response.status_code == 200:
        data = json.loads(response.content)
        elo = data['chess_rapid']['last']['rating']
        return elo
    
    else:
        print(f"Error: {response.status_code} - {response.content}")
        return None
