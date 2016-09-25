from random import randint

def DoGame():

	smallestNumber = 0
	biggestNumber = 100
	randomNumber = 0
	while True:
		randomNumber = randint(smallestNumber, biggestNumber)
		print(randomNumber)
		inputStr = input("Hoger, lager of correct?(H/L/C)")
		if "h" in inputStr.lower():
			smallestNumber = randomNumber
		elif "l" in inputStr.lower():
			biggestNumber = randomNumber
		elif "c" in inputStr.lower():
			return 1
			
			
		if smallestNumber >= biggestNumber:
			return 0
		
while True:
	if DoGame() == 0:
		print("Lekker aan het cheaten?")
	else:
		print("Ik win altijd")
		
	inputStr = input("Nog een potje?(Y/N)")
	
	if "N" in inputStr:
		quit();