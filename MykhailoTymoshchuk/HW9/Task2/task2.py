import pygame #імпортуємо модуль pygame

# Блок нижче відповідає за параметри гри: 
#     FPS - кадри в секунду з якими буде відтворюватись гра
#     WIDTH|HEIGHT DISPLAY - Ширина та висота диспеля в пікселях
#     COORD_X|COORD_Y - Координата початку по х та у  
#     WIDTH_RECTANGLE|HEIGHT_RECTANGLE - Ширина та висота прямокутника 
#     DELTA_STEP - крок із яким переміщається об'єкт (прямокутника) 
#     BLACK_COLOR|RED_COLOR - колір фону вікна (чорний) та колір прямокутника(червоний)
#     

FPS = 60 
WIDTH_DISPLAY = 800 
HEIGHT_DISPLAY = 800 

COORD_X = 10 
COORD_Y = 10
WIDTH_RECTANGLE = 40
HEIGHT_RECTANGLE = 60
DELTA_STEP = 20 

BLACK_COLOR = (0,0,0)
RED_COLOR = (255,0,0) #

#Блок нижче відповідає за:
#   pygame.init - ініцілазація бібліотеки
#   gameDisplay - створення вікна гри заданих розмірів.
#   ygame.RESIABLE - вказує на те , що користувач може змінювати розмір вікна мишкою або за допомогою клавіш
#   ygame.display.set_caption - задаємо назву для нашого вікна
    
pygame.init() 

gameDisplay = pygame.display.set_mode((WIDTH_DISPLAY,HEIGHT_DISPLAY),pygame.RESIZABLE)
pygame.display.set_caption("My 1st game on pygame")

# Блок нижче відповідає за:
#     run - поки True гра буде відтворюватись
#     clock - змінна,яка контролює швидкіть оновлення гри,щоб забезпечити сталу швидкість в різних системах"""
    
run = True
clock = pygame.time.Clock()

# """ Блок коду нижче в якому :
#     while run - конструкція головного циклу гри.Поки значення run - дорівнює Тру,гра буде продовжуватись.False або якщо користувач
#     закриє вікно - гра припиняється.
#     pygame.time.delay - цей виклик функції відповідає за затримку в грі.Пройде Н кількість часу перед тим як перевірити наявність
#     подій або оновити зображення"""
while run:
    pygame.time.delay (100) 
    
# """ Цикл який перебирає всі події в грі,поки гравець не вирішить закрити вікно на Х, тоді в run встановлюється значення False
#     та цикл while run завершується , а гра припиняється""" 
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
                run = False
                
# """ Цей блок відповідає за натиск координати переміщення на натиск клавіші.
#         Перевіряється яка клавіша була натиснута та змінюються координати прямокутника """
    keys = pygame.key.get_pressed()
        
    if keys[pygame.K_LEFT]:
        COORD_X = max(0, COORD_X - DELTA_STEP)
    elif keys[pygame.K_RIGHT]:
        COORD_X = min(WIDTH_DISPLAY - WIDTH_RECTANGLE, COORD_X + DELTA_STEP)
    elif keys[pygame.K_UP]:
        COORD_Y = max(0,COORD_Y - DELTA_STEP)
    elif keys[pygame.K_DOWN]:
        COORD_Y = min(HEIGHT_DISPLAY - HEIGHT_RECTANGLE, COORD_Y + DELTA_STEP)

# """Цей блок відповідає за відображення об'єктів на екрані та керування частотою оновлення дисплею."""
    gameDisplay.fill(BLACK_COLOR)

    pygame.draw.rect(gameDisplay, RED_COLOR,[COORD_X, 
                                          COORD_Y, 
                                          WIDTH_RECTANGLE,
                                          HEIGHT_RECTANGLE])
    pygame.display.update()
    clock.tick(FPS)
    
    