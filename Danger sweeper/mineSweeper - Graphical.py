#center screen
import pygame
import time
import random
import os

#put under imports
os.environ['SDL_VIDEO_CENTERED'] = '1'

class Tile():
    """Tile class. each square is a Tile"""
    def __init__(self, x, y, rand):
        """constructor"""
        #self.color = blue
        self.size = ( 40,40 )
        self.mine = False
        self.potential = None
        self.discovered = False
        self.x = x
        self.y = y
        self.danger = 0
        self.clicked = False
        self.img = None
        self.flagged = False
        self.flag = None
        if rand:
            self.base = dirt
        else:
            self.base = grass


    def discover(self):
        """called if selector is over Tile"""
        if not self.discovered:
            #self.color = self.potential
            self.discovered = True
            if self.potential != "GREEN":
                self.flagged = True
                if self.potential == "RED":
                    self.img = flagRED
                elif self.potential == "ORANGE":
                    self.img = flagORGANGE
                elif self.potential == "YELLOW":
                    self.img = flagYELLOW
            if self.potential == "BOMB":
                self.img = flagBOMB

    def defineColor(self, board):
        """generates the color (and consequently the 'safety') of the tile"""
        if( not self.mine ): #not a mine
            if( self.danger == 0 ):
                self.potential = "GREEN"
            if( self.danger == 1 ):
                self.potential = "YELLOW"
            if( self.danger == 2 ):
                self.potential = "ORANGE"
            if( self.danger >= 3 ):
                self.potential = "RED"
        else:
            self.potential = "BOMB"

    def scanNeighboors(self, board):
        """scans over neighboors of bombs"""

        for x in range(0, 2):
            for y in range(0, 2):
                tmpx = x-1
                tmpx = self.x+tmpx
                tmpy = y-1
                tmpy = self.y+tmpy

                board[tmpx][tmpy].danger += 1

    def forceSafety(self, board):
        """forces neighboors of start/finish to be safe"""
        for x in range(0, 1):
            for y in range(0, 1):
                tmpx = x-1
                tmpx = self.x+tmpx
                tmpy = y-1
                tmpy = self.y+tmpy

                board[tmpx][tmpy].danger = 0

    def showBomb(self):
        pygame.draw.circle(screen, black, (self.x*40+20 , self.y*40+20), 10)
        pygame.draw.circle(screen, white, (self.x*40+20 , self.y*40+20), 5)


    def draw(self, screen, x, y, pressed):
        #pygame.draw.rect( screen, self.color, (self.x*40,self.y*40,40,40) )
        screen.blit(self.base, (self.x*40, self.y*40))
        if self.flagged:# and not self.mine:
            screen.blit(self.img, (self.x*40, self.y*40))
        if pressed[pygame.K_LSHIFT] and self.mine:
            self.showBomb()


            screen.blit
#        if self.clicked:
#            pygame.draw.line(screen, red, (self.x*40+4, self.y*40+4), (self.x*40+40-4, self.y*40+40-4), 5)
#            pygame.draw.line(screen, red, (self.x*40+40-4, self.y*40-4), (self.x*40+4, self.y*40+40+4), 5)

    def clickCheck(self, mx, my):
        if (self.x*40 < mx < self.x*40+40) and (self.y*40 < my < self.y*40+40):
            if not self.clicked:
                while(mousepress):
                   self.clicked = True
            else:
                while(mousepress):
                    self.clicked = False

    def showbomb(self):
        pygame.draw.circle(screen, black, (self.x*40+20 , self.y*40+20), 10)
        pygame.draw.circle(screen, white, (self.x*40+20 , self.y*40+20), 5)



class Selector():
    def __init__(self, startPos):
        self.x = startPos[0]
        self.y = startPos[1]
        self.face ="S"
        self.row = 0
        self.col = 0
        self.phase = 0

    def update(self, pressed):
        #event buffering
#        if pressed[pygame.K_UP]:
#            self.y-=1
#        if pressed[pygame.K_DOWN]:
#            self.y+=1
#        if pressed[pygame.K_LEFT]:
#            self.x-=1
#        if pressed[pygame.K_RIGHT]:
#            self.x+=1

        #event polling
        if pressed == pygame.K_RIGHT:
            self.x+=1
            self.face = "E"
            self.row = 3
        elif pressed == pygame.K_LEFT:
            self.x-=1
            self.face = "W"
            self.row = 2
        elif pressed == pygame.K_UP:
            self.y-=1
            self.face = "N"
            self.row = 1
        elif pressed == pygame.K_DOWN:
            self.y+=1
            self.face = "S"
            self.row = 0

        if(self.y < 0):
            self.y = 0
        if(self.y > 14):
            self.y = 14
        if(self.x < 0):
            self.x = 0
        if(self.x > 19):
            self.x = 19

    def drawSprite(self, screen):
        #24x32 person

        screen.blit(hero, (self.x*40+5, self.y*40+2), (self.col, self.row*32, 24, 32))

        self.phase +=1         # a delay because time not implemented
        if self.phase > 10:
            self.col +=24
            self.phase = 0
            if self.col >= 192:
                self.col = 0


    def draw(self, screen):
        self.drawSprite(screen)
        #pygame.draw.rect(screen, red, (self.x*40, self.y*40, 40,40), 1)

def makeBombs(difficulty, board):
    i = 0
    NUM = 5
    while( i < NUM*difficulty ):
        randRow = random.randint(0, len(board)-1)
        randCol = random.randint(0, len(board[randRow])-1)
        already = board[randRow][randCol].mine
        board[randRow][randCol].mine = True

        if not already:
            if randRow != 0:
                if randCol != 0:
                    board[randRow-1][randCol-1].danger +=1
                board[randRow-1][randCol].danger +=1
                if randCol != 14:
                    board[randRow-1][randCol+1].danger +=1
            if randCol != 0:
                board[randRow][randCol-1].danger +=1
            board[randRow][randCol].danger +=1
            if randCol != 14:
                board[randRow][randCol+1].danger +=1

            if randRow != 19:
                if randCol != 0:
                    board[randRow+1][randCol-1].danger +=1
                board[randRow+1][randCol].danger +=1
                if randCol != 14:
                    board[randRow+1][randCol+1].danger +=1

        i+=1
    print("bombs made")

def fillBoard(board):
    for x in range(0, 20):
        tmp = []
        for y in range(0, 15):
            rand = random.randint(0,1)
            tmp.append(Tile(x,y,rand))
        board.append(tmp)
    print("board filled")

def make_screen():
    """creates the code for a new screen"""
    return pygame.display.set_mode((800,600))

def grid_overlay(screen):
    """draw a grid over the screen, each square is a tile size"""
    i=0
    while(i < screen.get_width()):
        pygame.draw.line(screen, black, (i, 0), (i, screen.get_height()))
        i+=40

    i=0
    while(i<screen.get_height()):
        pygame.draw.line(screen, black, (0,i), (screen.get_width(), i))
        i+=40

#initialize
pygame.display.init()
pygame.font.init()
pygame.mixer.init()

#screen variables
screen= make_screen()
title = False

#clock
clock = pygame.time.Clock()
dt = 1.0

#colors
red    = (255,0,0)
orange = (255,200,50)
yellow = (255,255,0)
green  = (0,255,0)
blue   = (0,0,255)
purple = (128,0,128)
white  = (255,255,255)
black  = (0,0,0)

#fonts
fontobj= pygame.font.SysFont("Times New Roman", 20, True)
fonttitle= pygame.font.SysFont("Times New Roman", 70, True)

#sounds
#squee = pygame.mixer.Sound("sqeek.ogg")
boom = pygame.mixer.Sound("media/bomb.ogg")
pygame.mixer.music.load("media/run.ogg")
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.2)

#images
dirt = pygame.image.load("media/dirt.png")
grass = pygame.image.load("media/grass.png")
#umbrellas modified from - http://media.smashingmagazine.com/images/css-sprites/pokemon.gif
flagRED = pygame.image.load("media/flagRED.png")
flagORGANGE = pygame.image.load("media/flagORANGE.png")
flagYELLOW = pygame.image.load("media/flagYELLOW.png")
flagBOMB = pygame.image.load("media/flagBOMB.png")
hero = pygame.image.load("media/walk.png")

#other variables
running = True
done = False

difficulty = 1  #starting difficulty

start = [0,0]
end = [19,14]

bomblist = []

while not done:
    board = []
    selector = Selector(start)

    fillBoard(board)
    makeBombs(difficulty, board)

    board[start[0]][start[1]].mine = False
    board[start[0]][start[1]].forceSafety(board)
    #----- something wrong might be here
    board[end[0]][end[1]].mine = False
    board[end[0]][end[1]].forceSafety(board)
    #-----

    #finds danger of Tiles and fills bombList
    for x in range(len(board)):
        for y in range(len(board[x])):
            if board[x][y].mine:
                bomblist.append(board[x][y])
            board[x][y].defineColor(board)

    #first 2 are free ;)
    board[selector.x+1][selector.y].discover()
    board[selector.x][selector.y+1].discover()


    running = True

    while running:
        #events
        #place inside game loop
        pygame.event.pump()
        elist = pygame.event.get()
        pressed= pygame.key.get_pressed()
        mousepress = pygame.mouse.get_pressed()
        mx, my = pygame.mouse.get_pos()

        #press space to reset
        if pressed[pygame.K_SPACE]:
            running = False

        #press escape to exit or hit Close
        for e in elist:
            if e.type == pygame.QUIT:
                pygame.mixer.Sound.play(boom)
                running = False
                done = True
            elif e.type == pygame.KEYDOWN:
                if e.key == pygame.K_ESCAPE:
                    pygame.mixer.Sound.play(boom)
                    running = False
                    done = True
#                elif e.type == pygame.K_MOUSEBUTTONDOWN:
#                    board[x][y].clickCheck(mx, my)
                else:
                     selector.update(e.key)


        #selector
        #selector.update(pressed)

        #print( "discovering board["+str(selector.x)+"]["+str(selector.y)+"] - color = "+ str(board[selector.x][selector.y].color ))
        board[selector.x][selector.y].discover()


        #boom when explode
        if board[selector.x][selector.y].mine:
            pygame.mixer.Sound.play(boom)
            running = False
            for x in range(len(board)):
                for y in range(len(board[x])):
                    if board[x][y].mine:
                        board[x][y].showbomb()
            pygame.display.flip()
            time.sleep(.7)
        #you beat the level!!!
        if board[selector.x][selector.y] == board[end[0]][end[1]]:
            running = False
            difficulty +=1
#        if( mousepress[0] ):
#            for x in range(len(board)):
#                for y in range(len(board[x])):
#                    board[x][y].clickCheck(mx, my, mousepress)

        #draw screen
        #screen.fill(white)

        #place tiles onto screen
        for x in range(len(board)):
            for y in range(len(board[x])):
                board[x][y].draw(screen, x, y, pressed)
        #grid_overlay(screen)

        #forces corner to ALWAYS be purple
        #board[start[0]][start[1]].color = purple
        #board[end[0]][end[1]].color = purple


        #draws the current level top left. next level bottom right
        currDiff = fontobj.render(str(difficulty), False, white)
        screen.blit(currDiff, (0,0))
        nextDiff = fontobj.render(str(difficulty+1), False, white)
        screen.blit(nextDiff, (765, 560))
        #pygame.draw.circle(screen, yellow, (end[0]*40+20,end[1]*40+20), 10)

        selector.draw(screen)
        pygame.display.flip()



#enders
pygame.mixer.music.stop()
pygame.display.quit()
