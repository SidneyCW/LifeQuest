import requests
import json

def chess_elo_getter(player_username):
    url = f"https://api.chess.com/pub/player/{player_username}/stats"

    try:
        response = requests.get(url)
        response.raise_for_status()  # Raises an HTTPError if the HTTP request returned an unsuccessful status code
        
        data = response.json()
        elo = data.get('chess_rapid', {}).get('last', {}).get('rating')
        
        if elo is not None:
            return elo
        else:
            print(f"Error: Unable to retrieve chess rating for {player_username}")
            return None
    
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None
    except json.JSONDecodeError as e:
        print(f"Error: Unable to decode JSON response - {e}")
        return None
    
print(chess_elo_getter('SleepySidney'))