import pygame as pg 
import random
pg.init()
win_width, win_height = 900, 550
window = pg.display.set_mode((win_width, win_height))
pg.display.set_caption("PING PONG")
class GameSprite:
    def __init__ (self, image, x, y, width, height, speed):
        self.width = width
        self.height = height
        self.speed = speed
        self.image = pg.transform.scale(pg.image.load(image), (width, height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
class Player(GameSprite):
    def control1(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_s] and self.rect.y < 550 - 100:
            self.rect.y += self.speed
        if keys[pg.K_w] and self.rect.y > 0:
            self.rect.y -= self.speed
    def control2(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_DOWN] and self.rect.y < 550 - 100:
            self.rect.y += self.speed
        if keys[pg.K_UP] and self.rect.y > 0:
            self.rect.y -= self.speed
class Ball(GameSprite):
    def move(self):
        global x2, y2, player1, player2
        self.rect.x += x2
        self.rect.y += y2
        if pg.sprite.collide_rect(player2, self):
            x2 = -3
        if pg.sprite.collide_rect(player1, self):
            x2 = 3
        if self.rect.y < 0:
            y2 = 3
        if self.rect.y > 500:
            y2 = -3
class GameOver(GameSprite):
     def display_winner(self):
        if player1_score >= 5:
            self.image = pg.transform.scale(pg.image.load("image/player2png.png"), (win_width, win_height))
        elif player2_score >= 5:
            self.image = pg.transform.scale(pg.image.load("image/player1png.png"), (win_width, win_height))
        self.reset()
x2, y2 = 3, 3
back = GameSprite("image/background.jpg", 0, 0, 900, 550, 0)
player1 = Player("image/player.png", 10, 215, 30, 120, 7)
player2 = Player("image/player.png", 850, 215, 32, 120, 7)
game_over = GameOver("image/background.jpg", 0, 0, win_width, win_height, 0)
ball = Ball("image/realistic-tennis-ball-isolated-on-white-background_97886-807-removebg-preview.png", 450, 275, 50, 50, 5)
player1_score = 0
player2_score = 0
game = True
while game:
    pg.time.Clock().tick(100)
    for i in pg.event.get():
        if i.type == pg.QUIT:
            exit()
    back.reset()
    player1.reset()
    player1.control1()
    player2.reset()
    player2.control2()
    ball.reset()
    ball.move()
    if ball.rect.x < -50:
        player1_score += 1
        ball.rect.x = 450
        ball.rect.y = 275
        x2 = random.choice([-3, 3])
        y2 = random.choice([-3, 3])
    elif ball.rect.x > win_width:
        player2_score += 1
        ball.rect.x = 450
        ball.rect.y = 275
        x2 = random.choice([-3, 3])
        y2 = random.choice([-3, 3])
    label = pg.font.SysFont('Grand9KCraft', 35).render(f'Miss balls: {player1_score}', True, 'white')
    window.blit(label, (20, 20))
    label2 = pg.font.SysFont('mini_pixel-7.ttf', 35).render(f'Miss balls: {player2_score}', True, 'white')
    window.blit(label2, (725, 20))
    if player1_score >= 5 or player2_score >= 5:
        game_over.display_winner()
        game = False
    pg.display.flip()
while True:
    pg.time.Clock().tick(60)
    for i in pg.event.get():
        if i.type == pg.QUIT:
            exit()
    pg.display.flip()
