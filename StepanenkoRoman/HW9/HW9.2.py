import pygame

FPS = 60

WIDTH_DISPLAY=500
HEIGHT_DISPLAY=500

WHITE_COLOR = (255, 255, 255)  
My_COLOR = (0, 0, 255)

COORD_X = 40
COORD_Y = 60
WIDTH_RECTANGLE = 50
HEIGHT_RECTANGLE = 70
DELTA_STEP = 5
 
 
pygame.init()

gameDisplay = pygame.display.set_mode((WIDTH_DISPLAY, HEIGHT_DISPLAY))

pygame.display.set_caption("My second game")

run = True
clock = pygame.time.Clock()

while run:
    pygame.time.delay(100)
    
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            run=False

    keys=pygame.key.get_pressed()
    
    if keys[pygame.K_LEFT] and COORD_X > DELTA_STEP:
        COORD_X = COORD_X - DELTA_STEP
    if keys[pygame.K_RIGHT] and COORD_X < (WIDTH_DISPLAY - WIDTH_RECTANGLE - DELTA_STEP):
        COORD_X = COORD_X + DELTA_STEP
    if keys[pygame.K_UP] and COORD_Y > DELTA_STEP:
        COORD_Y = COORD_Y - DELTA_STEP
    if keys[pygame.K_DOWN] and COORD_Y < (HEIGHT_DISPLAY - HEIGHT_RECTANGLE - DELTA_STEP):
        COORD_Y = COORD_Y + DELTA_STEP


    gameDisplay.fill((255,255,255)) 

    pygame.draw.rect(gameDisplay, My_COLOR, [COORD_X, 
                                            COORD_Y, 
                                            WIDTH_RECTANGLE, 
                                            HEIGHT_RECTANGLE])
    pygame.display.update()
    clock.tick(FPS)