#!/usr/bin/env python
'''
Dane Warren

Takes in running back the nearest neighbors as IDs and scores and outputs the nearest neighbors with names and scores.
'''
import cPickle as pickle

def getNames(kamaraKNN, rbs):
    nameScore = {}
    for ID in kamaraKNN.keys():
        nameScore[rbs[ID]] = kamaraKNN[ID]
    return nameScore

def main():
    file = open("../../datasets/pkl_datasets/kamaraKNN.pkl","rb")
    kamaraKNN = pickle.load(file)
    file.close()
    
    file = open("../../datasets/pkl_datasets/id_to_name.pkl","rb")
    rbs = pickle.load(file)
    file.close()

    nameScore = getNames(kamaraKNN, rbs)
    print(nameScore)

if __name__ == "__main__":
    main()
