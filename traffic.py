# importing pygame, make sure to download pygame
# Goto CMD, --> pip install pygame(Run as administrator)

import pygame

pygame.init()

# make the window
SIDE = 500
win = pygame.display.set_mode((SIDE, SIDE))
pygame.display.set_caption("Traffic Light!!")

white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
yellow = (255, 255, 0)
black = (0, 0, 0)

red_visible = False
green_visible = False
yellow_visible = False
reset = False

# make a font
FONT = pygame.font.SysFont('comicsans', 30)
clock = pygame.time.Clock()
run = True

# load images
images = []
for i in range(1, 5):
    image = pygame.image.load("bg" + str(i) + ".png")
    images.append(image)

# make redraw() func
# top left hand corner is this 0,0
# when you move down y cordinate increase, x is towards right


def drawWindow():
    win.blit(images[0], (0, 0))

    if red_visible:
        win.blit(images[1], (0, 0))
        text = FONT.render("STOP!", 1, red)
        win.blit(text, (SIDE/2 - text.get_width()/2, 450))

    if yellow_visible:
        win.blit(images[2], (0, 0))
        text = FONT.render("Prepare", 1, black)
        win.blit(text, (SIDE/2 - text.get_width()/2, 450))

    if green_visible:
        win.blit(images[3], (0, 0))
        text = FONT.render("Lets GO!", 1, green)
        win.blit(text, (SIDE/2 - text.get_width()/2, 450))

    if reset:
        text = FONT.render("All lights reset!", 1, black)
        win.blit(text, (SIDE/2 - text.get_width()/2, 450))

    text = FONT.render("DIY Traffic Lights", 1, black)
    win.blit(text, (SIDE/2 - text.get_width()/2, 20))

    pygame.display.update()


while run:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                red_visible = True
                yellow_visible = False
                green_visible = False
                reset = False

            if event.key == pygame.K_s:
                red_visible = False
                yellow_visible = True
                green_visible = False
                reset = False

            if event.key == pygame.K_d:
                red_visible = False
                yellow_visible = False
                green_visible = True
                reset = False

            if event.key == pygame.K_w:
                red_visible = False
                yellow_visible = False
                green_visible = False
                reset = True
    drawWindow()

pygame.quit()
