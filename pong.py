from pygame import *

game = true 
clock = time.Clock()

#класс спрайта
class GameSprite(sprite.Sprite):
    def __init__(self,p_image,p_x,p_y,size_x,size_y,p_speed):
        sprite.Sprite.__init__(self)
        self.image = transform.scale(image.load(p_image),(size_x,size_y))
        self.speed = p_speed
        self.rect = self.image.get_rect()
        self.rect.x = p_x
        self.rect.y = p_y
    def reset(self):
        window.blit(self.image, (self.rect.x,self.rect.y))
#класс Игрока
class Player(GameSprite):
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_W] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_S] and self.rect.y < 520:
            self.rect.y += self.speed

    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 520:
            self.rect.y += self.speed

window = display.set_mode((600,500))
window.fill((200,4,28))

while game:
    for e in event.get():
        if e.type == QIUT:
            game = False
racket1 = Player('',30,200,4,50,150)
racket2 = Player('',520,200,4,50,150)
ball = Player('',200,200,4,50,50)

font.init()
font = font.Font(None,35)
loose1 = font.render("PLAYER 1 LOSE!!!")
loose2 =  font.render("PLAYER 2 LOSE!!!")

if game == True:
    window .fill((200,4,28))
    racket1.update_l()
    racket2.update_r()


while True:
    display.update()
