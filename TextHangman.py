#Rohan Khanderia
#Computer Science II
#Period 5
#Hangman Project

#Converts the secret phrase into the underscores.
def wordToDash(secretPhrase):
	n = 0
	dashes = ""
	letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
	while n < int(len(secretPhrase)):
		if secretPhrase[n] not in letters != True:
			dashes = dashes + (secretPhrase[n])
		else:
			dashes = dashes + "_"
		n = n + 1
	return dashes

#This serves multiple purposes. It determines whether the guess is a letter in the first place, and if it is, it goes through the word and sees if you already guessed the letter or not.
def checkUsed(secretPhrase, guess, wrongGuesses, rightGuesses):
	count = 0
	length = int(len(secretPhrase))
	letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
	if guess in letters == False:
		return False
	while count < length:
		if secretPhrase[count] == guess:
			correct_letter = secretPhrase[count]
			for x in range(len(rightGuesses)):
				if guess == rightGuesses[x]:
					return "You have already guessed this letter"
			return correct_letter
		elif secretPhrase[count] != guess:
			 count = count + 1
		for x in range(len(wrongGuesses)):
			if guess == wrongGuesses[x]:
				return "You have already guessed this letter"
	return True

#This adds spaces in between the secret phrase.
def addSpaces(secretPhrase):
	n = 0
	y = ""
	while n < len(secretPhrase):
		y = y + secretPhrase[n] + " "
		n += 1
	return y

#This checks if the guess is in the word, and if it does, it uses the slice feature to insert the guess into the string in place of an underscore.
def convertDashesToLetters(secretPhrase, correct_letter, dashes):
	x = 0
	while x < int(len(secretPhrase)):
		if secretPhrase[x] == correct_letter:
			dashes = dashes[0:x] + correct_letter + dashes[x+1:]
		x = x + 1
	return dashes

#The main function, where everything is called from.
def main():
	print("Hangman is a word game where you are given a certain number of blanks to fill in")
	print("trying to guess a specific word. You have 6 tries in this game to guess the word")
	print("and you will lose if you are unable to guess the word within 6 chances.")
	secretPhrase = input("Please enter a phrase to guess: ").lower()
	original = secretPhrase
	secretPhrase = addSpaces(secretPhrase)
	dashes = wordToDash(secretPhrase)
	tries = 6
	wrongGuesses = None
	rightGuesses = ""
	while tries > 0 and secretPhrase != dashes:
		if wrongGuesses == "":
			wrongGuesses = None
		print("Chances left: " + str(tries))
		print("Wrong guesses: " + str(wrongGuesses))
		print("")
		print(dashes)
		print("")
		guess = input("Please type a letter to guess: ")
		letter = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
		while guess not in letter:
			guess = input("ERROR. Please enter a letter: ")
		guess = guess.lower()
		if wrongGuesses == None:
			wrongGuesses = ""
		if checkUsed(secretPhrase, guess, wrongGuesses, rightGuesses) == False:
			print("This is not a letter. Please enter a letter: ")
		elif checkUsed(secretPhrase, guess, wrongGuesses, rightGuesses) == True:
			print("This letter is not present.")
			tries = tries - 1
			wrongGuesses = wrongGuesses + " " + guess
		elif checkUsed(secretPhrase, guess, wrongGuesses, rightGuesses) == guess:
			correct_letter = checkUsed(secretPhrase, guess, wrongGuesses, rightGuesses)
			dashes = convertDashesToLetters(secretPhrase, correct_letter, dashes)
			rightGuesses = rightGuesses + guess
		elif checkUsed(secretPhrase, guess, wrongGuesses, rightGuesses) == "You have already guessed this letter":
			print("You have already guessed this letter. Guess again: ")
			
#The following will check how many tries the player has left, and will accordingly print out what the hangman is meant to look like at the time.
		if tries == 6:
			print("___________")
			print("|          ")
			print("|          ")
			print("|          ")
			print("|          ")
			print("|          ")
			print("|          ")
			print("|          ")
			print("_______    ")
			print("You have 6 tries left")
		if tries == 5:
			print("___________")
			print("|    |     ")
			print("|    0     ")
			print("|          ")
			print("|          ")
			print("|          ")
			print("|          ")
			print("|          ")
			print("_______    ")
			print("You have 5 tries left")
		if tries == 4:
			print("___________")
			print("|    |     ")
			print("|    0     ")
			print("|    |     ")
			print("|          ")
			print("|          ")
			print("|          ")
			print("|          ")
			print("_______    ")
			print("You have 4 tries left")
		if tries == 3:
			print("___________")
			print("|    |     ")
			print("|    0     ")
			print("|    |-    ")
			print("|          ")
			print("|          ")
			print("|          ")
			print("|          ")
			print("_______    ")
			print("You have 3 tries left")
		if tries == 2:
			print("___________")
			print("|    |     ")
			print("|    0     ")
			print("|   -|-    ")
			print("|          ")
			print("|          ")
			print("|          ")
			print("|          ")
			print("_______    ")
			print("You have 2 tries left")
		if tries == 1:
			print("___________")
			print("|    |     ")
			print("|    0     ")
			print("|   -|-    ")
			print("|     \    ")
			print("|          ")
			print("|          ")
			print("|          ")
			print("_______    ")
			print("You have 1 tries left")

#The user loses.
	if tries == 0:
		print("___________")
		print("|    |     ")
		print("|    0     ")
		print("|   -|-    ")
		print("|   / \    ")
		print("|          ")
		print("|          ")
		print("|          ")
		print("_______    ")
		print("The game is over!")
		print("The secret phrase was:", original)

#The user wins.
	else:
		print("Congratulations! You win!")
		print("The secret phrase was:", original)
		
			
main()