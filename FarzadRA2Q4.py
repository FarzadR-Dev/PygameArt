# P.Conc., A2 Q4
# Farzad Rahman
# Truman98 - ICS
# March 4, 2020
# ICS3UI - 03, Ms. Harris
# Modifications: All done on same day as start

# Tree image link: https://ya-webdesign.com/image/yggdrasil-vector/2117824.html
# Picnic table link: https://www.top5reviewed.com/picnic-tables/


# Setup
import pygame #Imports library for access to its assets
pygame.init() # Initializes all the modules
screen = pygame.display.set_mode((600, 600)) # Sets screen with given display size
done = False # to make program keep the image to stay until exited


# Images used, sources in intro at top
tree = pygame.image.load('tree.png')
table = pygame.image.load('table.png')


# Colors used
Backcolour = pygame.color.Color('#E17210') # This uses a color code rather than RGB
green = (46, 164, 74)
brown = (105, 54, 19)
grey = (114, 114, 114)
red = (186, 9, 9)
suncolor = (220, 59, 10)


screen.fill(Backcolour) # Sets sky color


pygame.draw.circle(screen, suncolor, (300,400), 200) # The Sunset


def Grass(): # Landscape function
    grass = pygame.draw # So I do not have to retype it over and over
    grass.circle(screen, green,(240,600),200) # One Hill
    grass.circle(screen, green, (130,650), 300) # Another Hill
    grass.ellipse(screen, green, (230,380,500,300)) # Last Hill
Grass() # Fuction called so it actually happens


def Props(): # For all the props in this program
    props = pygame.draw
    screen.blit(table,(245,445)) # Image of a table
    props.rect(screen, grey, (100, 300, 110,70)) # Some kind of outdoor shelter
    props.polygon(screen, red, ((80,300),(205,270),(235,300))) # Roof
Props() #Function called



def plant(): # A single Tree
    screen.blit(tree,(400,180)) # Image of tree
plant() # Function called


while not done:         # This chunk keeps the program from closing itself
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
    pygame.display.flip()