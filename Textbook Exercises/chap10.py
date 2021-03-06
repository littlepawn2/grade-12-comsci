##chapter 10-lists&stuff
# Chapter 10
# Exercise # 10

def countfivelenwords(passedList):
    count = 0
    for word in passedList:
        if len(word) == 5:
            count += 1
    return count

# Exercise # 11

def uptoevenSum(passedList):
    numSum = 0
    for num in passedList:
        if num % 2 == 0:
            break
        numSum += num
    return numSum

# Exercise # 12

def uptosam(passedList):
    count = 0
    for word in passedList:
        count += 1
        if word.upper() == "SAM":
            break
    return count

# Exercise # 13

#count
def mycount(obj, passedList):
    count = 0
    for thing in passedList:
        count += 1
        if thing == obj:
            break
    return count

#in
def myin(obj, passedList):
    index = 0
    while index < len(passedList):
        if passedList[index] == obj:
            return True
        index += 1
    return False

#reverse
def myreverse(passedList):
    outList = []
    for i in range(1, len(passedList)+1):
        outList.append(passedList[-i])
    return outList

#index
def myindex(obj, passedList):
    for i in range(len(passedList)):
        if passedList[i] == obj:
            return i
    return -1

#insert
def myinsert(index, obj, passedList):
    return passedList[:index] + [obj] + passedList[index:]

# Exercise # 14

def myreplace(string, old, new):
    charlist = list(string)
    indexofchanges = []
    old = list(old)
    lenold = len(old)
    for i in range(len(charlist)-lenold, 0, -1):
        if charlist[i:i+lenold] == old:
            indexofchanges.append(i)
    for i in indexofchanges:
        charlist[i:i+lenold] = new
    return "".join(charlist)

# Exercise # 15 & 16

def expandL(rulekeys, rules, string, depth):
    for i in range(depth):
        for j in range(len(rules)):
            string = applyRule(rulekeys[j], rules[j], string)
    return string

def applyRule(rulekey, rule, string):
    stringlist = list(string)
    for i in range(len(stringlist)):
        if stringlist[i] == rulekey:
            stringlist[i] = rule
    return "".join(stringlist)
    
def drawLines(string, turtlein, distance, angle):
    savedTurtles = []
    for char in string:
        if char == "F":
            turtlein.forward(distance)
        elif char == "B":
            turtlein.backward(distance)
        elif char == "+":
            turtlein.right(angle)
        elif char == "-":
            turtlein.left(angle)
        elif char == "[":
            savedTurtles.append([turtlein.heading(), turtlein.xcor(), turtlein.ycor()])
        elif char == "]":
            lastTurtle = savedTurtles.pop()
            turtlein.setheading(lastTurtle[0])
            turtlein.setposition(lastTurtle[1], lastTurtle[2])


# ________________________________________

# Call code for Exercise 10

# print(countfivelenwords(["hello", "bye", "hi", "words"]))

# Call code for Exercise 11

# print(uptoevenSum([3, 3, 3, 4, 3, 3]))

# Call code for Exercise 12

# print(uptosam(["hi", "hi", "hi", "Sam", "hi"]))

# Call code for Exercise 13

# print(mycount(3, [1, 2, 3, 4, 5, 3, 4, 3]))

# print(myin(3, [1, 2, 3, 4, 5]))
# print(myin(6, [1, 2, 3, 4, 5]))

# print(myreverse([1, 2, 3, 4, 5]))

# print(myindex(3, [1, 2, 3, 4, 5]))
# print(myindex(7, [1, 2, 3, 4, 5]))

# print(myinsert(3, 0, [1, 2, 3, 4, 5]))

# Call code for Exercise 14

# print(myreplace('Mississippi', 'i', 'I'))

import turtle

# Call code for Exercise 15

# wn = turtle.Screen()
# clyde = turtle.Turtle()
# rulekeys = ["H", "X"]
# rules = ["HFX[+H][-H]", "X[-FFF][+FFF]FX"]

# string = expandL(rulekeys, rules, "H", 3)
# drawLines(string, clyde, 10, 25.7)
# wn.exitonclick()

# Call code for Exercise 16

# wn = turtle.Screen()
# jim = turtle.Turtle()
# rulekeys = ["F"]
# rules = ["F[-F]F[+F]F"]

# string = expandL(rulekeys, rules, "F", 4)
# drawLines(string, jim, 10, 25)
# wn.exitonclick()


    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    