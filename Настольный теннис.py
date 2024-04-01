import pygame
size = width, height = (640, 480)
screen = pygame.display.set_mode(size)
fps = pygame.time.Clock()
pygame.init()
font = pygame.font.SysFont(None, 30)

#Процедура рисования кнопки меню
def drawButton(x_button, y_button, width_button, height_button, stroka):
    color = pygame.Color(50, 150, 150)
    pygame.draw.rect(screen, color, (x_button+3, y_button+3, width_button, height_button), 0)
    hsv = color.hsva
    color.hsva = (hsv[0], hsv[1], hsv[2]+30, hsv[3])
    pygame.draw.rect(screen, color, (x_button, y_button, width_button, height_button), 0)
    color.hsva = (hsv[0], hsv[1], hsv[2], hsv[3])
    pygame.draw.rect(screen, color, (x_button, y_button, width_button, height_button), 3)    
    font = pygame.font.SysFont('timesnewroman', 30, bold = True, italic = False)
    text = font.render(stroka, 0, (255, 0, 0))
    dx = width_button//2 - text.get_width()//2
    dy = height_button//2 - text.get_height()//2
    screen.blit(text, (x_button + dx, y_button + dy)) 

#Функция нажания кнопки меню
def clickButton(dy):
    return pos_mouse[0]>x_button and pos_mouse[0]<x_button+width_button and pos_mouse[1]>y_button+dy and pos_mouse[1]<y_button+dy+height_button and buttons_mouse[0]

#Процедура рисования строки текста справки        
def drawText(stroka, dy, size_font):
    font = pygame.font.SysFont('timesnewroman', size_font, bold = True, italic = False)
    text = font.render(stroka, 0, (255, 0, 0))
    dx = width//2 - text.get_width()//2
    screen.blit(text, (dx, dy))       

#Переменные шарика
x=320
y=240
r=10
vx=3
vy=3
#Переменные игроков
#Правый игрок
br_x=500
br_y=200
br_w=10
br_h=100
score_r = 0
b_speed=5   #Скорость перемещения игроков
#Левый игрок
bl_x=100
bl_y=200
bl_w=10
bl_h=100
score_l = 0
#Переменные кнопок
width_button = 200
height_button = 50
x_button = width//2 - width_button//2
y_button = 200
dy_button1 = 0
dy_button2 = 100
dy_button3 = 200
#переменные страниц меню
PAGE = 'menu'
color_bg = 'White'
#Игровой цикл
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        
        keyboard = pygame.key.get_pressed()
        buttons_mouse = pygame.mouse.get_pressed()
        pos_mouse = pygame.mouse.get_pos()        
        #Управление игроками
        if keyboard[pygame.K_o]:
            br_y -= b_speed
        if keyboard[pygame.K_l]:
            br_y += b_speed
        if keyboard[pygame.K_w]:
            bl_y -= b_speed
        if keyboard[pygame.K_s]:
            bl_y += b_speed
        
    screen.fill(color_bg)
    #Страница Меню
    if PAGE == 'menu':        
        drawButton(x_button, y_button+dy_button1, width_button, height_button, 'Начало')
        drawButton(x_button, y_button+dy_button2, width_button, height_button, 'Правила')
        drawButton(x_button, y_button+dy_button3, width_button,height_button, 'Выход')    

        if clickButton(dy_button1):    
            PAGE = 'game'  
        if clickButton(dy_button2):    
            PAGE = 'help'
        if clickButton(dy_button3):    
            PAGE = 'exit'        
    #Страница Справки
    if PAGE == 'help':
        color_bg = 'Yellow'

        if keyboard[pygame.K_ESCAPE]:
            PAGE = 'menu'
            color_bg = 'White'
        
        drawText("Правила игры", 50, 30) 
        drawText("Управление игроками", 100, 20)
        drawText("Левый - Игрок 1 - 'W' - верх, 'S' - вниз", 130, 20)
        drawText("Правый - Игрок 2 - 'O' - верх, 'L' - вниз", 150, 20)
        drawText("Игра ведется до 11 очков", 300, 20)
        drawText("Выход в меню - 'ESC'", 450, 22)
    #Выход    
    if PAGE == 'exit':
        run = False
    #Страница игры
    if PAGE == 'game':
        
        if keyboard[pygame.K_ESCAPE]:
            PAGE = 'menu'
        #Шарик
        pygame.draw.circle(screen, 'red', (x, y), r, 3)
        x+=vx
        y+=vy
        #Условия гола
        if x+r>740:
            score_r += 1
            x=150
            y=240  
        if x-r<-100:
            score_l += 1 
            x=450
            y=240        
        #Условие отскока шарика от горизонтальных границ
        if y+r>480 or y-r<0:
            vy=-vy
        #Игрок правый
        pygame.draw.rect(screen, 'black', (br_x, br_y, br_w, br_h), 0)
        #Условие отскока шарика от правого игрока
        if x+r>br_x and x-r<br_x+br_w and y+r>br_y and y-r<br_y+br_h:
            vx=-vx
        #Игрок левый
        pygame.draw.rect(screen, 'black', (bl_x, bl_y, bl_w, bl_h), 0)
        #Условие отскока шарика от левого игрока
        if x+r>bl_x and x-r<bl_x+bl_w and y+r>bl_y and y-r<bl_y+bl_h:
            vx=-vx    
    
        text_l = font.render("Игрок 1", False, (0, 0, 0))
        text_r = font.render("Игрок 2", False, (0, 0, 0))
        screen.blit(text_l, (70, 0))
        screen.blit(text_r, (470, 0))    
        text_l = font.render(str(score_l), True, (255, 0, 0))
        text_r = font.render(str(score_r), True, (255, 0, 0))
        screen.blit(text_l, (100, 30))
        screen.blit(text_r, (500, 30))
        #Условия победы
        if score_l>=11:
            text = font.render("Победил Игрок 2", True, (255, 0, 0))
            screen.blit(text, (width//2 - text.get_width()//2, 240))
            vx=0
            vy=0               
        if score_r>=11:
            text = font.render("Победил Игрок 1", True, (255, 0, 0))
            screen.blit(text, (width//2 - text.get_width()//2, 240))
            vx=0
            vy=0
        
    pygame.display.flip()
    fps.tick(60)
pygame.quit()