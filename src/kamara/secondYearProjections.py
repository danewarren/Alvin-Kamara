#!/usr/bin/env python
'''
Dane Warren

Based on the players closest to Alvin Kamara, 
determine second year projections for Kamara
based on their second years.
'''

def getMarcusAllen():
    stats = {} 
    stats["name"] = "Marcus Allen"
    stats["games"] = 16
    stats["rushYards"] = 1014
    stats["rushTDs"] = 9
    stats["airYards"] = 590
    stats["airTDs"] = 2
    stats["receptions"] = 68
    stats["fantasyPoints"] = float((stats["rushYards"]+stats["airYards"]))/10 + (stats["rushTDs"]+stats["airTDs"])*6 + stats["receptions"]
    stats["fantasyPointsPerGame"] = stats["fantasyPoints"] / stats["games"]
    return stats

def getKelvinBryant():
    stats = {}
    stats["name"] = "Kelvin Bryant"
    stats["games"] = 11
    stats["rushYards"] = 406
    stats["rushTDs"] = 1
    stats["airYards"] = 490
    stats["airTDs"] = 5
    stats["receptions"] = 43
    stats["fantasyPoints"] = float((stats["rushYards"]+stats["airYards"]))/10 + (stats["rushTDs"]+stats["airTDs"])*6 + stats["receptions"]
    stats["fantasyPointsPerGame"] = stats["fantasyPoints"] / stats["games"]
    return stats

def getDavidJohnson():
    stats = {}
    stats["name"] = "David Johnson"
    stats["games"] = 16
    stats["rushYards"] = 1239
    stats["rushTDs"] = 16
    stats["airYards"] = 879
    stats["airTDs"] = 4
    stats["receptions"] = 80
    stats["fantasyPoints"] = float((stats["rushYards"]+stats["airYards"]))/10 + (stats["rushTDs"]+stats["airTDs"])*6 + stats["receptions"]
    stats["fantasyPointsPerGame"] = stats["fantasyPoints"] / stats["games"]
    return stats

def getRogerCraig():
    stats = {}
    stats["name"] = "Roger Craig"
    stats["games"] = 16
    stats["rushYards"] = 649
    stats["rushTDs"] = 7
    stats["airYards"] = 675
    stats["airTDs"] = 3
    stats["receptions"] = 71
    stats["fantasyPoints"] = float((stats["rushYards"]+stats["airYards"]))/10 + (stats["rushTDs"]+stats["airTDs"])*6 + stats["receptions"]
    stats["fantasyPointsPerGame"] = stats["fantasyPoints"] / stats["games"]
    return stats

def getHerschelWalker():
    stats = {}
    stats["name"] = "Herschel Walker"
    stats["games"] = 12
    stats["rushYards"] = 891
    stats["rushTDs"] = 7
    stats["airYards"] = 715
    stats["airTDs"] = 1
    stats["receptions"] = 60
    stats["fantasyPoints"] = float((stats["rushYards"]+stats["airYards"]))/10 + (stats["rushTDs"]+stats["airTDs"])*6 + stats["receptions"]
    stats["fantasyPointsPerGame"] = stats["fantasyPoints"] / stats["games"]
    return stats


def main():
    marcusAllen = getMarcusAllen()
    print(marcusAllen)
    
    kelvinBryant = getKelvinBryant()
    print(kelvinBryant)

    davidJohnson = getDavidJohnson()
    print(davidJohnson)

    rogerCraig = getRogerCraig()
    print(rogerCraig)

    herschelWalker = getHerschelWalker()
    print(herschelWalker)

    neighbors = []
    neighbors.append(marcusAllen)
    neighbors.append(kelvinBryant)
    neighbors.append(davidJohnson)
    neighbors.append(rogerCraig)
    neighbors.append(herschelWalker)
    
    gamesTotal = 0
    fantasyTotal = 0
    for neighbor in neighbors:
        gamesTotal += neighbor["games"]
        fantasyTotal += neighbor["fantasyPoints"]
    kamara = {}
    kamara["name"] = "Alvin Kamara"
    kamara["fantasyProjectionPerGame"] = fantasyTotal / gamesTotal
    kamara["fantasyProjection"] = kamara["fantasyProjectionPerGame"] * 16
    
    print(kamara)

if __name__ == "__main__":
    main()
