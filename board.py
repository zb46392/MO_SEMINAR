from random import randint

class Board():
    MIN = 2
    MAX = 20
    
    def __init__(self, width = None, height = None, state = []):
        self.width = width
        self.height = height
        self.state = state
        self.specialTurn = True
        
    def flipTile(self, x, y, color):
        if self.state[x][y] == "w":
            splitRow = list(self.state[x])
            splitRow[y] = "b"
            self.state[x] = "".join(splitRow)
        elif self.state[x][y] == "b":
            splitRow = list(self.state[x])
            splitRow[y] = "w"
            self.state[x] = "".join(splitRow)
            
        for tile in self.findAdjecentTilesWithSameColor(x, y, color):
            self.flipTile(tile["x"], tile["y"], tile["color"])
        
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
        return Board(self.width, self.height, self.state)
        
    def generateRandomBoard(self):
        self.width = randint(Board.MIN, Board.MAX+1)
        self.height = randint(Board.MIN, Board.MAX+1)
        self.state = []
        
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
                
            

    def __str__(self):
        bStr = "X: " + str(self.width) + ", Y:" + str(self.height) + "\n"
        
        for row in self.state:
            bStr += str(row) + "\n"
            
        return bStr

if __name__ == "__main__":
    b = Board()
    
    b.generateRandomBoard()
    
    print(b)
    