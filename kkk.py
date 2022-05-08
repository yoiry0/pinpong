from pygame import *


window = display.set_mode((700,500))
display.set_caption('Ping-Pong')
background = transform.scale(image.load("fon.jpg") , (700,500))

font.init()
font = font.Font( None , 36)

lose1 = font.render("player 1 lose" , True, (255 ,255 ,255))
lose2 = font.render("player 2 lose" , True , (255,255,255))

class GameSprite(sprite.Sprite):
    def __init__(self, player_image , player_x , player_y ,player_widht , player_height , player_speed):
        super().__init__()
        self.image =  transform.scale(image.load(player_image) , (player_widht , player_height))
        self.rect = self.image.get_rect()
        self.rect.x =  player_x
        self.rect.y = player_y
        self.speed = player_speed
    def recet(self):
        window.blit(self.image,(self.rect.x, self.rect.y))


class Player2(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()

        if keys_pressed[K_DOWN] and self.rect.y <350:
            self.rect.y+=self.speed

        if keys_pressed[K_UP]and self.rect.y >0:
            self.rect.y-=self.speed  


class Player(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()

        if keys_pressed[K_s] and self.rect.y< 350:
            self.rect.y+=self.speed

        if keys_pressed[K_w] and self.rect.y>0:
            self.rect.y-=self.speed  


player = Player("steni.jpg" , 20 ,170,30 , 150 , 2)
player2 = Player2("steni.jpg" , 650,170 , 30 , 150 , 2)
ball = GameSprite("ball.png" , 300 ,400 ,40 , 40 , 15)

clock = time.Clock()
FPS = 60
finish = False
game = True

speed_x = 3 
speed_y = 3

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    window.blit(background, (0, 0))     
    if finish != True:
        window.blit(background, (0, 0))
        player.recet()
        player.update()
        player2.update()
        player2.recet()   
        ball.recet()
        
        ball.rect.x += speed_x
        ball.rect.y += speed_y
    if ball.rect.y > 500-50 or ball.rect.y <0:
        speed_y *=-1

    if sprite.collide_rect(player , ball) or sprite.collide_rect(player2 , ball):
        speed_x *= -1

    if ball.rect.y== 450:
        window.blit(lose1 , (200 , 200))
        finish = True
    
    if ball.rect.y == 0:
        windoe.blit(lose2 , (200 , 200))
        finish = True
    window.blit(background, (0, 0))
    player.recet()
    player.update()
    player2.update()
    player2.recet()   
    ball.recet()

    display.update()
        

    
