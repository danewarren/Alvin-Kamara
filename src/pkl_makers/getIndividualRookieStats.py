#!/usr/bin/env python
'''
Dane Warren

Creates a dictionary containing the statlines of the rookie seasons of the submitted running backs. Playoff games included.
'''
import cPickle as pickle
import json

'''
Given the rbs dictionary and a name, returns the ID of the name.
@param rbs: Dictionary of IDs and RB names
@param name: String of player's name
@return: The player's ID
'''
def getID(rbs, name):
    return rbs[name]

'''
Resets running back data
'''
def resetData():
    data = {}
    data["gamesPlayed"] = 0
    data["rushing_attempts"] = 0
    data["rushing_yards"] = 0
    data["rushing_touchdowns"] = 0
    data["receiving_targets"] = 0
    data["receiving_receptions"] = 0
    data["receiving_yards"] = 0
    data["receiving_touchdowns"] = 0
    return data

'''
Obtains the rookie year stat line for the given player
@param gameStats: The individual game stats for every game going back to 1950
@param ID: The player's ID
@returns: A dictionary of the players' rookie year stat line
'''
def getRookieStats(gameStats, ID):
    data = {}
    data["gamesPlayed"] = 0
    data["rushing_attempts"] = 0
    data["rushing_yards"] = 0
    data["rushing_touchdowns"] = 0
    data["receiving_targets"] = 0
    data["receiving_receptions"] = 0
    data["receiving_yards"] = 0
    data["receiving_touchdowns"] = 0
    year = 2500
    for game in gameStats[0]:
        if game.get("player_id") == ID:
            if year > int(game.get("year")):
                data = resetData()
                year = int(game.get("year"))
            if year == int(game.get("year")):
                print(game)
                data["gamesPlayed"] += 1
                data["rushing_attempts"] += game.get("rushing_attempts")
                data["rushing_yards"] += game.get("rushing_yards")
                data["rushing_touchdowns"] += game.get("rushing_touchdowns")
                data["receiving_targets"] += game.get("receiving_targets")
                data["receiving_receptions"] += game.get("receiving_receptions")
                data["receiving_yards"] += game.get("receiving_yards")
                data["receiving_touchdowns"] += game.get("receiving_touchdowns")
    if data["rushing_attempts"] == 0:
        data["rushYpA"] = 0
        data["rushTDpA"] = 0
    else:
        data["rushYpA"] = float(data["rushing_yards"]) / float(data["rushing_attempts"])
        data["rushTDpA"] = float(data["rushing_touchdowns"]) / float(data["rushing_attempts"])
    if data["receiving_receptions"] == 0:
        data["airYpR"] = 0
        data["airTDpR"] = 0
    else:
        data["airYpR"] = float(data["receiving_yards"]) / float(data["receiving_receptions"])
        data["airTDpR"] = float(data["receiving_touchdowns"]) / float(data["receiving_receptions"])
    if data["gamesPlayed"] == 0:
        data["rushYpG"] = 0
        data["rushTDpG"] = 0
        data["airYpG"] = 0
        data["airTDpG"] = 0
    else:
        data["airYpG"] = float(data["receiving_yards"]) / float(data["gamesPlayed"])
        data["airTDpG"] = float(data["receiving_touchdowns"]) / float(data["gamesPlayed"])
        data["rushYpG"] = float(data["rushing_yards"]) / float(data["gamesPlayed"])
        data["rushTDpG"] = float(data["rushing_touchdowns"]) / float(data["gamesPlayed"])
    return data

def main():
    gameStats = [json.loads(line) for line in open('../../datasets/json_datasets/games.json')]
    file = open("../../datasets/pkl_datasets/rbs.pkl","rb")
    rbs = pickle.load(file)
    file.close()
    
    #rb is name, rbs[rb] is ID
    data = {}
    rbData = []
    data = getRookieStats(gameStats, 23099)
    data["ID"] = 23099
    rbData.append(data)

    '''
    file = open("../../datasets/pkl_datasets/rookie_rbStats.pkl","wb")
    pickle.dump(rbData, file)
    file.close()
    '''
    print(rbData)

if __name__ == "__main__":
    main()
