import pygame
import random
import time
import os
import sys
import re
import math
from pygame.locals import *
from os import system

sys.setrecursionlimit(1000000000)

pygame.init()

clock = pygame.time.Clock()

#Sets up the window
screen_width = 1440
screen_height = 900

#Initializes the variables for colors that might be needed
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0 , 0)
green = (0, 255, 0)
blue = (0, 0, 255)
yellow = (255, 185, 15)
darkgreen = (0, 180, 0)
darkyellow = (190, 180, 10)
darkred = (180, 0, 0)
darkblue = (0, 0, 180)
grey = (128, 138, 135)

screen = pygame.display.set_mode((screen_width, screen_height))
screen.fill(white)
pygame.display.set_caption("Hangman")
clock = pygame.time.Clock

Font = pygame.font.Font("freesansbold.ttf", 25)
FontTime = pygame.font.Font("freesansbold.ttf", 40)
FontBig = pygame.font.Font("freesansbold.ttf", 50)

easyWords = ["APPLE", "TEST", "LENGTH", "BUILD", "SEAT", "PERSON", "HUMAN", "BOARD"]
mediumWords = ["LICENSE", "LAPTOP", "TRAFFIC", "DRIVER", "BACKPACK", "CARAVAN"]
hardWords = ["AUTOMOBILE", "ASTROLOGICAL", "AVENGERS", "RESPECT", "PRESIDENT", "PENTHOUSE"]

#----------------------------------------------------------------------------------------------------------	
	
def message_display(text):
	largeText = pygame.font.Font("freesansbold.ttf", 110)
	textSurface, textRect = text_objects(text, largeText)
	textRect.center = ((screen_width/2), (screen_height - 800))
	screen.blit(textSurface, textRect)
	
	pygame.display.update() 
	
def text_objects(text, font):
	textSurface = font.render(text, True, black)
	return textSurface, textSurface.get_rect()
	
def completedhangman():
	#Tries = 8
	pygame.draw.line(screen, black, (1000, 100), (1300, 100), 10)
	#Tries = 7
	pygame.draw.line(screen, black, (1000, 100), (1000, 700), 10)
	#Tries = 6
	pygame.draw.line(screen, black, (1200, 100), (1200, 175), 10)
	#Tries = 5
	pygame.draw.circle(screen, black, (1200, 225), 50)
	#Tries = 4
	pygame.draw.line(screen, black, (1200, 275), (1200, 500), 10)
	#Tries = 3
	pygame.draw.line(screen, black, (1200, 500), (1300, 600), 10)
	#Tries = 2
	pygame.draw.line(screen, black, (1200, 500), (1100, 600), 10)
	#Tries = 1
	pygame.draw.line(screen, black, (1200, 387.5), (1300, 387.5), 10)
	#Tries = 0
	pygame.draw.line(screen, black, (1200, 387.5), (1100, 387.5), 10)
	pygame.display.update()
	
def happyhangman():
	pygame.draw.line(screen, black, (1000, 100), (1300, 100), 10)
	pygame.draw.line(screen, black, (1000, 100), (1000, 700), 10)
	pygame.draw.line(screen, black, (1200, 100), (1200, 175), 10)
	pygame.draw.circle(screen, black, (1200, 305), 50)
	pygame.draw.circle(screen, white, (1180, 285), 7)
	pygame.draw.circle(screen, white, (1220, 285), 7)
	smileRect = pygame.Rect(1175, 300, 50, 20)
	pygame.draw.arc(screen, white, smileRect, math.pi, 2*math.pi, 3)
	pygame.draw.line(screen, black, (1200, 335), (1200, 600), 10)
	pygame.draw.line(screen, black, (1200, 600), (1300, 700), 10)
	pygame.draw.line(screen, black, (1200, 600), (1100, 700), 10)
	pygame.draw.line(screen, black, (1200, 387.5), (1300, 387.5), 10)
	pygame.draw.line(screen, black, (1200, 387.5), (1100, 387.5), 10)


def greyhangman():
	#Tries = 8
	pygame.draw.line(screen, grey, (1000, 100), (1300, 100), 10)
	#Tries = 7
	pygame.draw.line(screen, grey, (1000, 100), (1000, 700), 10)
	#Tries = 6
	pygame.draw.line(screen, grey, (1200, 100), (1200, 175), 10)
	#Tries = 5
	pygame.draw.circle(screen, grey, (1200, 225), 50)
	#Tries = 4
	pygame.draw.line(screen, grey, (1200, 275), (1200, 500), 10)
	#Tries = 3
	pygame.draw.line(screen, grey, (1200, 500), (1300, 600), 10)
	#Tries = 2
	pygame.draw.line(screen, grey, (1200, 500), (1100, 600), 10)
	#Tries = 1
	pygame.draw.line(screen, grey, (1200, 387.5), (1300, 387.5), 10)
	#Tries = 0
	pygame.draw.line(screen, grey, (1200, 387.5), (1100, 387.5), 10)
	pygame.display.update()

def whitehangman(): 
	#Tries = 8
	pygame.draw.line(screen, white, (1000, 100), (1300, 100), 10)
	#Tries = 7
	pygame.draw.line(screen, white, (1000, 100), (1000, 700), 10)
	#Tries = 6
	pygame.draw.line(screen, white, (1200, 100), (1200, 175), 10)
	#Tries = 5
	pygame.draw.circle(screen, white, (1200, 225), 50)
	#Tries = 4
	pygame.draw.line(screen, white, (1200, 275), (1200, 500), 10)
	#Tries = 3
	pygame.draw.line(screen, white, (1200, 500), (1300, 600), 10)
	#Tries = 2
	pygame.draw.line(screen, white, (1200, 500), (1100, 600), 10)
	#Tries = 1
	pygame.draw.line(screen, white, (1200, 387.5), (1300, 387.5), 10)
	#Tries = 0
	pygame.draw.line(screen, white, (1200, 387.5), (1100, 387.5), 10)
	pygame.display.update()

def hangman(tries, status):
	if tries == 8:
		pygame.draw.line(screen, black, (1000, 100), (1300, 100), 10)
		pygame.display.update()
	elif tries == 7:
		pygame.draw.line(screen, black, (1000, 100), (1300, 100), 10)
		pygame.draw.line(screen, black, (1000, 100), (1000, 700), 10)
		pygame.display.update()	
	elif tries == 6:
		pygame.draw.line(screen, black, (1000, 100), (1300, 100), 10)
		pygame.draw.line(screen, black, (1000, 100), (1000, 700), 10)
		pygame.draw.line(screen, black, (1200, 100), (1200, 175), 10)
		pygame.display.update()
	elif tries == 5:
		pygame.draw.line(screen, black, (1000, 100), (1300, 100), 10)
		pygame.draw.line(screen, black, (1000, 100), (1000, 700), 10)
		pygame.draw.line(screen, black, (1200, 100), (1200, 175), 10)
		pygame.draw.circle(screen, black, (1200, 225), 50)
		pygame.display.update()
	elif tries == 4:
		pygame.draw.line(screen, black, (1000, 100), (1300, 100), 10)
		pygame.draw.line(screen, black, (1000, 100), (1000, 700), 10)
		pygame.draw.line(screen, black, (1200, 100), (1200, 175), 10)
		pygame.draw.circle(screen, black, (1200, 225), 50)
		pygame.draw.line(screen, black, (1200, 275), (1200, 500), 10)	
		pygame.display.update()
	elif tries == 3:
		pygame.draw.line(screen, black, (1000, 100), (1300, 100), 10)
		pygame.draw.line(screen, black, (1000, 100), (1000, 700), 10)
		pygame.draw.line(screen, black, (1200, 100), (1200, 175), 10)
		pygame.draw.circle(screen, black, (1200, 225), 50)
		pygame.draw.line(screen, black, (1200, 275), (1200, 500), 10)
		pygame.draw.line(screen, black, (1200, 500), (1300, 600), 10)
		pygame.display.update()
	elif tries == 2:
		pygame.draw.line(screen, black, (1000, 100), (1300, 100), 10)
		pygame.draw.line(screen, black, (1000, 100), (1000, 700), 10)
		pygame.draw.line(screen, black, (1200, 100), (1200, 175), 10)
		pygame.draw.circle(screen, black, (1200, 225), 50)
		pygame.draw.line(screen, black, (1200, 275), (1200, 500), 10)
		pygame.draw.line(screen, black, (1200, 500), (1300, 600), 10)
		pygame.draw.line(screen, black, (1200, 500), (1100, 600), 10)
		pygame.display.update()
	elif tries == 1:
		pygame.draw.line(screen, black, (1000, 100), (1300, 100), 10)
		pygame.draw.line(screen, black, (1000, 100), (1000, 700), 10)
		pygame.draw.line(screen, black, (1200, 100), (1200, 175), 10)
		pygame.draw.circle(screen, black, (1200, 225), 50)
		pygame.draw.line(screen, black, (1200, 275), (1200, 500), 10)
		pygame.draw.line(screen, black, (1200, 500), (1300, 600), 10)
		pygame.draw.line(screen, black, (1200, 500), (1100, 600), 10)
		pygame.draw.line(screen, black, (1200, 387.5), (1300, 387.5), 10)
		pygame.display.update()
	elif tries == 0 and status == "lose":
		pygame.draw.line(screen, black, (1000, 100), (1300, 100), 10)
		pygame.draw.line(screen, black, (1000, 100), (1000, 700), 10)
		pygame.draw.line(screen, black, (1200, 100), (1200, 175), 10)
		pygame.draw.circle(screen, black, (1200, 225), 50)
		pygame.draw.line(screen, black, (1200, 275), (1200, 500), 10)
		pygame.draw.line(screen, black, (1200, 500), (1300, 600), 10)
		pygame.draw.line(screen, black, (1200, 500), (1100, 600), 10)
		pygame.draw.line(screen, black, (1200, 387.5), (1300, 387.5), 10)
		pygame.draw.line(screen, black, (1200, 387.5), (1100, 387.5), 10)
		pygame.display.update()


def gameDifficulty():
	mode = None
	mouse = pygame.mouse.get_pos()
	click = pygame.mouse.get_pressed()

	#EASY
	if (screen_width * .25) + 170 > mouse[0] > (screen_width * .25) and (200 + 100) > mouse[1] >  200:
		pygame.draw.rect(screen, darkgreen, ((screen_width * (.25)), (200), 170, 100))
	else:
		pygame.draw.rect(screen, green, ((screen_width * (.25)), (200), 170, 100))
		
	smalltext = pygame.font.Font("freesansbold.ttf", 40)
	textSurface, textRect = text_objects("Easy", smalltext)
	textRect.center = ( (screen_width * (.25) + (170/2)), (200 + (100/2)))
	screen.blit(textSurface, textRect)
	
	#MEDIUM
	if (screen_width * .25) + 170 > mouse[0] > (screen_width * .25) and (350 + 100) > mouse[1] >  350:
		pygame.draw.rect(screen, darkyellow, ((screen_width * (.25)), (350), 170, 100))
	else:
		pygame.draw.rect(screen, yellow, ((screen_width * (.25)), (350), 170, 100))
	
	smalltext = pygame.font.Font("freesansbold.ttf", 40)
	textSurface, textRect = text_objects("Medium", smalltext)
	textRect.center = ( (screen_width * (.25) + (170/2)), (350 + (100/2)))
	screen.blit(textSurface, textRect)
		
	#HARD
	if (screen_width * .25) + 170 > mouse[0] > (screen_width * .25) and (500 + 100) > mouse[1] > 500:
		pygame.draw.rect(screen, darkred, ((screen_width * (.25)), (500), 170, 100))
	else:
		pygame.draw.rect(screen, red, ((screen_width * (.25)), (500), 170, 100))
	
	smalltext = pygame.font.Font("freesansbold.ttf", 40)
	textSurface, textRect = text_objects("Hard", smalltext)
	textRect.center = ( (screen_width * (.25) + (170/2)), (500 + (100/2)))
	screen.blit(textSurface, textRect)
	
	#QUIT
	if (screen_width * .25) + 170 > mouse[0] > (screen_width * .25) and (650 + 100) > mouse[1] > 650:
		pygame.draw.rect(screen, darkblue, ((screen_width * (.25)), (650), 170, 100))
	else:
		pygame.draw.rect(screen, blue, ((screen_width * (.25)), (650), 170, 100))

	smalltext = pygame.font.Font("freesansbold.ttf", 40)
	textSurface, textRect = text_objects("Quit", smalltext)
	textRect.center = ( (screen_width * (.25) + (170/2)), (650 + (100/2)))
	screen.blit(textSurface, textRect)
	
	pygame.display.update()
	
	if 360 < pygame.mouse.get_pos()[0] < 360+170 and 200 < pygame.mouse.get_pos()[1] < 300:
		mode = "easy"
		running = False
		return mode
		
	#Medium
	elif 360 < pygame.mouse.get_pos()[0] < 360+170 and 350 < pygame.mouse.get_pos()[1] < 450:
		mode = "medium"
		running = False
		return mode
		
	#Hard
	elif 360 < pygame.mouse.get_pos()[0] < 360+170 and 500 < pygame.mouse.get_pos()[1] < 600: 
		mode = "hard"
		running = False
		return mode
		
	#Quit
	elif 360 < pygame.mouse.get_pos()[0] < 360+170 and 650 < pygame.mouse.get_pos()[1] < 750:
		pygame.quit()


def introScreen():
	#Allows users to exit the Intro Screen
	intro = True
	while intro == True:
		for event in pygame.event.get():
			
			if event.type == pygame.QUIT:
				pygame.quit()
				
		screen.fill(white)
		largeText = pygame.font.Font("freesansbold.ttf", 110)
		textSurface, textRect = text_objects("Hangman", largeText)
		textRect.center = ((screen_width/2), (screen_height - 800))
		screen.blit(textSurface, textRect)
		
		completedhangman()
		
		mode = gameDifficulty()
		return mode
		
def game(wordlist, running):
	screen.fill(white)
	pygame.event.set_blocked(MOUSEBUTTONDOWN)
	pygame.display.update()
	
	word = random.choice(wordlist)

	tries = 9
	
	running = True

	keyPressed = " "
	
	wordBank = [ ]
	emptyList = [ ]
	for x in range(len(word)):
		emptyList.append("_ ")
	
	Hidden = Font.render("".join(emptyList), True, black)
	HiddenRect = Hidden.get_rect()
	HiddenRect.center = (350, 250)
	screen.blit(Hidden,HiddenRect)
	
	while running == True:
		
		inbank = False
		
		status = " "
		greyhangman()
		hangman(tries, status)
	
		
		for event in pygame.event.get():
			
			if (event.type == QUIT):
				running = False
				pygame.quit()

			elif event.type == KEYDOWN:
				pygame.draw.rect(screen, white, (200, 500, 800, 300))
				keyPressed = event.key
				pygame.draw.rect(screen, white,(220,200,280,100))
				pygame.draw.rect(screen, white, (260,50,200,100)) 
				userInput = event.key
				if re.search("[a-z]",chr(event.key)):
					for x in range(len(wordBank)):
						if wordBank[x] == chr(event.key):
							Input = Font.render("You have already guessed this letter!", True, red)
							InputRect = Input.get_rect()
							InputRect.center = (400, 100)
							screen.blit(Input, InputRect)
							screen.blit(Hidden,HiddenRect)
							inbank = True
						
					if ((chr(event.key).upper() in word) or (chr(event.key).lower() in word)):
						wordBank.append(chr(event.key))
						for x in range(len(word)):
							if ((word[x] == (chr(event.key)).upper()) or (word[x] == (chr(event.key)).lower())):
								emptyList[x] = word[x]
															
					elif inbank != True:
						tries = tries - 1
						wordBank.append(chr(event.key))
						
					Hidden = Font.render("".join(emptyList), True, black)
					HiddenRect = Hidden.get_rect()
					HiddenRect.center = (350, 250)
					screen.blit(Hidden,HiddenRect)
					
				else:
						Input = Font.render("Please enter a letter!", True, red)
						InputRect = Input.get_rect()
						InputRect.center = (400, 100)
						screen.blit(Input, InputRect)
						screen.blit(Hidden,HiddenRect)
				
				
				Input = FontTime.render("Letters guessed:", True, black)
				InputRect = Input.get_rect()
				InputRect.center = (200, 580)
				screen.blit(Input, InputRect)
				screen.blit(Hidden,HiddenRect)
						
				wordBank = list(dict.fromkeys(wordBank))
				wordBankBlit = Font.render(str(wordBank), 1, black)
				screen.blit(wordBankBlit, (200, 620))
							
			elif event.type == KEYUP:
				pygame.draw.rect(screen, white, (0, 50, 1500, 100))
		
		if tries == 0:
			screen.fill(white)
			status = "lose"
			hangman(0, "lose")
			Over = Font.render("You have lost! Game over!", True, red)
			OverRect = Over.get_rect()
			OverRect.center = (500, 220)
			screen.blit(Over,OverRect)
			pygame.display.update()
			
			Word = FontBig.render("The word is:", True, black)
			WordRect = Word.get_rect()
			WordRect.center = (500, 350)
			screen.blit(Word, WordRect)

			Word2 = FontBig.render(word, True, black)
			Word2Rect = Word2.get_rect()
			Word2Rect.center = (500, 400)
			screen.blit(Word2, Word2Rect)
			pygame.display.update()
			
			Restart = FontBig.render("Press R to restart!", True, darkred)
			RestartRect = Restart.get_rect()
			RestartRect.center = (500, 800)
			screen.blit(Restart, RestartRect)
			
			pygame.display.update()
			running = False
			
		if (word == "".join(emptyList)):
			screen.fill(white)
			happyhangman()
			status = "win"
			Congrats = FontBig.render("CONGRATS! You've guessed the word!", True, green)
			CongratsRect = Congrats.get_rect()
			CongratsRect.center = (500, 220)
			screen.blit(Congrats, CongratsRect)
			
			Word = FontBig.render("The word is:", True, black)
			WordRect = Word.get_rect()
			WordRect.center = (500, 350)
			screen.blit(Word, WordRect)

			Word2 = FontBig.render(word, True, black)
			Word2Rect = Word2.get_rect()
			Word2Rect.center = (500, 400)
			screen.blit(Word2, Word2Rect)
			
			Restart = FontBig.render("Press R to restart!", True, darkred)
			RestartRect = Restart.get_rect()
			RestartRect.center = (500, 800)
			screen.blit(Restart, RestartRect)
			
			pygame.display.update()
			running = False	
	
			
def restart():
	pygame.event.set_allowed(MOUSEBUTTONDOWN)
	main()
		
		
def main():
	introScreen()
	running = True
	while running == True:
		for event in pygame.event.get():
			if event.type == QUIT:
				running = False
				pygame.quit()
			elif event.type == MOUSEBUTTONDOWN:
				mode = introScreen()
				if mode == "easy":
					game(easyWords, running)
				elif mode == "medium":
					game(mediumWords, running)
				elif mode == "hard":
					game(hardWords, running)
			if event.type == pygame.KEYDOWN and event.key == K_r:
				restart()
				
					
main()