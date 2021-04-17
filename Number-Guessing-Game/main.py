import random

def guessNumber():

	attempts = 1

	player = input(f"Let's play Number Guessing Game! \nWhat's your name? ")

	print(f"Hello {player}! Let the fun begin! Just keep it in mind, you have 5 chances only!")

	number = int(input("Guess A Number between 1 - 10!: "))

	randomNumber = random.randint(1, 10)

	if number < 1 or number > 10:
		print("Please enter the number is range! (Between 1 - 100!)")

	else:
		try:
			while(attempts < 5):
				if(number == randomNumber):
					print(f"{player}, You Got it in {attempts} attempts. Congratulations !!")
					break
				else:
					if (number > randomNumber):
						print(f"{player}, you guessed it a bit high!")
					elif(number < randomNumber):
						print(f"{player}, you guessed it a bit low!")

					print("Let's try again! Enter another number!")
					number = int(input())
					attempts+=1
			if(attempts == 5):
				print(f"Oops! You Ran Out of Attempts! The number is: {randomNumber}")
		except:
			print("Oops! An Error Occured!!")

if __name__ == '__main__':
    guessNumber()