#!/usr/bin/env python
'''
Dane Warren

Compare Alvin Kamara's historic first NFL season to all other RBs
'''
import cPickle as pickle

'''
@returns: Alvin Kamara's rookie season stats as a dictionary
'''
def getKamaraStats():
    data = {}
    data["gamesPlayed"] = 16
    data["rushing_attempts"] = 120
    data["rushing_yards"] = 728
    data["rushing_touchdowns"] = 8
    data["receiving_receptions"] = 81
    data["receiving_yards"] = 826
    data["receiving_touchdowns"] = 5
    data["rushYpA"] = float(data["rushing_yards"]) / float(data["rushing_attempts"])
    data["rushYpG"] = float(data["rushing_yards"]) / float(data["gamesPlayed"])
    data["rushTDpG"] = float(data["rushing_touchdowns"]) / float(data["gamesPlayed"])
    data["rushTDpA"] = float(data["rushing_touchdowns"]) / float(data["rushing_attempts"])
    data["airYpG"] = float(data["receiving_yards"]) / float(data["gamesPlayed"])
    data["airYpR"] = float(data["receiving_yards"]) / float(data["receiving_receptions"])
    data["airTDpG"] = float(data["receiving_touchdowns"]) / float(data["gamesPlayed"])
    data["airTDpR"] = float(data["receiving_touchdowns"]) / float(data["receiving_receptions"])
    return data

'''
@param x: Number to compare to y
@param y: Number to compare to x
@returns: The similarity of the two numbers
'''
def similarityScore(x, y):
    if x < y:
        similarity = float(x) / float(y)
    else:
        similarity = float(y) / float(x)
    return similarity

'''
@param rbStats: The stats of every rookie running back since 1950
@param kamaraStats: Alvin Kamara's rookie season stats
@returns: The similarity rating of this RB and Kamara
'''
def getSimilarity(rb, kamaraStats):
    similarity = 0

    if rb["gamesPlayed"] >= 8:

        rushYpASim = similarityScore(rb["rushYpA"], kamaraStats["rushYpA"])
        rushYpGSim = similarityScore(rb["rushYpG"], kamaraStats["rushYpG"])
        rushTDpGSim = similarityScore(rb["rushTDpG"], kamaraStats["rushTDpG"])
        rushTDpASim = similarityScore(rb["rushTDpA"], kamaraStats["rushTDpA"])
        airYpGSim = similarityScore(rb["airYpG"], kamaraStats["airYpG"])
        airYpRSim = similarityScore(rb["airYpR"], kamaraStats["airYpR"])
        airTDpGSim = similarityScore(rb["airTDpG"], kamaraStats["airTDpG"])
        airTDpRSim = similarityScore(rb["airTDpR"], kamaraStats["airTDpR"])
        similarity = .125 * (rushYpASim + rushYpGSim + rushTDpGSim + rushTDpASim + airYpGSim + airYpRSim + airTDpGSim + airTDpRSim)

    if rb["ID"] == 11877:
        similarity = 0

    return similarity

'''
@param k: The number of neighbors to return
@param rbStats: The stats of every rookie running back since 1950
@param kamaraStats: Alvin Kamara's rookie season stats
@returns: A dictionary containing the k nearest neighbors to Kamara, as well as their similarity ratings
'''
def kamaraKNN(k, rbStats, kamaraStats):
    nearestNeighbors = {}
    for rb in rbStats:
        similarity = getSimilarity(rb, kamaraStats)
        if len(nearestNeighbors) < 5:
            nearestNeighbors[rb["ID"]] = similarity
        else:
            sortedNums = sorted(nearestNeighbors.values())
            if(similarity > sortedNums[0]):
                sortedNames = sorted(nearestNeighbors, key=nearestNeighbors.get)
                del nearestNeighbors[sortedNames[0]]
                nearestNeighbors[rb["ID"]] = similarity
    return nearestNeighbors

def main():
    file = open("../../datasets/pkl_datasets/rookie_rbStats.pkl","rb")
    rbStats = pickle.load(file)
    file.close()

    kamaraStats = getKamaraStats()
    nearestNeighbors = {}
    nearestNeighbors = kamaraKNN(5, rbStats, kamaraStats)
    print(nearestNeighbors)
    file = open("../../datasets/pkl_datasets/kamaraKNN.pkl", "wb")
    pickle.dump(nearestNeighbors, file)
    file.close()

if __name__ == "__main__":
    main()
