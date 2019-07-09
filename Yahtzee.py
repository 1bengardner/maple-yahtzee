#1
from Tkinter import *
import random

def gameOver():
    top = Toplevel(bg="orange")
    top.title("Game Over")
    topFrame = Frame(top, bg="orange", relief="ridge", bd=5)
    gameOverTitle = Label(topFrame, text="Game Over", font=("arial", 20), bg="orange")
    gameOverText = Label(topFrame, text="You finished the game with "+str(totalScore)+" points and "+str(yahtzeeCount)+" yahtzees.", bg="orange")
    okButton = Button(topFrame, text="OK", bg="yellow", command=top.destroy)
    topFrame.grid()
    gameOverTitle.grid(row=1, column=1, pady=10)
    gameOverText.grid(row=2, column=1, pady=5, padx=10)
    okButton.grid(row=3, column=1, ipadx=20, pady=20)
    
    resetGame()

def diceReset():
    global rollCount
    global potentialScore
    potentialScore = 0
    rollCount = 0
    die1.config(image=photoList[20])
    die2.config(image=photoList[20])
    die3.config(image=photoList[20])
    die4.config(image=photoList[20])
    die5.config(image=photoList[20])
    die1.value=0
    die2.value=0
    die3.value=0
    die4.value=0
    die5.value=0
    dieHold1.deselect()
    dieHold2.deselect()
    dieHold3.deselect()
    dieHold4.deselect()
    dieHold5.deselect()
    rollScore.config(text="Roll Value: "+str(potentialScore))
    selectButton.config(state="disabled")
    rollButton.config(state="normal")
    rollCountLabel.config(text="Rolls Made: "+str(rollCount))

def select():
    global totalScore
    global selectionCount
    global subTotal
    global yahtzeeCount
    global subTotalBonus
    if rollUsed != 0:
        if rollUsed == 1:
            onesButton.config(state="disabled")
            subTotal += potentialScore
        elif rollUsed == 2:
            twosButton.config(state="disabled")
            subTotal += potentialScore
        elif rollUsed == 3:
            threesButton.config(state="disabled")
            subTotal += potentialScore
        elif rollUsed == 4:
            foursButton.config(state="disabled")
            subTotal += potentialScore
        elif rollUsed == 5:
            fivesButton.config(state="disabled")
            subTotal += potentialScore
        elif rollUsed == 6:
            sixesButton.config(state="disabled")
            subTotal += potentialScore
        elif rollUsed == 7:
            threeOfAKindButton.config(state="disabled")
        elif rollUsed == 8:
            fourOfAKindButton.config(state="disabled")
        elif rollUsed == 9:
            fullHouseButton.config(state="disabled")
        elif rollUsed == 10:
            smallStraightButton.config(state="disabled")
        elif rollUsed == 11:
            largeStraightButton.config(state="disabled")
        elif rollUsed == 12:
            chanceButton.config(state="disabled")
        elif rollUsed == 13:
            yahtzeeButton.config(state="disabled")
        selectionCount += 1
        totalScore += potentialScore
        if bonusYahtzee:
            totalScore += 100
            yahtzeeCount += 1
        if subTotal >= 63 and subTotalBonus == False:
            totalScore += 35
            subTotalBonus = True
            subTotalLabel.config(fg="red")
        yahtzeeCountLabel.config(text="Yahtzees: "+str(yahtzeeCount))
        subTotalLabel.config(text="Sub Total: "+str(subTotal))
        scoreLabel.config(text="SCORE "+str(totalScore))
        
        diceReset()
        if selectionCount == 13:
            gameOver()
    else:
        pass


def ones():
    global rollUsed
    global potentialScore
    potentialScore = 0
    if die1.value == 1:
        potentialScore += 1
    if die2.value == 1:
        potentialScore += 1
    if die3.value == 1:
        potentialScore += 1
    if die4.value == 1:
        potentialScore += 1
    if die5.value == 1:
        potentialScore += 1
    rollScore.config(text="Roll Value: "+str(potentialScore))
    rollUsed = 1

def twos():
    global rollUsed
    global potentialScore
    potentialScore = 0
    if die1.value == 2:
        potentialScore += 2
    if die2.value == 2:
        potentialScore += 2
    if die3.value == 2:
        potentialScore += 2
    if die4.value == 2:
        potentialScore += 2
    if die5.value == 2:
        potentialScore += 2
    rollScore.config(text="Roll Value: "+str(potentialScore))
    rollUsed = 2

def threes():
    global rollUsed
    global potentialScore
    potentialScore = 0
    if die1.value == 3:
        potentialScore += 3
    if die2.value == 3:
        potentialScore += 3
    if die3.value == 3:
        potentialScore += 3
    if die4.value == 3:
        potentialScore += 3
    if die5.value == 3:
        potentialScore += 3
    rollScore.config(text="Roll Value: "+str(potentialScore))
    rollUsed = 3

def fours():
    global rollUsed
    global potentialScore
    potentialScore = 0
    if die1.value == 4:
        potentialScore += 4
    if die2.value == 4:
        potentialScore += 4
    if die3.value == 4:
        potentialScore += 4
    if die4.value == 4:
        potentialScore += 4
    if die5.value == 4:
        potentialScore += 4
    rollScore.config(text="Roll Value: "+str(potentialScore))
    rollUsed = 4

def fives():
    global rollUsed
    global potentialScore
    potentialScore = 0
    if die1.value == 5:
        potentialScore += 5
    if die2.value == 5:
        potentialScore += 5
    if die3.value == 5:
        potentialScore += 5
    if die4.value == 5:
        potentialScore += 5
    if die5.value == 5:
        potentialScore += 5
    rollScore.config(text="Roll Value: "+str(potentialScore))
    rollUsed = 5

def sixes():
    global rollUsed
    global potentialScore
    potentialScore = 0
    if die1.value == 6:
        potentialScore += 6
    if die2.value == 6:
        potentialScore += 6
    if die3.value == 6:
        potentialScore += 6
    if die4.value == 6:
        potentialScore += 6
    if die5.value == 6:
        potentialScore += 6
    rollScore.config(text="Roll Value: "+str(potentialScore))
    rollUsed = 6

def threeOfAKind():
    global rollUsed
    global potentialScore
    potentialScore = 0
    if (die1.value == die2.value == die3.value)\
or (die1.value == die2.value == die4.value)\
or (die1.value == die2.value == die5.value)\
or (die1.value == die3.value == die4.value)\
or (die1.value == die3.value == die5.value)\
or (die1.value == die4.value == die5.value)\
or (die2.value == die3.value == die4.value)\
or (die2.value == die3.value == die5.value)\
or (die2.value == die4.value == die5.value)\
or (die3.value == die4.value == die5.value):
        potentialScore = die1.value + die2.value + die3.value + die4.value + die5.value
    rollScore.config(text="Roll Value: "+str(potentialScore))
    rollUsed = 7

def fourOfAKind():
    global rollUsed
    global potentialScore
    potentialScore = 0
    if (die1.value == die2.value == die3.value == die4.value)\
or (die1.value == die2.value == die3.value == die5.value)\
or (die1.value == die2.value == die4.value == die5.value)\
or (die1.value == die3.value == die4.value == die5.value)\
or (die2.value == die3.value == die4.value == die5.value):
        potentialScore = die1.value + die2.value + die3.value + die4.value + die5.value
    rollScore.config(text="Roll Value: "+str(potentialScore))
    rollUsed = 8

def fullHouse():
    global rollUsed
    global potentialScore
    potentialScore = 0
    if (((die1.value == die2.value) and (die3.value == die4.value == die5.value))\
or ((die1.value == die3.value) and (die2.value == die4.value == die5.value))\
or ((die1.value == die4.value) and (die2.value == die3.value == die5.value))\
or ((die1.value == die5.value) and (die2.value == die4.value == die3.value))\
or ((die2.value == die3.value) and (die1.value == die4.value == die5.value))\
or ((die2.value == die4.value) and (die1.value == die3.value == die5.value))\
or ((die2.value == die5.value) and (die1.value == die4.value == die3.value))\
or ((die3.value == die4.value) and (die1.value == die2.value == die5.value))\
or ((die3.value == die5.value) and (die1.value == die2.value == die4.value))\
or ((die4.value == die5.value) and (die1.value == die2.value == die3.value)))\
and ((die1.value == die2.value == die3.value == die4.value == die5.value) == False):
        potentialScore = 25
    rollScore.config(text="Roll Value: "+str(potentialScore))
    rollUsed = 9

def smallStraight():
    global rollUsed
    global potentialScore
    potentialScore = 0
    if (((die1.value == 1) or (die2.value == 1) or (die3.value == 1) or (die4.value == 1) or (die5.value == 1))\
and ((die1.value == 2) or (die2.value == 2) or (die3.value == 2) or (die4.value == 2) or (die5.value == 2))\
and ((die1.value == 3) or (die2.value == 3) or (die3.value == 3) or (die4.value == 3) or (die5.value == 3))\
and ((die1.value == 4) or (die2.value == 4) or (die3.value == 4) or (die4.value == 4) or (die5.value == 4)))\
or (((die1.value == 2) or (die2.value == 2) or (die3.value == 2) or (die4.value == 2) or (die5.value == 2))\
and ((die1.value == 3) or (die2.value == 3) or (die3.value == 3) or (die4.value == 3) or (die5.value == 3))\
and ((die1.value == 4) or (die2.value == 4) or (die3.value == 4) or (die4.value == 4) or (die5.value == 4))\
and ((die1.value == 5) or (die2.value == 5) or (die3.value == 5) or (die4.value == 5) or (die5.value == 5)))\
or (((die1.value == 3) or (die2.value == 3) or (die3.value == 3) or (die4.value == 3) or (die5.value == 3))\
and ((die1.value == 4) or (die2.value == 4) or (die3.value == 4) or (die4.value == 4) or (die5.value == 4))\
and ((die1.value == 5) or (die2.value == 5) or (die3.value == 5) or (die4.value == 5) or (die5.value == 5))\
and ((die1.value == 6) or (die2.value == 6) or (die3.value == 6) or (die4.value == 6) or (die5.value == 6))):
        potentialScore = 30
    rollScore.config(text="Roll Value: "+str(potentialScore))
    rollUsed = 10

def largeStraight():
    global rollUsed
    global potentialScore
    potentialScore = 0
    if (((die1.value == 1) or (die2.value == 1) or (die3.value == 1) or (die4.value == 1) or (die5.value == 1))\
and ((die1.value == 2) or (die2.value == 2) or (die3.value == 2) or (die4.value == 2) or (die5.value == 2))\
and ((die1.value == 3) or (die2.value == 3) or (die3.value == 3) or (die4.value == 3) or (die5.value == 3))\
and ((die1.value == 4) or (die2.value == 4) or (die3.value == 4) or (die4.value == 4) or (die5.value == 4))\
and ((die1.value == 5) or (die2.value == 5) or (die3.value == 5) or (die4.value == 5) or (die5.value == 5)))\
or (((die1.value == 2) or (die2.value == 2) or (die3.value == 2) or (die4.value == 2) or (die5.value == 2))\
and ((die1.value == 3) or (die2.value == 3) or (die3.value == 3) or (die4.value == 3) or (die5.value == 3))\
and ((die1.value == 4) or (die2.value == 4) or (die3.value == 4) or (die4.value == 4) or (die5.value == 4))\
and ((die1.value == 5) or (die2.value == 5) or (die3.value == 5) or (die4.value == 5) or (die5.value == 5))\
and ((die1.value == 6) or (die2.value == 6) or (die3.value == 6) or (die4.value == 6) or (die5.value == 6))):
        potentialScore = 40
    rollScore.config(text="Roll Value: "+str(potentialScore))
    rollUsed = 11

def chance():
    global rollUsed
    global potentialScore
    potentialScore = die1.value + die2.value + die3.value + die4.value + die5.value
    rollScore.config(text="Roll Value: "+str(potentialScore))
    rollUsed = 12

def yahtzee():
    global rollUsed
    global potentialScore
    global yahtzeeCount
    potentialScore = 0
    if die1.value == die2.value == die3.value == die4.value == die5.value and die1.value != 0:
        potentialScore = 50
        yahtzeeCount += 1
    rollScore.config(text="Roll Value: "+str(potentialScore))
    rollUsed = 13

def roll():
    global rollCount
    global rollUsed
    global bonusYahtzee
    potentialScore = 0
    rollUsed = 0
    bonusYahtzee = False
    rollScore.config(text="Roll Value: "+str(potentialScore))
    selectButton.config(state="normal")
    if h1.get() == False or die1.value == 0:
        number = random.randrange(1,7)
        die1.config(image=photoList[number-1])
        die1.value=number
    if h2.get() == False or die2.value == 0:
        number = random.randrange(1,7)
        die2.config(image=photoList[number-1])
        die2.value=number
    if h3.get() == False or die3.value == 0:
        number = random.randrange(1,7)
        die3.config(image=photoList[number-1])
        die3.value=number
    if h4.get() == False or die4.value == 0:
        number = random.randrange(1,7)
        die4.config(image=photoList[number-1])
        die4.value=number
    if h5.get() == False or die5.value == 0:
        number = random.randrange(1,7)
        die5.config(image=photoList[number-1])
        die5.value=number
    if die1.value == die2.value == die3.value == die4.value == die5.value:
        if yahtzeeCount == 0:
            yahtzeeButton.flash()
        else:
            bonusYahtzee = True
    rollCount += 1
    rollCountLabel.config(text="Rolls Made: "+str(rollCount))
    rollDisable()

def rollDisable():
    if rollCount == 3:
        rollButton.config(state="disabled")

def resetGame():
    global rollCount
    global potentialScore
    global totalScore
    global selectionCount
    global yahtzeeCount
    global subTotal
    global bonusYahtzee
    global subTotalBonus
    rollCount=0
    potentialScore=0
    totalScore=0
    selectionCount=0
    subTotal=0
    bonusYahtzee=False
    subTotalBonus=False

    rollButton.config(state="normal")
    onesButton.config(state="normal")
    twosButton.config(state="normal")
    threesButton.config(state="normal")
    foursButton.config(state="normal")
    fivesButton.config(state="normal")
    sixesButton.config(state="normal")
    threeOfAKindButton.config(state="normal")
    fourOfAKindButton.config(state="normal")
    fullHouseButton.config(state="normal")
    smallStraightButton.config(state="normal")
    largeStraightButton.config(state="normal")
    chanceButton.config(state="normal")
    yahtzeeButton.config(state="normal")

    rollScore.config(text="Roll Value: "+str(potentialScore))
    scoreLabel.config(text="SCORE "+str(totalScore))
    yahtzeeCountLabel.config(text="Yahtzees: "+str(yahtzeeCount))
    subTotalLabel.config(text="Sub Total: "+str(subTotal), fg="black")
    
    diceReset()


#main
rollCount = 0
potentialScore = 0
totalScore = 0
selectionCount = 0
subTotal = 0
yahtzeeCount = 0
bonusYahtzee = False
subTotalBonus = False

root = Tk()

imageList = ["one.gif", "two.gif", "three.gif", "four.gif", "five.gif", "six.gif",\
             "sel1.gif", "sel2.gif", "sel3.gif", "sel4.gif", "sel5.gif", "sel6.gif",\
             "sel7.gif", "sel8.gif", "sel9.gif", "sel10.gif", "sel11.gif", "sel12.gif", "sel13.gif", "yahtzee.gif", "cards.gif"]
photoList = []
for i in range(0,len(imageList)):
    photoList.append(PhotoImage(file=imageList[i]))

root.title("Maple Yahtzee")
mainframe = Frame(root, bg="beige")
selectionFrame = Frame(mainframe, relief="ridge", bd=4)
diceFrame = Frame(mainframe, bg="orange")
statsFrame = LabelFrame(diceFrame, bg="orange", text="Game Data")
valuesFrame = LabelFrame(diceFrame, bg="orange", text="Values")

yahtzeeImage = Label(mainframe, image=photoList[19])

onesButton = Button(selectionFrame, width=40, height=40, image=photoList[6], command=ones)
twosButton = Button(selectionFrame, width=40, height=40, image=photoList[7], command=twos)
threesButton = Button(selectionFrame, width=40, height=40, image=photoList[8], command=threes)
foursButton = Button(selectionFrame, width=40, height=40, image=photoList[9], command=fours)
fivesButton = Button(selectionFrame, width=40, height=40, image=photoList[10], command=fives)
sixesButton = Button(selectionFrame, width=40, height=40, image=photoList[11], command=sixes)
threeOfAKindButton = Button(selectionFrame, width=40, height=40, image=photoList[12], command=threeOfAKind)
fourOfAKindButton = Button(selectionFrame, width=40, height=40, image=photoList[13], command=fourOfAKind)
fullHouseButton = Button(selectionFrame, width=40, height=40, image=photoList[14], command=fullHouse)
smallStraightButton = Button(selectionFrame, width=40, height=40, image=photoList[15], command=smallStraight)
largeStraightButton = Button(selectionFrame, width=40, height=40, image=photoList[16], command=largeStraight)
chanceButton = Button(selectionFrame, width=40, height=40, image=photoList[17], command=chance)
yahtzeeButton = Button(selectionFrame, width=80, height=40, image=photoList[18], activebackground="red", command=yahtzee)
rollScore = Label(selectionFrame, text="Roll Value: "+str(potentialScore))

die1 = Label(diceFrame, width=110, height=110, image=photoList[0], bd=2, relief="sunken")
die2 = Label(diceFrame, width=110, height=110, image=photoList[1], bd=2, relief="sunken", bg="lightgray")
die3 = Label(diceFrame, width=110, height=110, image=photoList[2], bd=2, relief="sunken")
die4 = Label(diceFrame, width=110, height=110, image=photoList[3], bd=2, relief="sunken", bg="lightgray")
die5 = Label(diceFrame, width=110, height=110, image=photoList[4], bd=2, relief="sunken")
h1 = IntVar()
h2 = IntVar()
h3 = IntVar()
h4 = IntVar()
h5 = IntVar()
dieHold1 = Checkbutton(diceFrame, text="HOLD", variable=h1, bg="orange", indicatoron=0)
dieHold2 = Checkbutton(diceFrame, text="HOLD", variable=h2, bg="orange", indicatoron=0)
dieHold3 = Checkbutton(diceFrame, text="HOLD", variable=h3, bg="orange", indicatoron=0)
dieHold4 = Checkbutton(diceFrame, text="HOLD", variable=h4, bg="orange", indicatoron=0)
dieHold5 = Checkbutton(diceFrame, text="HOLD", variable=h5, bg="orange", indicatoron=0)
scoreLabel = Label(diceFrame, text="SCORE "+str(totalScore), font=("arial",20), bg="orange")
rollButton = Button(diceFrame, text="ROLL", bg="red", command=roll)
resetButton = Button(diceFrame, text="Reset Game", bg="red", command=resetGame)
quitButton = Button(diceFrame, text = "Quit", bg="red", command=root.destroy)
selectButton = Button(mainframe, text="Select", bg="yellow", fg="red", command=select)

rollCountLabel = Label(statsFrame, text="Rolls Made: "+str(rollCount), bg="orange")
subTotalLabel = Label(statsFrame, text="Sub Total: "+str(subTotal), bg="orange")
yahtzeeCountLabel = Label(statsFrame, text="Yahtzees: "+str(yahtzeeCount), bg="orange")
valuesLabel = Label(valuesFrame, text = "Snail - 1\nShroom - 2\nPig - 3\nRoot - 4\nPanda - 5\nMano - 6", justify="left", bg="orange")


mainframe.grid()
selectionFrame.grid(row=1, column=2)
diceFrame.grid(row=2, column=1, columnspan=3)
statsFrame.grid(row=3, column=4, columnspan=2)
valuesFrame.grid(row=3, column=1, columnspan=2, pady=10)

yahtzeeImage.grid(row=1, column=1, sticky=W)

onesButton.grid(row=1, column=2)
twosButton.grid(row=1, column=3)
threesButton.grid(row=1, column=4)
foursButton.grid(row=1, column=5)
fivesButton.grid(row=1, column=6)
sixesButton.grid(row=1, column=7)
threeOfAKindButton.grid(row=2, column=2)
fourOfAKindButton.grid(row=2, column=3)
fullHouseButton.grid(row=2, column=4)
smallStraightButton.grid(row=2, column=5)
largeStraightButton.grid(row=2, column=6)
chanceButton.grid(row=2, column=7)
yahtzeeButton.grid(row=2, column=8)
rollScore.grid(row=1, column=8, sticky=N+E+S+W)

die1.grid(row=1, column=1)
die2.grid(row=1, column=2)
die3.grid(row=1, column=3)
die4.grid(row=1, column=4)
die5.grid(row=1, column=5)
dieHold1.grid(row=2, column=1)
dieHold2.grid(row=2, column=2)
dieHold3.grid(row=2, column=3)
dieHold4.grid(row=2, column=4)
dieHold5.grid(row=2, column=5)
scoreLabel.grid(row=3, column=2, columnspan=3, pady=20)
rollButton.grid(row=4, column=3, ipady=5, sticky=E+W)
resetButton.grid(row=4, column=5, ipady=5, sticky=E+W)
quitButton.grid(row=4, column=1, ipady=5, sticky=E+W)
selectButton.grid(row=1, column=3, ipady=35)

rollCountLabel.grid(row=1, column=1, padx=20, pady=3, sticky=W)
subTotalLabel .grid(row=2, column=1, padx=20, sticky=W)
yahtzeeCountLabel.grid(row=3, column=1, padx=20, pady=3, sticky=W)
valuesLabel.grid(row=4, column=1, padx=10)

diceReset()

root.mainloop()