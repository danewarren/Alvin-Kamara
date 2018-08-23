#!/usr/bin/env python
'''
Dane Warren

Creates a dictionary of the rookie season statlines of every running back since 1950
'''
import cPickle as pickle
import json

'''
@param players: JSON dataset of all NFL players since 1950
@returns: A dictionary containing all running backs and their respective IDs
'''
def getRunningBacks(players):
    nameID = {}
    for player in players[0]:
        if player.get("position") == "RB":
            nameID[player.get("name")] = player.get("player_id")
    print(nameID)
    return nameID

def main():
    players = [json.loads(line) for line in open('../../datasets/json_datasets/profiles.json')]
    rbs = getRunningBacks(players)
    file = open("../../datasets/pkl_datasets/rbs.pkl","wb")
    pickle.dump(rbs, file)
    file.close()

if __name__ == "__main__":
    main()
