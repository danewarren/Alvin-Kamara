#!/usr/bin/env python
'''
Dane Warren

Creates a dictionary of every running back since 1950 and their IDs.
player[ID] = name
'''
import cPickle as pickle
import json

'''
@param players: JSON dataset of all NFL players since 1950
@returns: A dictionary containing all running backs and their respective IDs
'''
def getRunningBacks(players):
    IDname = {}
    for player in players[0]:
        if player.get("position") == "RB":
            IDname[player.get("player_id")] = player.get("name")
    print(IDname)
    return IDname

def main():
    players = [json.loads(line) for line in open('../../datasets/json_datasets/profiles.json')]
    rbs = getRunningBacks(players)
    file = open("../../datasets/pkl_datasets/id_to_name.pkl","wb")
    pickle.dump(rbs, file)
    file.close()

if __name__ == "__main__":
    main()
