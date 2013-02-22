#!/usr/bin/python
#TODO

import pygame
import sys
from pygame.locals import *
import csv
import random

pygame.init()

windowSurface = pygame.display.set_mode((1000, 800),0,32)
pygame.display.set_caption('Mahjong')

basicFont = pygame.font.SysFont(None, 14)

GREEN = (60,179,113)
WHITE = (255,255,255)
BLUE = (0,0,255)
RED = (255,0,0)

windowSurface.fill(GREEN)

pygame.display.flip()

deck=[]
my_deck=[]
my_deck_exposed_tiles=[]
player2_deck=[]
player2_deck_exposed_tiles=[]
player3_deck=[]
player3_deck_exposed_tiles=[]
player4_deck=[]
player4_deck_exposed_tiles=[]
tiles_in_center=[]
unplayed_tiles=[]

gameTurn=0

diceText = basicFont.render('Dice Roll', True, WHITE, BLUE)
diceTextRect = diceText.get_rect()
diceTextRect.centerx = windowSurface.get_rect().centerx
diceTextRect.centery = windowSurface.get_rect().centery

pygame.draw.rect(windowSurface, RED, (diceTextRect.left - 20, diceTextRect.top - 20,diceTextRect.width + 40, diceTextRect.height + 40))

windowSurface.blit(diceText, diceTextRect)
pygame.display.update()

def diceRoll():
    """Roll some dice."""
    result_number = str(dice(2,6))
    starting_number = basicFont.render(result_number, True, WHITE)
    staring_number_rect = starting_number.get_rect()
    starting_number.centerx = windowSurface.get_rect().centerx
    starting_number.centery = windowSurface.get_rect().centery
    pygame.draw.rect(windowSurface, BLUE, (starting_number_rect.left - 30, starting_number_rect.top - 30, starting_number_rect.width + 30, starting_number_rect.height + 30))
    windowSurface.blit(starting_number, starting_number_rect)
    pygame.display.update()

with open('tiledeck.csv', 'rb') as tiledeck:
    tiledeckreader = csv.reader(tiledeck)
    for row in tiledeckreader:
        deck.append(row)

def changeTile():
    """Change the display tile."""
    displaytile = pygame.image.load(deck[random.randint(0,len(deck)-1)][2]).convert_alpha()
    windowSurface.blit(displaytile, (444,444))
    pygame.display.flip()

def dice(num, sides):
    return reduce(lambda x,y,s=sides:x +random.randrange(s),
            range(num+1))+num

while True:
    for event in pygame.event.get():
        if event.type == MOUSEBUTTONUP:
            changeTile()
            diceRoll()

        if event.type == QUIT:
            pygame.quit()
            sys.exit()

#if __name__ == '__main__': StartGame.main()
