import pygame
from random import randint

pygame.init()

def display_text(text, font, color, x, y):
    text_surface = font.render(text, True, color)
    gameDisplay.blit(text_surface, (x, y))

TITLE_FONT = pygame.font.SysFont('Impact', 30, False, False)
REGULAR_FONT = pygame.font.SysFont('Impact', 20, False, False)
WIDTH = 500
HEIGHT = 250
BACKGROUND_COLOR = (17, 17, 17)
GRAY = (111, 111, 111)
CONGRATS_COLOR = (83, 219, 87)
TEXT_COLOR = (225, 225, 225)
TITLE_COLOR = (191, 191, 191)
LOSING_MESSAGE = (219,83,124)

gameDisplay = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Guess the number game')
clock = pygame.time.Clock()

rand_number = randint(1, 100)
print(rand_number)
NUMBER_OF_ATTEMPTES = 0
MAX_NUMBER_OF_ATTEMPTES = 10 

entered_number = 0
game_running = True
input_text = ""
congrats_message = ""
feedback_message = ""
losing_message = ""

def display_text(text, font, color, x, y):
    text_surface = font.render(text, True, color)
    gameDisplay.blit(text_surface, (x, y))

while game_running:
    gameDisplay.fill(BACKGROUND_COLOR)
    pygame.draw.rect(gameDisplay, GRAY, [0, 50, WIDTH, 50])
    display_text("GUESS THE NUMBER GAME", TITLE_FONT, TITLE_COLOR, 100, 55)
    display_text("Enter the number:", REGULAR_FONT, TEXT_COLOR, 100, 120)
    display_text(input_text, REGULAR_FONT, TEXT_COLOR, 250, 120)
    display_text(congrats_message, REGULAR_FONT, CONGRATS_COLOR, 100, 150)
    display_text(feedback_message, REGULAR_FONT, TEXT_COLOR, 100, 150)
    display_text(losing_message, REGULAR_FONT, TEXT_COLOR, 100, 150)

    NUMBER_OF_ATTEMPTES_text = f"Спроби: {NUMBER_OF_ATTEMPTES}/{MAX_NUMBER_OF_ATTEMPTES}"
    
    display_text(NUMBER_OF_ATTEMPTES_text, REGULAR_FONT, TEXT_COLOR, 100, 180)

    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    game_running = False
                elif event.key == pygame.K_RETURN:
                    entered_number = int(input_text)
                    NUMBER_OF_ATTEMPTES += 1
                    if entered_number == rand_number:
                        congrats_message = "Вітаємо!"
                        game_running = False
                    elif entered_number < 0 or entered_number > 100:
                        feedback_message = "Число в діапазоні від 0 до 100!"    
                    elif entered_number > rand_number:
                        feedback_message = "Число менше!"
                    elif entered_number < rand_number:
                        feedback_message = "Число більше!"
                    input_text = ""  
                elif event.key == pygame.K_BACKSPACE:  
                    input_text = input_text[:-1]
                else:
                    input_text += event.unicode
            if NUMBER_OF_ATTEMPTES >= MAX_NUMBER_OF_ATTEMPTES:
               feedback_message = "Ви вичерпали всі спроби!"
               game_running = False
    pygame.display.update()
    clock.tick(60)
pygame.quit()