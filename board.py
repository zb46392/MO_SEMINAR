# -*- coding: utf-8 -*-
"""
@author: Zdravko Baničević

Python 3.4
"""

from random import randint

class Board():
    MIN = 2
    MAX = 20
    
    def __init__(self, height = None, width = None, state = None, isSpecialTurn = None):
        self.width = width
        self.height = height
        if state is None:
            self.state = []
        else:            
            self.state = state
            
        if isSpecialTurn is None:
            self.isSpecialTurn = True
        else:
            self.isSpecialTurn = isSpecialTurn
        
    def flipTile(self, x, y, color):
        if self.state[x][y] == "w" and color == "w":
            splitRow = self.rowToLst(self.state[x])
            splitRow[y] = "b"
            self.state[x] = self.lstToRow(splitRow)
        elif self.state[x][y] == "b" and color == "b":
            splitRow = self.rowToLst(self.state[x])
            splitRow[y] = "w"
            self.state[x] = self.lstToRow(splitRow)
            
        for tile in self.findAdjecentTilesWithSameColor(x, y, color):
            self.flipTile(tile["x"], tile["y"], tile["color"])
    
    def rowToLst(self, row):
        return list(row)
        
    def lstToRow(self, lst):
        return "".join(lst)
        
    def findAdjecentTilesWithSameColor(self, x, y, color):
        tiles = []
        if x > 0 and self.state[x-1][y] == color: #                 GORE
            tiles.append(self.createTile(x-1, y, color))
        if x < self.height - 1 and self.state[x+1][y] == color: #   DOLE
            tiles.append(self.createTile(x+1, y, color))
        if y > 0 and self.state[x][y-1] == color: #                 LIVO
            tiles.append(self.createTile(x, y-1, color))
        if y < self.width - 1 and self.state[x][y+1] == color: #    DESNO
            tiles.append(self.createTile(x, y+1, color))
            
        return tiles
            
    def createTile(self, x, y, color):
            tile = {}
            tile["x"] = x
            tile["y"] = y
            tile["color"] = color
            
            return tile
            
    def returnCopy(self):
        return Board(self.height, self.width, [state for state in self.state], self.isSpecialTurn)
        
    def generateRandomBoard(self):
        self.width = randint(Board.MIN, Board.MAX+1)
        self.height = randint(Board.MIN, Board.MAX+1)
        self.state = []
        self.isSpecialTurn = True
        
        boardLst = []
        
        for i in range(self.width * self.height):
            rnd = randint(0, 99)
            
            if rnd > 69:
                boardLst.append("w")
            elif rnd > 19 and rnd < 70:
                boardLst.append("b")
            else:
                boardLst.append("e")
                
        if "e" not in boardLst:
            boardLst[randint(0, len(boardLst))] = "e"
        if "b" not in boardLst:
            boardLst[randint(0, len(boardLst))] = "b"
        if "w" not in boardLst:
            boardLst[randint(0, len(boardLst))] = "w"
            
        for i in range(self.height):
            self.state.append("".join(boardLst[i*self.width:i*self.width+self.width]))
                
    def splitBoardIntoSections(self):
        sections = []
        allTiles = self.getTiles()
        while len(allTiles) > 0:
            section = {}
            
            for sTile in self.findSectionTiles(list(allTiles.values())[0]):
                section[(sTile["x"], sTile["y"])] = allTiles.pop((sTile["x"], sTile["y"]))
                
            sections.append(section)
                
        return sections
                
        
    def getTiles(self):
        tiles = {}
        
        for x in range(self.height):
            for y in range(self.width):
                tiles[(x, y)] = self.createTile(x, y, self.state[x][y])
        
        return tiles
                
    def findSectionTiles(self, tile):
        tiles = [tile]
        sectionTiles = [tile]
        
        while len(tiles) > 0:
            sTile = tiles.pop(0)
            
            for tile in self.findAdjecentTilesWithSameColor(sTile["x"], sTile["y"], sTile["color"]):
                if tile not in sectionTiles:
                    tiles.append(tile)
                    sectionTiles.append(tile)
            
        return sectionTiles
            
    def fillEmptyCells(self, color):
        for i in range(len(self.state)):
            nRow = ""
            for cell in self.rowToLst(self.state[i]):
                if cell == "e":
                    nRow += color
                else:
                    nRow += cell
                    
            self.state[i] = nRow
            
    def makeSpecialTurn(self, color):
        self.fillEmptyCells(color)
        self.isSpecialTurn = False
            
    def getNextStates(self):
        nextStates = []
        
        if self.isSpecialTurn:
            tmpBoard = self.returnCopy()
            tmpBoard.makeSpecialTurn("b")
            
            nextStates.append({"board": tmpBoard.returnCopy(), "moves" : "b"})
            
            tmpBoard = self.returnCopy()
            tmpBoard.makeSpecialTurn("w")
            
            nextStates.append({"board": tmpBoard.returnCopy(), "moves" : "w"})
            
        else:
            for section in self.splitBoardIntoSections():
                
                tmpBoard = self.returnCopy()
                tmpTile = section[list(section.keys())[0]]
                
                tmpBoard.flipTile(tmpTile["x"], tmpTile["y"], tmpTile["color"])
                
                nextStates.append({"board": tmpBoard.returnCopy(), "moves" : (tmpTile["x"], tmpTile["y"])})
                
        return nextStates
            
            
    def isSolved(self):
        color = self.state[0][0]
        
        for row in self.state:
            for cell in self.rowToLst(row):
                if color != cell:
                    return False
                    
        return True
           
    def __str__(self):
        bStr = "N: " + str(self.width) + ", M:" + str(self.height) + "\n"
        
        for row in self.state:
            bStr += str(row) + "\n"
            
        return bStr