import requests
from prettyconf import config

AUTH_TOKEN = config('FOOTBALL_AUTH_TOKEN',
                    default='d201d60ea0a14340a865aee9e3a6350c')

url = "https://api.football-data.org/v4/matches"

headers = {'X-Auth-Token': AUTH_TOKEN}
response = requests.get(url, headers=headers).json()
matches = response['matches']
for match in matches:
    print(f"{match['homeTeam']['name']} - {match['awayTeam']['name']}")
