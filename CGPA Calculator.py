from tkinter import *
from Course import Course


def killAll(number):
	for i in range (number):
		listOfPrompts[i].destroy()
		listOfGrade[i].destroy()
		listOfWeight[i].destroy()
	del listOfPrompts[:]
	del listOfGrade[:]
	del listOfWeight[:]
	del listOfChoice[:]

def createBoxes(temp):
	killAll(len(listOfPrompts))
	number = int(temp)
	for i in range (number):
		weightChoice = StringVar(mainWindow)
		weightChoice.set(options[0]) 
		listOfChoice.append(weightChoice)
		tempString = ("Course "+ str(i+1)+":")
		listOfPrompts.append(Label(mainWindow, text = tempString))
		listOfPrompts[i].grid(row = i+4, column = 0, sticky=W)
		listOfGrade.append(Entry(mainWindow))
		listOfGrade[i].grid(row = i+4, column = 1, sticky=W)
		listOfWeight.append(OptionMenu(mainWindow,listOfChoice[i],*weights))
		listOfWeight[i].grid(row = i+4, column = 2, sticky=W)

def convertToPoint(percentGrade):
	if (percentGrade > 89):
		return 12
	elif (percentGrade > 84):
		return 11
	elif (percentGrade > 79):
		return 10
	elif (percentGrade > 76):
		return 9
	elif (percentGrade > 72):
		return 8
	elif (percentGrade > 69):
		return 7
	elif (percentGrade > 66):
		return 6
	elif (percentGrade > 62):
		return 5
	elif (percentGrade > 59):
		return 4
	elif (percentGrade > 56):
		return 3
	elif (percentGrade > 52):
		return 2
	elif (percentGrade > 49):
		return 1

def calculate():
	listOfCourses = []
	totalGrade = 0
	totalWeight = 0
	for i in range (len(listOfPrompts)):
		weight = float(listOfChoice[i].get())
		percentGrade = float(listOfGrade[i].get())
		gradePoint = convertToPoint(percentGrade)
		listOfCourses.append(Course(weight, gradePoint))
	
	for i in range (len(listOfCourses)):
		totalGrade = totalGrade +listOfCourses[i].returnGrade()
		totalWeight = totalWeight +listOfCourses[i].returnWeight()
	finalGPA = totalGrade/totalWeight
	finalGPA = round(finalGPA,1)
	answerString.set(finalGPA)
		


mainWindow = Tk()

listOfPrompts = []
listOfGrade = []
listOfWeight = []
listOfChoice = []
answerString = StringVar()

options = ["1","2","3","4","5","6","7","8","9","10"]
weights = ["0.5","1"]

numberOfCourses = StringVar(mainWindow)
numberOfCourses.set(options[4]) 


createBoxes("5")
optionBox = OptionMenu(mainWindow, numberOfCourses,*options, command = createBoxes)
optionBox.grid(row = 0, column = 1)

userPrompt = Label(mainWindow, text = "Number of Courses: ")
userPrompt.grid(row = 0, column = 0)

userPrompt1 = Label(mainWindow, text = "Enter percentage grade: ")
userPrompt1.grid(row = 1, column = 1)

userPrompt2 = Label(mainWindow, text = "Weight: ")
userPrompt2.grid(row = 1, column = 2)
	
calculateButton = Button(mainWindow, text="Calculate!", command = calculate)
calculateButton.grid(row = 16, column = 0, columnspan = 3)
	
displayGPA = Label(mainWindow, textvariable = answerString)
displayGPA.grid(row = 15, column = 0, columnspan = 3)
	
quitButton = Button(mainWindow, text="Quit!", command = quit)
quitButton.grid(row = 17, column = 0, columnspan = 3)

mainWindow.mainloop()
	


