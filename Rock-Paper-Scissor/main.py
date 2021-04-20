import random

# userChoice = int(input(" 1. Rock \n 2. Paper \n 3. Scissor \n Your Choice: "))
def computeGame(userChoice, compterChoice):

	if userChoice == compterChoice:
		print("It's a tie!")
	elif userChoice == 1:
		if compterChoice == 2:
			print("Computer wins!")
		else:
			print("You win! Congratulations!")
	elif userChoice == 2:
		if compterChoice == 3:
			print("Computer wins!")
		else:
			print("You win! Congratulations!")
	elif userChoice == 3:
		if compterChoice == 1:
			print("Computer wins!")
		else:
			print("You win! Congratulations!")


playAgain = "yes"

while playAgain.lower() == "yes" or playAgain.lower() == "y":
	userChoice = int(input(" 1. Rock \n 2. Paper \n 3. Scissor \n Your Choice: "))

	compterChoice = random.randint(1, 3)

	if userChoice < 1 or userChoice > 3:
	
		print("Please select a valid option!")

	else :

		print("Computer's Choice is:", compterChoice)

		computeGame(userChoice, compterChoice)

	playAgain = input("Wanna try again? (Yes / No): ")
