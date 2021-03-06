import pickle

class Scoreboard:
    
    def __init__(self):
        #opens scores file
        try:
            file = open("scores.pickle", "rb")
        except IOError:
            #creates blank file if not found
            print("scores not found, new scores file created")
            file = open("scores.pickle", "wb")
            pickle.dump({}, file)
            file.close()
            file = open("scores.pickle", "rb")
        finally:    
            self.scores = pickle.load(file) #dict of names w/scores
            file.close()
            
        self.start = 0
        self.scoreList = quickSort(1, self.toList())
            
    def clearScores(self):
        #clears the scores file
        self.scores = {}
        
        file = open("scores.pickle", "wb")
        pickle.dump({}, file)
        file.close()
        
    def toList(self):
        #converts score dict to a list
        outList = []
        for name in self.scores:
            outList.append([name, self.scores[name]])
        return outList
    
    def displayScores(self, x, y):
        #prints scores to screen
        #takes x and y of position to draw from
        textSize(30)
        fill(255)
        text("NAME", x, 50 + y)
        text("SCORE", x+300, 50 + y)
        for i in range(self.start, self.start+5):
            if i >= len(self.scoreList):
                break
            text(self.scoreList[i][0], x, (i-self.start)*100 + 150 + y)
            text(self.scoreList[i][1], x+300, (i-self.start)*100 + 150 + y)
            
    def incrementStart(self, direction):
        #takes 1/-1 to scroll up/down
        if self.start + 5 < len(self.scores) and direction == 1:
            self.start += direction
        elif self.start > 0 and direction == -1:
            self.start += direction
            
    def resetStart(self):
        #resets scrolling
        self.start = 0
        
    def addScore(self, player):
        #adds a score based on a PlayerInfo obj
        if player.name in self.scores:
            if self.scores[player.name] > player.score:
                self.scores[player.name] = player.score
                
                index = binarySearch(0, self.scoreList, player.name)
                self.scoreList[index][1] = player.score
        else:
            self.scores[player.name] = player.score
            self.scoreList.append([player.name, player.score])
            self.scoreList = insertionSort(1, self.scoreList)
        
    def updateFile(self):
        #sorts scores
        f = open("scores.pickle", "wb")
        pickle.dump(self.scores, f)
        f.close()
        
    def findScore(self, player):
        #takes a PlayerInfo and returns a score/None
        if player.name in self.scores:
            return self.scores[player.name]
        else:
            return None

def binarySearch(colNum, passedList, searchItem):
    #takes sorted list and an item
    #returns position of item in list
    top = 0
    bottom = len(passedList)
    middle = (bottom + top) // 2
    
    if passedList[middle][colNum] == searchItem:
        return middle
    
    while top != bottom:
        if passedList[middle][colNum] < searchItem:
            top = middle + 1
        else: 
            bottom = middle - 1
        middle = (bottom + top) // 2
        
    if passedList[middle][colNum] == searchItem:
        return middle
    else:
        print("Item not found")
        return None
    
def insertionSort(colNum, passedList):
    #takes list, sorts from small to big
    length = len(passedList)
    for i in range(length-1):
        #find minimum value in rest of list
        minimum = passedList[i][colNum]
        minimumPos = i
        for j in range(i, length):
            if passedList[j][colNum] < minimum:
                minimum = passedList[j][colNum]
                minimumPos = j
                
        #insert min value with value at correct pos
        passedList.insert(i, passedList[minimumPos])
        passedList.pop(minimumPos+1)
    return passedList

def quickSort(colNum, passedList):
    length = len(passedList)
    
    if length <= 1:
        return passedList
    
    pivot = 0
    pivotValue = passedList[pivot][colNum]
    
    leftMark = 1
    rightMark = length-1
    done = False
    
    while not done:
        while leftMark <= rightMark and passedList[leftMark][colNum] <= pivotValue:
            leftMark += 1
        
        while passedList[rightMark][colNum] > pivotValue and leftMark <= rightMark:
            rightMark -= 1
        
        if rightMark < leftMark:
            done = True
        else:
            (passedList[leftMark], passedList[rightMark]) = (passedList[rightMark], passedList[leftMark])
        
    (passedList[pivot], passedList[rightMark]) = (passedList[rightMark], passedList[pivot])

    return quickSort(colNum, passedList[:rightMark]) + [passedList[rightMark]] + quickSort(colNum, passedList[rightMark+1:])
        
