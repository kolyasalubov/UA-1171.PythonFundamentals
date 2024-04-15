import pygame #імпортуємо модуль pygame
""" 
Варіант гри з звуком + працював над виведенням повідолмення але щось не вийшло)
"""
#Ініціалізація pygame
pygame.init()

#Параметри гри
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

#Дисплей та звук
gameDisplay = pygame.display.set_mode((WIDTH_DISPLAY,HEIGHT_DISPLAY),pygame.RESIZABLE)
pygame.display.set_caption("My 1st game on pygame")
# ініціалізаця звукового модуля та додавання звуку - фейл)
pygame.mixer.init()
fail_sound = pygame.mixer.Sound('MykhailoTymoshchuk/HW9/Task2/kva_kva_sound.wav')

#
font = pygame.font.Font ("MykhailoTymoshchuk/HW9/Task2/arial.ttf",36)

#    
run = True
clock = pygame.time.Clock()


while run:
    pygame.time.delay (100) 
    
#   
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
                run = False
                
                
    keys = pygame.key.get_pressed()
        
    if keys[pygame.K_LEFT]:
        COORD_X = max(0, COORD_X - DELTA_STEP)
    elif keys[pygame.K_RIGHT]:
        COORD_X = min(WIDTH_DISPLAY - WIDTH_RECTANGLE, COORD_X + DELTA_STEP)
    elif keys[pygame.K_UP]:
        COORD_Y = max(0,COORD_Y - DELTA_STEP)
    elif keys[pygame.K_DOWN]:
        COORD_Y = min(HEIGHT_DISPLAY - HEIGHT_RECTANGLE, COORD_Y + DELTA_STEP)
        
#Перевірка торкання стінки

    if COORD_X <= 0 or COORD_X >= WIDTH_DISPLAY - WIDTH_RECTANGLE or \
       COORD_Y <= 0 or COORD_Y >= HEIGHT_DISPLAY - HEIGHT_RECTANGLE:
        fail_sound.play()
        message = font.render ('Loooser', True , (160, 32, 240, 255))
        gameDisplay.blit(message, (WIDTH_DISPLAY // 2 - message.get_width() // 2, HEIGHT_DISPLAY // 2 - message.get_height() // 2))
#Очистка екрану 
    gameDisplay.fill(BLACK_COLOR)
#Малюємо прямокутник
    pygame.draw.rect(gameDisplay, RED_COLOR,[COORD_X, 
                                          COORD_Y, 
                                          WIDTH_RECTANGLE,
                                          HEIGHT_RECTANGLE])
#Оновлення дисплею
    pygame.display.update()
#Обмеження кадрів в секунду
    clock.tick(FPS)
    
pygame.quit()
    