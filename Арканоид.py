import pygame
size = width, height = (640, 480)
screen = pygame.display.set_mode(size)
fpsClock = pygame.time.Clock()
pygame.init()

#БЛОК
class Block():
    def __init__(self, x, y, w, h, visible, color):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.visible = visible
        self.color = color
    
    def draw(self):
        if self.visible:
            pygame.draw.rect(screen, self.color, (self.x, self.y, self.w, self.h), 0)        

#ПЛАТФОРМА
class Platform():
    def __init__(self, x, y, w, h, speed):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.speed = speed
    
    def draw(self):
        pygame.draw.rect(screen, (0, 0, 0), (self.x, self.y, self.w, self.h), 0)        

#ШАРИК
class Ball():
    def __init__(self, x, y, r, vx, vy):
        self.x = x
        self.y = y
        self.r = r
        self.vx = vx
        self.vy = vy
    
    def draw(self):
        pygame.draw.circle(screen, 'red', (self.x, self.y), self.r, 0)        

def drawText(stroka, dy, size_font):
    font = pygame.font.SysFont('timesnewroman', size_font, bold = True, italic = False)
    text = font.render(stroka, 0, (255, 0, 0))
    dx = width//2 - text.get_width()//2
    screen.blit(text, (dx, dy))  

blocks_list = []
#Создание блоков
def creatBlocks(level):
    drawText("Уровень " + str(level), 0, 10)
    color_list = ['red', 'orange', 'yellow', 'green', 'cyan', 'blue', 'violet', 'pink']
    if level == 1:
        num_color = 0
        for x in range(50, 600, 70):
            blocks_list.append(Block(x, 20, 60, 30, True, color_list[num_color]))
            num_color += 1
        
        num_color = 0    
        for x in range(80, 600-70, 70):
            blocks_list.append(Block(x, 60, 60, 30, True, color_list[num_color]))
            num_color += 1 
            
        num_color = 0
        for x in range(50, 600, 70):
            blocks_list.append(Block(x, 100, 60, 30, True, color_list[num_color]))
            num_color += 1    

    if level == 2:
        num_color = 0
        for x in range(50, 600, 70):
            blocks_list.append(Block(x, 200, 60, 30, True, color_list[num_color]))
            num_color += 1        

#Создание игрока
gamer = Platform(300, 450, 100, 10, 25)

#Создание шарика
ball = Ball(350, 440, 10, 0, 0)

n = 23
level = 1
fall = False
creatBlocks(level)
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            
        keyboard = pygame.key.get_pressed()
        buttons_mouse = pygame.mouse.get_pressed()
        pos_mouse = pygame.mouse.get_pos() 
        
        #Управление Платформой
        if keyboard[pygame.K_LEFT]:
            gamer.x -= gamer.speed
        if keyboard[pygame.K_RIGHT]:
            gamer.x += gamer.speed 
        #Запуск шарика
        if keyboard[pygame.K_SPACE]:
            ball.vx=3
            ball.vy=-3
            fall = True
    
    screen.fill('White')
    #Рисование блоков
    for i in range(len(blocks_list)):
        blocks_list[i].draw()
     
    #Рисование игрока   
    gamer.draw()
 
    #Рисование шарика   
    ball.draw() 
    if fall:
        ball.x+=ball.vx
        ball.y+=ball.vy 
    else:
        ball.x = gamer.x+gamer.w/2  
    
    #Условие проигрыша
    if ball.y+ball.r>height:
        ball.vy=0        
        ball.vx=0        
    
    #Условие отскока от верхней границы
    if ball.y-ball.r<0:
        ball.vy=-ball.vy    
    
    #Условие отскока от боковых границ
    if ball.x+ball.r>width or ball.x-ball.r<0:
        ball.vx=-ball.vx  
        
    #Условие отскока от платформы
    if ball.x+ball.r>gamer.x and ball.x-ball.r<gamer.x+gamer.w and ball.y+ball.r>gamer.y and ball.y-ball.r<gamer.y+gamer.h:
        ball.vy=-ball.vy    
    
    #Условие столкновения с блоками
    for i in range(len(blocks_list)):    
        if ball.x+ball.r>blocks_list[i].x and ball.x-ball.r<blocks_list[i].x+blocks_list[i].w and ball.y+ball.r>blocks_list[i].y and ball.y-ball.r<blocks_list[i].y+blocks_list[i].h and blocks_list[i].visible==True:
            ball.vy=-ball.vy
            blocks_list[i].visible=False
            n-=1
    if n==0:
        n=8
        drawText("Уровень пройден", 300, 30)
        ball.x = gamer.x+gamer.w/2
        ball.y = 440
        ball.vy=0        
        ball.vx=0
        level=2
        creatBlocks(level)
        
    
    pygame.display.flip()
    fpsClock.tick(60)
pygame.quit()