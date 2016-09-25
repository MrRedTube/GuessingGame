from random import randint

def DoGame():

	smallestNumber = 0
	biggestNumber = 100
	randomNumber = 0
	while True:
		randomNumber = randint(smallestNumber, biggestNumber)
		print(randomNumber)
		inputStr = input("Hoger, lager of correct?(H/L/C)")
		
		if len(inputStr) > 1 or len(inputStr) <= 0:
			return 0
		
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
		print("Waar ben je nou mee bezig? Zo kunnen wij niet verder, jongeman.")
	else:
		print("Ik win altijd")
		
	inputStr = input("Nog een potje?(Y/N)")
	
	if "n" in inputStr.lower():
		quit();