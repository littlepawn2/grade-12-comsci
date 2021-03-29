from Ship import Ship

class Board:
    
    boardSizeX = 10 #has to be >= 6
    boardSizeY = 10 #has to be >= 6
    squareSize = 50 #graphical problems when below about 15
    
    def __init__(self, x, y):
        self.x = x #position of corner of board
        self.y = y
        self.ships = []
        self.grid = [[False for i in range(Board.boardSizeX)] for i in range(Board.boardSizeY)]
        
    def getSizeX(self):
        return Board.boardSizeX
    
    def getSizeY(self):
        return Board.boardSizeY
    
    def getSquSize(self):
        return Board.squareSize
        
    def addShip(self, ship):
        #adds a ship to the board
        self.ships.append(ship)
        
    def shipCollision(self, passedShip):
        #checks one ship against the rest
        for ship in self.ships:
            if not ship.moving:
                for pnt in ship.occupiedSquares:
                    if pnt in passedShip.occupiedSquares:
                        return True
        return False
    
    def createRandomBoard(self):
        #generates a random board of ships
        self.ships = []
        self.ships.append(Ship.generateRandomShip(6, self))
        self.ships.append(Ship.generateRandomShip(5, self))
        self.ships.append(Ship.generateRandomShip(4, self))
        self.ships.append(Ship.generateRandomShip(3, self))
        self.ships.append(Ship.generateRandomShip(2, self))

        
    def drawBoard(self):
        #draws grid
        for i in range(Board.boardSizeX):
            for j in range(Board.boardSizeY):
                fill(100, 100, 255)
                square(i*Board.squareSize+self.x, j*Board.squareSize+self.y, Board.squareSize)
                
    def drawHits(self):
        #draws hit markers
        for i in range(Board.boardSizeX):
            for j in range(Board.boardSizeY):
                if self.grid[i][j] == True:
                    for ship in self.ships:
                        if ship.isPointOnShip(i, j):
                            fill(255, 0, 0)
                            break
                        else:
                            fill(255)
                        
                    circle(i*Board.squareSize+self.x+Board.squareSize/2, j*Board.squareSize+self.y+Board.squareSize/2, Board.squareSize/2)
    
    def isSquareOnBoard(self, x, y):
        if x >= 0 and x <= Board.boardSizeX - 1 and y >= 0 and y <= Board.boardSizeY - 1:
            return True
        return False
                    
    def drawShips(self):
        #draws ships on board
        for ship in self.ships:
            ship.drawShip(self)
            
    #for player ship placement -----------------------
        
    def mouseClickedCheck(self):
        #activates fns in ship
        clickX = (mouseX-self.x) // Board.squareSize
        clickY = (mouseY-self.y) // Board.squareSize
        click = [clickX, clickY]
        
        for ship in self.ships:
            if click in ship.occupiedSquares:
                ship.switchMoving()
                
    def mouseReleasedCheck(self):
        #activates fns in ship
        for ship in self.ships:
            if ship.moving:
                ship.placeShip(self)
                ship.switchMoving()
                
    #for game -------------------------------------
    
    def clickToFire(self, message):
        #calls fire based on mouse position
        clickX = (mouseX-self.x) // Board.squareSize
        clickY = (mouseY-self.y) // Board.squareSize
        return self.fire(clickX, clickY, message)
    
    def fire(self, clickX, clickY, message):
        #most game logic here
        #returns True if valid move, False otherwise
        if not self.isSquareOnBoard(clickX, clickY):
            return False
        if self.grid[clickX][clickY] == True:
            return False
        else:
            self.grid[clickX][clickY] = True
            for ship in self.ships:
                ship.hit(clickX, clickY, message)
            
        return True
    
    def checkLoss(self):
        #checks for a loss
        for ship in self.ships:
            if not ship.isSunk():
                return False
        return True
        
        

                
        
        