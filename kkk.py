from pygame import *


window = display.set_mode((700,500))
display.set_caption('Ping-Pong')
background = transform.scale(image.load("fon.jpg") , (700,500))

font.init()
font = font.Font( None , 50)


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
ball = GameSprite("ball.jpg" , 300 ,400 ,40 , 40 , 15)

clock = time.Clock()
FPS = 60
finish = False
game = True

speed_x = 3 
speed_y = 3
pl1 = 0
pl2 = 0    
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

   
    play1= font.render( str(pl2) + ":" , True ,(255 ,255 ,255))
    play2 = font.render( str(pl1), True ,(255 ,255 ,255))
    window.blit(play1 , (320, 50))
    window.blit(play2 , (350, 50))
    lose1 = font.render("player 1 lose" , True, (255 ,215 ,0))
    lose2 = font.render("player 2 lose" , True , (255,215,0))

    if ball.rect.x >= 700:
        pl1 = pl1 + 1 
        ball.rect.x == 300
        ball.rect.y == 200
        game = True
    if ball.rect.x <=0:
        pl2 = pl2 + 1
        ball.rect.x = 300 
        ball.rect.y = 200
        game = True 
    if pl1 >= 5:
        window.blit(lose1 (300,400))
        finish = True
    if pl2 >= 5:
        window.blit(lose2 ,(300 ,400))
        finish = True
    player.recet()
    player.update()
    player2.update()
    player2.recet()   
    ball.recet()

    display.update()
        

    
