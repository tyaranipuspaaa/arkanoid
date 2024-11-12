from pygame import*
from random import*
import pygame
font.init()

font1 = font.Font(None, 80) #yg 80 size nya
red = (255, 0, 0) #hitam
green = (0,255,0)
win = font1.render('Congrats!',True, green)
lose = font1.render('You died', True, red)

class Area():
    #characteristict of character
    def __init__(self,filename, x, y, width, height):
        #install from super class
        sprite.Sprite.__init__(self)

        #set the images
        self.image = transform.scale(image.load(filename), (width,height))
        #set the location
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    #method for showing character
    def draw(self):
        screen.blit(self.image, (self.rect.x, self.rect.y))
    
    #agar bisa ngerasain dia di klik mouse / tidak
    def collidepoint(self, x, y):
        return self.rect.collidepoint(x, y) 
    
    #agar bisa ngerasain apakah photo frame nya tabrakan dgn yg lain
    def colliderect(self, rect):
      return self.rect.colliderect(rect)


class Label():

    #method
    #set kalimat, font size, warna font (0,0,0) rgb hitam
    def set_text(self, text, fsize=12, text_color=(0, 0, 0)):
        self.image = pygame.font.SysFont('verdana', fsize).render(text, True, text_color)

    #draw text box ke layar
    def draw(self, shift_x=0, shift_y=0):
        self.fill()
        screen.blit(self.image, (self.rect.x + shift_x, self.rect.y + shift_y))


class Picture(Area):

          #karakteristik -> filename dari photo
    def __init__(self, filename, x=0, y=0, width=10, height=10):
        Area.__init__(self, x=x, y=y, width=width, height=height)
        self.image = pygame.image.load(filename)
    #method -> photo frame + photonya akan digambar ke screen 
    def draw(self):
        screen.blit(self.image, (self.rect.x, self.rect.y))


width = 500
height = 500
screen = display.set_mode((width, height))
  
#set background
#upload background
img_background = "background.jpeg"
background = transform.scale(image.load(img_background), (width,height))

dx = 10
dy = 4
img_platfrom = "platfrom.png"

kec_bola_x, kec_bola_y = 3,3

width_p =50
height_p = 50
platform = Area(img_platfrom, 200,400,width_p, height_p)


ing_bola = "ball.png"
width_b= 50
height_b = 50
ball = Area(ing_bola, 150,100,width_b, height_b)

ing_musuh1 = "enemy1.png"
ing_musuh2 = "enemy2.png"
ing_musuh3 = "enemy3.png"
ing_musuh4 = "enemy4.png"
ing_musuh5 = "enemy5.png"


list_monster = list()
jumlah_musuh1 = randint(1,5)
jumlah_musuh2 = randint(1,5)
jumlah_musuh3 = randint(1,5)
jumlah_musuh4 = randint(1,5)
jumlah_musuh5 = randint(1,5)

width_m = 50
height_m = 50

for i in range(jumlah_musuh1):
    x = randint(10, width-50)
    y = randint(10, 250)
    musuh1 = Area(ing_musuh1, x,y,width_m, height_m)
    list_monster.append(musuh1)

for i in range(jumlah_musuh2):
    x = randint(10, width-50)
    y = randint(10, 250)
    musuh2 = Area(ing_musuh2, x,y,width_m, height_m)
    list_monster.append(musuh2)

for i in range(jumlah_musuh3):
    x = randint(10, width-50)
    y = randint(10, 250)
    musuh3 = Area(ing_musuh3, x,y,width_m, height_m)
    list_monster.append(musuh3)

for i in range(jumlah_musuh4):
    x = randint(10, width-50)
    y = randint(10, 250)
    musuh4 = Area(ing_musuh4, x,y,width_m, height_m)
    list_monster.append(musuh4)

for i in range(jumlah_musuh5):
    x = randint(10, width-50)
    y = randint(10, 250)
    musuh5 = Area(ing_musuh5, x,y,width_m, height_m)
    list_monster.append(musuh5)

kec_bola_x = 2
kec_bola_x = 2

fps = time.Clock()

move_left = False
move_right = False

permainan_dimulai = True
while permainan_dimulai: #selama permainan dimulai
    screen.blit(background, (0,0)) #set background
    platform.draw()
    ball.draw()

    #pengecekan tombol
    for e in event.get():
        #jika pencet tombol silang
        if e.type == QUIT:
            #maka akan quit
            quit()
        if e.type == KEYDOWN:
            if e.key == K_LEFT:
                move_left = True
            if e.key == K_RIGHT:
                move_right = True
        if e.type == KEYUP:
            if e.key == K_LEFT:
                move_left = False
            if e.key == K_RIGHT:
                move_right = False
    if move_left:
        platform.rect. x -= dx
    if move_right:
        platform.rect.x += dx
    ball.rect.x += kec_bola_x
    ball.rect.y += kec_bola_y
    if len(list_monster) <= 0:
        screen.blit(win, (150,150))
        kec_bola_y = 0
        kec_bola_x = 0
        dx = 0

    if ball.rect.y < 0:
        kec_bola_y *= -1

    if ball.rect.x < 0 or ball.rect.x > width-50:
        kec_bola_x *= -1

    if ball.rect.y > 450:
        screen.blit(lose, (150,150))
        kec_bola_y = 0
        kec_bola_x = 0
        dx = 0
    if ball.rect.colliderect(platform.rect):
        kec_bola_y *= -1

    for m in list_monster:
        m.draw()
        if m.rect.colliderect(ball.rect):
            list_monster.remove(m)
            kec_bola_y *= -1

    display.update()
    fps.tick(60)




