import re

import pandas as pd
import json
import numpy as np
import uuid
import os
import glob


# This is the uuid for all lineup name spaces
GLOBAL_UUID = uuid.UUID("7b246383-caa5-400c-aded-befb7843c447")



# team map is a dictionary of lineups for a given team
# the key of team map in a hash of a given lineup. Each value is an object with features

# list of players is the input
def generateLineupUUID(players_list):
    sorted_player_list = sorted(players_list)
    lineupString = ''.join(map(str, sorted_player_list))
    return uuid.uuid3(GLOBAL_UUID, lineupString)


def buildFilePath(game_directory, team):
    print (game_directory + f'/*{team}')
    return game_directory + f'/*{team}'

def getUniqueLineups(game_directory, team):
    # Iterate through file and only add games which were games of the specified team
    lineupMap = dict()
    # files = [f for f in os.listdir(game_directory) if re.match(rf'({team})+', f)]
    files = [f for f in os.listdir(game_directory) if f.endswith('.json')]
    for filePath in files:
        absoluteFilePath = game_directory + '/' + filePath
        with open(absoluteFilePath) as json_file:
            json_data = json.load(json_file)

            for i in range(len(json_data['periods'])):
                period = json_data['periods'][i]
                for j in range(len(period['events'])):
                    event = json_data['periods'][i]['events'][j]
                    # Get lineup on lineup change and store that in map
                    if (event['event_type'] == 'lineupchange'):
                        home_players = event['on_court']['home']['players']
                        away_players = event['on_court']['away']['players']
                        home_players_list = []
                        away_players_list = []

                        for player in home_players:
                            home_players_list.append(player['full_name'])
                        for player in away_players:
                            away_players_list.append(player['full_name'])

                        home_lineup_uuid = str(generateLineupUUID(home_players_list))
                        away_lineup_uuid = str(generateLineupUUID(away_players_list))

                        if (home_lineup_uuid not in lineupMap):
                            lineupMap[home_lineup_uuid] = home_players_list
                        if (away_lineup_uuid not in lineupMap):
                            lineupMap[away_lineup_uuid] = away_players_list
    with open(f'C:/Users/ghock/workplace/NBA_game-data_2018/nba/lineupUUIDS/all_lineups_2018.json', 'w') as fp:
        json.dump(lineupMap, fp, indent=2)

team = "GSW"
getUniqueLineups('C:/Users/ghock/workplace/NBA_game-data_2018/nba/pbp_data', team)
print(generateLineupUUID(['tat', 'asf']))
print(generateLineupUUID(['asf','tat']))

