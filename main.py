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

'''
0 -> 3
1 -> 3
2 -> 2
3 -> 17
4 -> 3
'''

BOARD = BOARD_4


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
    

def minimumMoves(n, m, x):
    board = Board(n, m, x)
    
    paths = findMostPromisingPaths({"board": board, "moves": []})
    
    if paths["solved"]:
        return paths["paths"]     
    
    paths = paths["paths"]    
    
    while len(paths) > 0:
        
        path = paths.pop(0) # PATH = ( BOARD , [ MOVES ])
        
        mostPromisingPaths = findMostPromisingPaths(path)
        
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