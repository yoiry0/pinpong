from pygame import *


window = display.set_mode((700,500))
display.set_caption('Ping-Pong')

background = transform.scale(image.load("platform.png") , (700,500))
clock = time.Clock()
FPS = 60 
game = True
finish = False
while game:

    window.blit(background, (0, 0))
    display.update()
    clock.tick(FPS)