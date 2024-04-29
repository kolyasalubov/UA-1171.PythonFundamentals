import pygame as pg
import random, time, sys
from pygame.locals import *

# Загальні параметри гри. Розмір вікна, фпс, швидкість переміщення. Палітра кольорів та змінна для клітинки фігури
FPS = 60
WINDOW_W, WINDOW_H = 600, 500
BLOCK, CUP_H, CUP_W = 20, 20, 10
SIDE_FREQ, DOWN_FREQ = 0.15, 0.1 

SIDE_MARGIN = int((WINDOW_W - CUP_W * BLOCK) / 2)
TOP_MARGIN = WINDOW_H - (CUP_H * BLOCK) - 5

colors = ((0, 0, 225), (0, 225, 0), (225, 0, 0), (225, 225, 0)) 
lightcolors = ((30, 30, 255), (50, 255, 50), (255, 30, 30), (255, 255, 30)) 

white, gray, black  = (255, 255, 255), (185, 185, 185), (0, 0, 0)
brd_color, bg_color, txt_color, title_color, info_color = white, black, white, colors[3], colors[0]

# Додамо трішки вайбу 80х.
pg.mixer.init()
retro_sound = pg.mixer.Sound('MykhailoTymoshchuk\PetProject\_sound\_retroSound.wav')
retro_sound.set_volume(0.025)

fig_w, fig_h = 5, 5
empty = 'o'

# Матричний метод визначення положення фігур
figures = {'S': [['ooooo',
                  'ooooo',
                  'ooxxo',
                  'oxxoo',
                  'ooooo'],
                 ['ooooo',
                  'ooxoo',
                  'ooxxo',
                  'oooxo',
                  'ooooo']],
           'Z': [['ooooo',
                  'ooooo',
                  'oxxoo',
                  'ooxxo',
                  'ooooo'],
                 ['ooooo',
                  'ooxoo',
                  'oxxoo',
                  'oxooo',
                  'ooooo']],
           'J': [['ooooo',
                  'oxooo',
                  'oxxxo',
                  'ooooo',
                  'ooooo'],
                 ['ooooo',
                  'ooxxo',
                  'ooxoo',
                  'ooxoo',
                  'ooooo'],
                 ['ooooo',
                  'ooooo',
                  'oxxxo',
                  'oooxo',
                  'ooooo'],
                 ['ooooo',
                  'ooxoo',
                  'ooxoo',
                  'oxxoo',
                  'ooooo']],
           'L': [['ooooo',
                  'oooxo',
                  'oxxxo',
                  'ooooo',
                  'ooooo'],
                 ['ooooo',
                  'ooxoo',
                  'ooxoo',
                  'ooxxo',
                  'ooooo'],
                 ['ooooo',
                  'ooooo',
                  'oxxxo',
                  'oxooo',
                  'ooooo'],
                 ['ooooo',
                  'oxxoo',
                  'ooxoo',
                  'ooxoo',
                  'ooooo']],
           'I': [['ooxoo',
                  'ooxoo',
                  'ooxoo',
                  'ooxoo',
                  'ooooo'],
                 ['ooooo',
                  'ooooo',
                  'xxxxo',
                  'ooooo',
                  'ooooo']],
           'O': [['ooooo',
                  'ooooo',
                  'oxxoo',
                  'oxxoo',
                  'ooooo']],
           'T': [['ooooo',
                  'ooxoo',
                  'oxxxo',
                  'ooooo',
                  'ooooo'],
                 ['ooooo',
                  'ooxoo',
                  'ooxxo',
                  'ooxoo',
                  'ooooo'],
                 ['ooooo',
                  'ooooo',
                  'oxxxo',
                  'ooxoo',
                  'ooooo'],
                 ['ooooo',
                  'ooxoo',
                  'oxxoo',
                  'ooxoo',
                  'ooooo']]}

# Блок який відповідає за вікно паузи
def pauseScreen():
        pause = pg.Surface((600, 500), pg.SRCALPHA)   
        pause.fill((0, 0, 255, 127))                        
        display_surf.blit(pause, (0, 0))

# Основна фукнція гри. Ініцілазація змін
def main():
    global FPS_clock, display_surf, basic_font, big_font
    pg.init()
    retro_sound.play()
    FPS_clock = pg.time.Clock()
    display_surf = pg.display.set_mode((WINDOW_W, WINDOW_H))
    basic_font = pg.font.SysFont('arial', 20) 
    big_font = pg.font.Font('MykhailoTymoshchuk\PetProject\_fonts\_font_retro.ttf', 70) # Кастомний шрифт, для більшого вайбу
    showText('TETRIS')
    
    while True: # Головний цикл гри, виклик самого тетрісу. вікна пазуи та тексту.Відтворюється поки не буде примусово зупинено
        runTetris()
        pauseScreen()
        showText('Гра закінчена')

#Ця функція відповідає за основний цикл гри
# Ініціалізація необхідних змінних : стакан ,рухи фігур ,рахунок, рівень а також приймає нові фігури,як наступні
def runTetris():
    cup = emptycup()
    last_move_down = time.time()
    last_side_move = time.time()
    last_fall = time.time()
    going_down = False 
    going_left = False
    going_right = False
    points = 0
    level, fall_speed = calcSpeed(points)
    fallingFig = getNewFig()
    nextFig = getNewFig() #Виклик нової фігури

# Перевірка наявності фігури,яка падає.
    while True: 
        if fallingFig == None:
            #Якщо фігура не падає, то ми генеруємо нову 
            fallingFig = nextFig
            nextFig = getNewFig()
            last_fall = time.time()
            

            if not checkPos(cup, fallingFig):
                return # Якщо фігурі немає куди впасти - гра закінчена
        quitGame()
        
        # Перевірка події паузи
        for event in pg.event.get(): 
            if event.type == KEYUP:
                if event.key == K_SPACE:
                    pauseScreen()
                    showText('Пауза')
                    last_fall = time.time()
                    last_move_down = time.time()
                    last_side_move = time.time()
                elif event.key == K_LEFT:
                    going_left = False
                elif event.key == K_RIGHT:
                    going_right = False
                elif event.key == K_DOWN:
                    going_down = False
                    
#Обробка подій які відповідають за натискання клавіш під час гри
            elif event.type == KEYDOWN:
                if event.key == K_LEFT and checkPos(cup, fallingFig, adjX=-1):
                    fallingFig['x'] -= 1 #віднімання 1 від координати Х ,Яка відповідає за вертикальне падіння 
                    going_left = True
                    going_right = False
                    last_side_move = time.time()

                elif event.key == K_RIGHT and checkPos(cup, fallingFig, adjX=1):
                    fallingFig['x'] += 1
                    going_right = True
                    going_left = False
                    last_side_move = time.time()

                # Поворот фігури + перевірка чи місце на цей мув
                elif event.key == K_UP:
                    fallingFig['rotation'] = (fallingFig['rotation'] + 1) % len(figures[fallingFig['shape']])
                    if not checkPos(cup, fallingFig):
                        fallingFig['rotation'] = (fallingFig['rotation'] - 1) % len(figures[fallingFig['shape']])

                # Присокрення падіння фігури.
                elif event.key == K_DOWN:
                    going_down = True
                    if checkPos(cup, fallingFig, adjY=1): # CheckPos функція - перевірка можливості руху фігури.Чи вона не конфлікує
                                                        # з межею стакана або іншими фігурами
                        fallingFig['y'] += 1
                    last_move_down = time.time()

                # Миттєве скидання фігури вниз
                elif event.key == K_RETURN: # клавіша ENTER 
                    going_down = False 
                    going_left = False
                    going_right = False
                    for i in range(1, CUP_H):
                        if not checkPos(cup, fallingFig, adjY=i):
                            break
                    fallingFig['y'] += i - 1

        # Керування падінням фігури при зажатій клавіші
        if (going_left or going_right) and time.time() - last_side_move > SIDE_FREQ:
            if going_left and checkPos(cup, fallingFig, adjX=-1):
                fallingFig['x'] -= 1
            elif going_right and checkPos(cup, fallingFig, adjX=1):
                fallingFig['x'] += 1
            last_side_move = time.time()

        if going_down and time.time() - last_move_down > DOWN_FREQ and checkPos(cup, fallingFig, adjY=1):
            fallingFig['y'] += 1
            last_move_down = time.time()

        # Перевірка фігури при "вільному падінні"
        if time.time() - last_fall > fall_speed: # Вільне падіння фігури            
            if not checkPos(cup, fallingFig, adjY=1): # Перевірка "Призмелення" фігури
                addToCup(cup, fallingFig) # Фігура приземлилась - добавляємо до стакану
                points += clearCompleted(cup)
                level, fall_speed = calcSpeed(points)
                fallingFig = None
            else: # Пока фігура не приземлилась, продовжуєм рух
                fallingFig['y'] += 1
                last_fall = time.time()

        # Малюємо вікно гри. Відображення кольору, інформації про рівень, рахунок.
        display_surf.fill(bg_color)
        # display_surf.blit(title_bg, (0,0))
        drawTitle()
        gamecup(cup)
        drawInfo(points, level)
        drawnextFig(nextFig)
        if fallingFig != None:
            drawFig(fallingFig)
        pg.display.update()
        FPS_clock.tick(FPS)

# Створення текстового обєкту на екрані гри.Встановлення кольору та шрифту
def txtObjects(text, font, color):
    surf = font.render(text, True, color)
    return surf, surf.get_rect()

# Завершення гри
def stopGame():
    pg.quit() # закриття самої бібліотеки та звільнення пам'яті
    sys.exit()# коректне закриття програми

# Перевірка всіх подій на натиск клавіш користувачем
def checkKeys():
    quitGame()

    for event in pg.event.get([KEYDOWN, KEYUP]):
        if event.type == KEYDOWN:
            continue
        return event.key
    return None

# Відображення тексту на екрані гри та вказівка для користувача
def showText(text):
    titleSurf, titleRect = txtObjects(text, big_font, title_color)
    titleRect.center = (int(WINDOW_W / 2) - 1, int(WINDOW_H / 2) - 2)
    display_surf.blit(titleSurf, titleRect)
    
    
    pressKeySurf, pressKeyRect = txtObjects('Тицьни щоб почати', basic_font, title_color)
    pressKeyRect.center = (int(WINDOW_W / 2), int(WINDOW_H / 2) + 150)
    display_surf.blit(pressKeySurf, pressKeyRect)
    #Цикл буде виконуватись поки не буде натиску жодної із клавіш
    while checkKeys() == None:
        pg.display.update()
        FPS_clock.tick()

# Перевіка вхідних подій ,які відповідають за закриття вікна
def quitGame():
    for event in pg.event.get(QUIT): 
        stopGame() 
    for event in pg.event.get(KEYUP): 
        if event.key == K_ESCAPE:
            stopGame() 
        pg.event.post(event) 

# Визначення швидкості падіння фігур та рівня на основі набраних балів
def calcSpeed(points):
    
    level = int(points / 10) + 1
    fall_speed = 0.27 - (level * 0.02)
    return level, fall_speed

# Генерування фігури та її параметрів - колір, положення
def getNewFig():
    # Повернення випадкової фігури з випадковим кольором.Отримання списку фігур.Встановлення рандомного повроту фігури
    shape = random.choice(list(figures.keys()))
    newFigure = {'shape': shape,
                'rotation': random.randint(0, len(figures[shape]) - 1),
                'x': int(CUP_W / 2) - int(fig_w / 2),
                'y': -2, 
                'color': random.randint(0, len(colors)-1)}
    return newFigure

# Фукнція яка додає фігуру в стакан.
def addToCup(cup, fig):
    for x in range(fig_w): # Перевірка координат різних осей х і у
        for y in range(fig_h):
            if figures[fig['shape']][fig['rotation']][y][x] != empty: # перевірка на заповнення клітинки і додавання до стакану ,Як наслідок
                cup[x + fig['x']][y + fig['y']] = fig['color']

# Створення порожнього стакана
def emptycup():
    # создает пустой стакан
    cup = []
    for i in range(CUP_W):
        cup.append([empty] * CUP_H)
    return cup

# Перевірка клітинки в стакані за координатами
def incup(x, y):
    return x >= 0 and x < CUP_W and y < CUP_H

# Перевірка знаходження фігури в межах ігрового поля та її неконфліктність з іншими фігурами
def checkPos(cup, fig, adjX=0, adjY=0):
    for x in range(fig_w):
        for y in range(fig_h):
            abovecup = y + fig['y'] + adjY < 0
            if abovecup or figures[fig['shape']][fig['rotation']][y][x] == empty:
                continue
            if not incup(x + fig['x'] + adjX, y + fig['y'] + adjY):
                return False
            if cup[x + fig['x'] + adjX][y + fig['y'] + adjY] != empty:
                return False
    return True

# Перевірка повного заповлення поля
def isCompleted(cup, y):
    for x in range(CUP_W):
        if cup[x][y] == empty:
            return False
    return True

#Видалення нижнього ряду та додавання нового
def clearCompleted(cup):

    removed_lines = 0
    y = CUP_H - 1 
    while y >= 0:
        if isCompleted(cup, y):
           for pushDownY in range(y, 0, -1):
                for x in range(CUP_W):
                    cup[x][pushDownY] = cup[x][pushDownY-1]
           for x in range(CUP_W):
                cup[x][0] = empty
           removed_lines += 1
        else:
            y -= 1 
    return removed_lines

# Конвертація координат блоіків у піксельні координати на ігровому полі.Потрібно для правильного рендеру блоків.
def convertCoords(BLOCK_x, BLOCK_y):
    return (SIDE_MARGIN + (BLOCK_x * BLOCK)), (TOP_MARGIN + (BLOCK_y * BLOCK))

# Візуалізація квадратних блоків ,Які складають фігуру.
def drawBLOCK(BLOCK_x, BLOCK_y, color, pixelx=None, pixely=None):
    if color == empty:
        return
    if pixelx == None and pixely == None:
        pixelx, pixely = convertCoords(BLOCK_x, BLOCK_y)
    pg.draw.rect(display_surf, colors[color], (pixelx + 1, pixely + 1, BLOCK - 1, BLOCK - 1), 0, 3)
    pg.draw.rect(display_surf, lightcolors[color], (pixelx + 1, pixely + 1, BLOCK - 4, BLOCK - 4), 0, 3)
    pg.draw.circle(display_surf, colors[color], (pixelx + BLOCK / 2, pixely + BLOCK / 2), 5)

# Встановлення параметрів ігрового поля 
def gamecup(cup):
    # Границя ігроового поля та стакану
    pg.draw.rect(display_surf, brd_color, (SIDE_MARGIN - 4, TOP_MARGIN - 4, (CUP_W * BLOCK) + 8, (CUP_H * BLOCK) + 8), 5)

    # drawTitle()
    # drawInfo()
    # drawNextFig()
    # Фон ігрового поля
    pg.draw.rect(display_surf, bg_color, (SIDE_MARGIN, TOP_MARGIN, BLOCK * CUP_W, BLOCK * CUP_H))
    for x in range(CUP_W):
        for y in range(CUP_H):
            drawBLOCK(x, y, cup[x][y])

#retro_font = pg.font.Font('F:\SoftServe\MyLocal\Train\SelfStudy\PetProject\_fonts\_font_retro.ttf', 52)

# Параметри тексту
def drawTitle():
    titleSurf = big_font.render('TETRIS', True, title_color)
    titleRect = titleSurf.get_rect()
    titleRect.topleft = (WINDOW_W - 410, 20)
    display_surf.blit(titleSurf, titleRect)
    
#Параметри виведення інформативного поля та текстів в грі
def drawInfo(points, level):

    pointsSurf = basic_font.render(f'РАХУНОК: {points}', True, txt_color)
    pointsRect = pointsSurf.get_rect()
    pointsRect.topleft = (WINDOW_W - 550, 180)
    display_surf.blit(pointsSurf, pointsRect)

    levelSurf = basic_font.render(f'РІВЕНь: {level}', True, txt_color)
    levelRect = levelSurf.get_rect()
    levelRect.topleft = (WINDOW_W - 550, 250)
    display_surf.blit(levelSurf, levelRect)

    pausebSurf = basic_font.render('ПАУЗА: ПРОБІЛ', True, info_color)
    pausebRect = pausebSurf.get_rect()
    pausebRect.topleft = (WINDOW_W - 570, 420)
    display_surf.blit(pausebSurf, pausebRect)
    
    escbSurf = basic_font.render('ВИХІД: Esc', True, info_color)
    escbRect = escbSurf.get_rect()
    escbRect.topleft = (WINDOW_W - 550, 450)
    display_surf.blit(escbSurf, escbRect)

# Малювання фігур
def drawFig(fig, pixelx=None, pixely=None):
    figToDraw = figures[fig['shape']][fig['rotation']]
    if pixelx == None and pixely == None:    
        pixelx, pixely = convertCoords(fig['x'], fig['y'])

    for x in range(fig_w):
        for y in range(fig_h):
            if figToDraw[y][x] != empty:
                drawBLOCK(None, None, fig['color'], pixelx + (x * BLOCK), pixely + (y * BLOCK))

#Візуалізація і відображення наступної фігура на границі поля гри
def drawnextFig(fig):  
    nextSurf1 = basic_font.render('НАСТУПНА', True, txt_color)
    nextSurf2 = basic_font.render('ФІГУРА', True , txt_color)
    nextRect1 = nextSurf1.get_rect()
    nextRect2 = nextSurf2.get_rect()
    # Координата виведення першого слова
    nextRect1.topleft = (WINDOW_W - 150, 180) # 
    display_surf.blit(nextSurf1, nextRect1)
    # Координата виведення другого слова
    nextRect2.topleft = (WINDOW_H - 30 ,nextRect1.bottom + 10) # 
    display_surf.blit(nextSurf2, nextRect2)
    drawFig(fig, pixelx=WINDOW_W - 150, pixely=250)

if __name__ == '__main__':
    main()