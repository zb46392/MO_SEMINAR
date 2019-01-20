# -*- coding: utf-8 -*-
"""
@author: Zdravko Baničević

Python 3.4
"""
from board import Board
from time import time

BOARD_0 = {"n": 3, "m": 3, "x": ["bwe","web","ebw"]}
BOARD_1 = {"n": 3, "m": 3, "x": ["bwe","wbw","ewb"]}
BOARD_2 = {"n": 4, "m": 4, "x": ["beww","beww","beww","wewe"]}
BOARD_3 = {"n": 20, "m": 20, "x": ["bwbwbwbwbwbwbwbwbwbw","wbwbwbwbwbwbwbwbwbwb","bwbwbwbwbwbwbwbwbwbw","wbwbwbwbwbwbwbwbwbwb","bwbwbwbwbwbwbwbwbwbw","wbwbwbwbwbwbwbwbwbwb","bwbwbwbwewbwbwbwbwbw","wbwbwbwbebwbwbwbwbwb","bwbwbwbwewbwbwbwbwbw","wbwbwbwbebwbwbwbwbwb","bwbwbwbwewbwbwbwbwbw","wbwbwbwbebwbwbwbwbwb","bwbwbwbwewbwbwbwbwbw","wbwbwbwbebwbwbwbwbwb","bwbwbwbwewbwbwbwbwbw","wbwbwbwbwbwbwbwbwbwb","bwbwbwbwbwbwbwbwbwbw","wbwbwbwbwbwbwbwbwbwb","bwbwbwbwbwbwbwbwbwbw","wbwbwbwbwbwbwbwbwbwe"]}
BOARD_4 = {"n": 2, "m": 8, "x": ["ewewbbbb","bwebewww"]}
BOARD_5 = {"n": 12, "m": 6, "x": ["bewbbe", "eebwbw", "eeebwe", "bbeeww", "eebbee", "bbwbww", "wwbwww", "eeewwe", "ebwebe", "eewewe", "eweeeb", "eeebwe"]}
BOARD_6 = {"n": 9, "m": 6, "x": ["ewbbww", "bbbbee", "weeeee", "bbeebe", "eewbwe", "weebee", "ewbeww", "wwwwbe", "bbewee"]}
BOARD_7 = {"n": 2, "m": 6, "x": ["wbebbb", "ebbebe"]}
BOARD_8 = {"n":12, "m":11, "x": ["eebbeebbwwb", "ewwwebbbwww", "bbbewebwbbb", "ebewweebeee", "ewbwbbewbbw", "wbeeebwbeee", "weewewewbbw", "ebwbbbeeeew", "webwebeewwb", "bbwweebbebe", "eebbbwebwbw", "beebbebwbbb"]}
BOARD_9 = {"n": 2, "m": 15, "x": ["ebbeeeeweeebbeb", "eewwbbbbbebbbwb"]}
BOARD_10 = {"n":16, "m": 16, "x": ["wwbeeewewwebwwwe", "bwbebebbwweweebe", "wwwbeebeebewbeew", "beeeeebwweweewbe", "wwwbebeweewbeeee", "webebbebeebewbbb", "bwewbwewbwbewebe", "ebbbbewbwewebbwb", "bweebwwebbewebwb", "ebewewebbwwbeebb", "wbebeewwebwbebwe", "eeewbewbweebebwb", "bwweebebbwbeebew", "bebbewbebbwwweew", "ebewbbwbwbeewbwb", "ewebbbwebewwbbbb"]}
BOARD_11 = {"n":14, "m": 17, "x": ["ebbebebewebbwwbwe", "wbeewbwwebewbebeb", "weweeewwwwewbwweb", "wbewbbbwbeeeewewe", "bbewwebwbeebbbbew", "webeeeeweeeebeewb", "eebwbwbbbewbbeebe", "webeeebeebewbbwee", "wbebwbeewwbwebbbb", "eebwwewwwwbwweewb", "ebweeebeewewbbbwb", "wwebweeweebwbbebw", "eeebwbwewweewbebb", "wewweewwbbweebewe"]}
BOARD_12 = {"n": 14, "m":17, "x":["ebbebebewebbwwbwe", "wbeewbwwebewbebeb", "weweeewwwwewbwweb", "wbewbbbwbeeeewewe", "bbewwebwbeebbbbew", "webeeeeweeeebeewb", "eebwbwbbbewbbeebe", "webeeebeebewbbwee", "wbebwbeewwbwebbbb", "eebwwewwwwbwweewb", "ebweeebeewewbbbwb", "wwebweeweebwbbebw", "eeebwbwewweewbebb", "wewweewwbbweebewe"]}
BOARD_X = {"n":20,"m":20,"x":["bwbwbwbwbwbwbwbwbwbw","wwwwbbbbwwwwbbbbwwbb","bwbwbwbwbwbwbwbwbwbw","wwwwbbbbwwwwbbbbwwbb","bwbwbwbwbwbwbwbwbwbw","wwwwbbbbwwwwbbbbwwbb","bwbwbwbwbwbwbwbwbwbw","wwwwbbbbwwwwbbbbwwbb","bwbwbwbwbwbwbwbwbwbw","wwwwbbbbwwwwbbbbwwbb","bwbwbwbwbwbwbwbwbwbw","wwwwbbbbweewbbbbwwbb","bwbwbwbwbwbwbwbwbwbw","wwwwbbbbwwwwbbbbwwbb","bwbwbwbwbwbwbwbwbwbw","wwwwbbbbwwwwbbbbwwbb","bwbwbwbwbwbwbwbwbwbw","wwwwbbbbwwwwbbbbwwbb","bwbwbwbwbwbwbwbwbwbw", "wwwwbbbbwwwwbbbbwwbb"]}

'''
0 -> 3
1 -> 3
2 -> 2
3 -> 17
4 -> 3
5 -> 3 ! 5
6 -> 3
7 -> 2
8 -> 3
9 -> 2
10 -> 3
11 -> 3
12 -> 2 ? 3
X -> 6 ! 5
'''

BOARD = BOARD_12


def findMostPromisingPaths(path):
    
    nbrOfSections = len(path["board"].splitBoardIntoSections())
    mostPromisingPaths = []
    
    for nextState in path["board"].getNextStates():
        if nextState["board"].isSolved():
            path["moves"].append(nextState["moves"])
            return {"solved" : True, "paths" : path["moves"]}
            
        if len(nextState["board"].splitBoardIntoSections()) < nbrOfSections:
            nbrOfSections = len(nextState["board"].splitBoardIntoSections())
            mostPromisingPaths = []
            
            newPath = [move for move in path["moves"]]
            newPath.append(nextState["moves"])
            
            mostPromisingPaths.append({"board": nextState["board"], "moves": newPath})
        '''    
        elif len(nextState["board"].splitBoardIntoSections()) == nbrOfSections:
            newPath = [move for move in path["moves"]]
            newPath.append(nextState["moves"])
            
            mostPromisingPaths.append({"board": nextState["board"], "moves": newPath})
        '''            
            
    return {"solved": False, "paths": mostPromisingPaths}
    
def findNextPaths(path):
    paths = []
    
    for nextState in path["board"].getNextStates():
        if nextState["board"].isSolved():
            path["moves"].append(nextState["moves"])
            return {"solved" : True, "paths" : path["moves"]}
            
        newPath = [move for move in path["moves"]]
        newPath.append(nextState["moves"])
        
        paths.append({"board": nextState["board"], "moves": newPath})
        
    return {"solved": False, "paths": paths}
    
def minimumMoves(n, m, x):
    board = Board(n, m, x)
    
    #paths = findMostPromisingPaths({"board": board, "moves": []})
    paths = findNextPaths({"board": board, "moves": []})
    
    if paths["solved"]:
        return paths["paths"]     
    
    paths = paths["paths"]    
    
    while len(paths) > 0:
        
        path = paths.pop(0) # PATH = ( BOARD , [ MOVES ])
        
        mostPromisingPaths = findMostPromisingPaths(path)
        #mostPromisingPaths = findNextPaths(path)
        
        if mostPromisingPaths["solved"]:
            return mostPromisingPaths["paths"]
            
        paths += mostPromisingPaths["paths"]
        

def main():
    start = time()
    mm = minimumMoves(BOARD["n"], BOARD["m"], BOARD["x"])
    stop = time()
    
    print(str(len(mm)) + " : " + str(mm))
    print(stop - start)

if __name__ == "__main__":
    main()