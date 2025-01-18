#Create your own ping pong
from pygame import *
from random import randint
from time import time as timer


window_width = 700 
window_height = 500
window = display.set_mode((window_width, window_height))
display.set_caption("Ping Pong Game")
background = (200,255,255)
window.fill(background)

run = True
FPS = 60
clock = time.Clock()

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_right(self):
        keys_pressed = key.get_pressed()

        if keys_pressed[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys_pressed[K_DOWN] and self.rect.y < window_height - 80:
            self.rect.y += self.speed
    
    def update_left(self):
        keys_pressed = key.get_pressed()

        if keys_pressed[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys_pressed[K_s] and self.rect.y < window_height - 80:
            self.rect.y += self.speed
        
racket1 = Player('racket.png', 30, 200, 50, 150, 4)
racket2 = Player('racket.png', 620, 200, 50, 150, 4)
ball = GameSprite('ball.png', 200, 200, 50, 50,4 )

font.init()
font1 = font.SysFont("Arial",50)

lose1 = font1.render("PLAYER 1 LOSES!PRESS R TO RESTART", True, (200, 0, 0))
lose2 = font1.render("PLAYER 2 LOSES!PRESS R TO RESTART", True, (200, 0, 0))

finish = False
speed_x = 3 
speed_y = 3

while run:
    for e in event.get():
        if e.type == QUIT:
            run = False
        if e.type == KEYDOWN:
            if e.key == K_r:
                finish = False
                racket1.rect.x = 30
                racket1.rect.y = 200
                racket2.rect.x = 620
                racket2.rect.y = 200
                ball.rect.x = 200
                ball.rect.y = 200
                
    sprite.collide_rect(ball,racket1)

    if finish == False:
        window.fill(background)
        ball.reset()
        racket1.reset()
        racket2.reset()
        racket1.update_left()
        racket2.update_right()
        ball.rect.x += speed_x
        ball.rect.y += speed_y
        if sprite.collide_rect(ball, racket1) or sprite.collide_rect(ball, racket2):
            speed_x *= -1
            speed_y *= 1
        if ball.rect.y < 0 or ball.rect.y > window_height - 50:
            speed_y *= -1
            speed_x *= 1

        if ball.rect.x < racket1.rect.x:
            window.blit(lose1,(200,200))
            finish = True

        if ball.rect.x > racket2.rect.x + 20:
            window.blit(lose2,(200,200))
            finish = True



    display.update()
    clock.tick(FPS)
    