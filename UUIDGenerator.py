import pandas as pd
import json
import numpy as np
import uuid

# team map is a dictionary of lineups for a given team
# the key of team map in a hash of a given lineup. Each value is an object with features
teamMap = dict()

# list of players is the input
def generateLineupUUID(team_uuid, players_list):
    lineupString = ''.join(map(str, players_list))
    return uuid.uuid3(team_uuid, lineupString)

# function takes a filepath of the game file
def getUniqueLineups(filePath):
    with open(filePath) as json_file:
        json_data = json.load(json_file)
        for i in range(len(json_data['periods'])):
            period = json_data['periods'][i]
            for j in range(len(period['events'])):
                event = json_data['periods'][i]['events'][j]


getUniqueLineups('C:/Users/ghock/Desktop/nba_data/ATL-BKN-2019-03-10.json')
test_uuid = uuid.uuid4()
print (generateLineupUUID(test_uuid, ['tat', 'asf']))


