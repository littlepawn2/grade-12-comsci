from Board import Board
from Computer import Computer
from Interface import Messager
from Interface import Button
from Interface import Menu
from Scoreboard import Scoreboard
from PlayerInfo import PlayerInfo
from Interface import Keyboard

gameState = 0 #0-menu, 1-ship placement, 2-play
playerBoard = Board(550, 0)
computerBoard = Board(0, 0)
computer = Computer(playerBoard)
player = PlayerInfo()

turn = True #True-player, False-comp
menuState = None

turnMessager = Messager(200, 550)
sinkMessager = Messager(450, 50)
bottomRightButton = Button(500, 510, 200, 80)

menu = Menu(710, 510, 330, 80, [Button(710, 510, 100, 80, "?"), Button(810, 510, 130, 80, "Scores"), Button(940, 510, 100, 80, "Exit")])

scoreboard = Scoreboard()

name = ""

def reset():
    global gameState, playerBoard, computerBoard, turn, computer, turnMessager, sinkMessager, bottomRightButton, scoreboard, player, menu, menuState
    playerBoard = Board(550, 0)
    computerBoard = Board(0, 0)
    computer = Computer(playerBoard)
    playerBoard.createRandomBoard()
    computerBoard.createRandomBoard()
    
    bottomRightButton.setMessage("Ready")
    turnMessager.setMessage("Place your ships")
    sinkMessager.setMessage("")
    turn = True
    player.score = 0
    
    gameState = 1

def setup():
    global playerBoard, computerBoard
    size(1050, 600)
    textAlign(CENTER, CENTER)
    
    #generate boards
    playerBoard.createRandomBoard()
    computerBoard.createRandomBoard()
    
    #scoreboard.clearScores() #######TEMPORARY
    
    
    
    
def draw():
    #no logic in here, only graphics
    global gameState, playerBoard, computerBoard, turnMessager, sinkMessager, bottomRightButton, scoreboard, player, menu, menuState
    background(0)
    

    if gameState == -1:
        #menu was clicked
        menu.drawMenu()
        if menuState[1] == 0:
            #help
            pass
        elif menuState[1] == 1:
            #scores
            scoreboard.displayScores(300, 0)
            text("Your High Score:", 850, 50)
            text(str(scoreboard.findScore(player)), 850, 100)
    
    if gameState == 0:
        #add some title picture
        
        
        #display player name
        fill(255)
        textSize(40)
        text("Enter your name:", 350, 400)
        textAlign(BASELINE, CENTER)
        player.displayName(550, 400)
        textAlign(CENTER, CENTER)
        
        #say something like press annywhere to begin
        
        #menu
        menu.drawMenu()
        
        
    elif gameState == 1:
        #draw boards
        playerBoard.drawBoard()
        playerBoard.drawShips()
        
        computerBoard.drawBoard()
        #computerBoard.drawShips()
        
        #draw message
        turnMessager.printMessage(40)
        
        #draw button
        bottomRightButton.drawButton()
        menu.drawMenu()
        
    elif gameState == 2:
        #draw boards
        playerBoard.drawBoard()
        playerBoard.drawShips()
        playerBoard.drawHits()
        
        computerBoard.drawBoard()
        computerBoard.drawShips()
        computerBoard.drawHits()
        
        #draw any messages
        turnMessager.printMessage(40)
        sinkMessager.printMessage(40)
        
        #draw button
        bottomRightButton.drawButton()
        menu.drawMenu()
        
        
def keyPressed():
    global gameState, player
    if gameState == 0:
        #player should enter name in the menu
        player.name = Keyboard.keyIn(player.name)
        

def mousePressed():
    global gameState, playerBoard, computerBoard
    
    if gameState == 1:
        playerBoard.mouseClickedCheck()

def mouseReleased():
    #most logic should go in here
    global gameState, playerBoard, computerBoard, turn, computer, turnMessager, sinkMessager, bottomRightButton, scoreboard, player, menu, menuState
    if menu.click() != None:
        if gameState == -1:
            if menuState[1] == menu.click():
                gameState = menuState[0]
            else:
                menuState[1] = menu.click()
        else:
            menuState = [gameState, menu.click()]
            gameState = -1
        
    if gameState == -1:
        if menuState[1] == 0:
            #help
            pass
        elif menuState[1] == 1:
            #scores
            pass
        elif menuState[1] == 2:
            exit()
    
    elif gameState == 0 and menu.click() == None:
        #set buttons message to "Ready" before going to gameState = 1
        bottomRightButton.setMessage("Ready")
        turnMessager.setMessage("Place your ships")
        gameState = 1
        
    elif gameState == 1:
        if bottomRightButton.isClicked(): #button takes priority
            bottomRightButton.setMessage("Reset")
            turnMessager.setMessage("Player's Turn")
            gameState = 2
        else:
            #player places pieces
            playerBoard.mouseReleasedCheck()
        
        
    elif gameState == 2:
        if bottomRightButton.isClicked():
            reset()
        if not computerBoard.checkLoss() or playerBoard.checkLoss():
            if turn:
                #player clicks for their turn
                sinkMessager.setMessage("")
                if computerBoard.clickToFire(sinkMessager):
                    player.score += 1
                    turnMessager.setMessage("Computer's Turn")
                    
                    if computerBoard.checkLoss():
                        turnMessager.setMessage("Player Wins")
                        #update scoreboard
                        scoreboard.addScore(player)
                        scoreboard.updateFile()
                        
                    turn = not(turn)
                    
            else:
                #player clicks anywhere to pass AI's turn
                computer.makeMove()
                
                turnMessager.setMessage("Player's Turn")
                
                if playerBoard.checkLoss():
                    turnMessager.setMessage("Computer Wins")
                    
                turn = not(turn)

        
        
    
    
    
    
    
    
    
    
    
    
    
    
    
