from pygame import *

window  = display.set_mode((600,600))
display.set_caption('Шедевр!')
back = (255,255,255)
window.fill(back)

clock = time.Clock()
game = True
finish = False
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y,coord_x,coord_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (coord_x,coord_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.coord_x = coord_x
        self.coord_y = coord_y
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image,(self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_1(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys_pressed[K_DOWN] and self.rect.y < 430:
            self.rect.y += self.speed
    def update_2(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys_pressed[K_s] and self.rect.y < 430:
            self.rect.y += self.speed

ball = GameSprite('ball.png', 100,100,100,100,5)
raket_left = Player('raketblue.png',33,50,17,170,4)
raket_right = Player('raketred.png',550,50,17,170,4)

while game:   
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish != True:
        window.fill(back)
    raket_left.reset()
    raket_right.reset()
    ball.reset()
    raket_left.reset()
    raket_left.update_2()
    raket_right.update_1()
    display.update()
    clock.tick(60)
