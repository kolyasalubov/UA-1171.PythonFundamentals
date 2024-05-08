import pygame
from random import randint as rand

width=1200
height=770
fps=60

pygame.init()
screen=pygame.display.set_mode((width,height))
clock=pygame.time.Clock()

img = pygame.image.load('space.jpg').convert()
pygame.display.set_caption('arkanoid')
pygame.display.set_icon(pygame.image.load("icon.png"))

#LIFES
life=3

# text settings
text_font=pygame.font.SysFont('Arial',30)
def draw_text(text,font,text_col,x,y):
    img=font.render(text,True,text_col)
    screen.blit(img,(x,y))

#platform settings
platform_w= 210
platform_h= 20
platform_speed= 10
platform= pygame.Rect(width//2 - platform_w//2, height - platform_h - 10, platform_w, platform_h)

# ball settings
speed_standart = 4
ball_radius= 10
ball_speed= speed_standart
ball_rect= int(ball_radius*2**0.5)
ball= pygame.Rect(rand(ball_rect,width - ball_rect), height//2, ball_rect, ball_rect)
dx= 1
dy= -1

# block settings
block_list=[pygame.Rect(10+120*i, 10+77*j, 80, 20)for i in range(10) for j in range(4)]
color_list=[(rand(30,255),rand(30,255),rand(30,255)) for i in range(10) for j in range(4)]


def detect_collision(dx,dy,ball,rect):
    if  dx > 0:
        delta_x = ball.right - rect.left
    else:
        delta_x=rect.right - rect.left
    if dy > 0:
        delta_y = ball.bottom - rect.top
    else:
        delta_y=rect.bottom - ball.top
    if abs(delta_x - delta_y) < 10:
        dx=-dx
        dy=-dy
    elif delta_x > delta_y:
        dy = -dy
    elif delta_x < delta_y:
        dx = -dx
    return dx,dy


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    screen.blit(img,(0,0))
   
    # game
    [pygame.draw.rect(screen,color_list[color],block)for color, block in enumerate(block_list)]
    pygame.draw.rect(screen, pygame.Color('aqua'), platform)
    pygame.draw.circle(screen,pygame.Color('yellow'), ball.center, ball_radius)

    #text
    draw_text('LIFES: '+str(life),text_font,(255,255,255),width-110,10)

    #ball movement
    ball.x +=ball_speed*dx
    ball.y+=ball_speed*dy

    #collision left/right
    if ball.centerx < ball_radius or ball.centerx > width - ball_radius:
        dx= -dx
    #collision top
    if ball.centery < ball_radius:
       dy= -dy 
       
    #collision platform
    if ball.colliderect(platform) and dy > 0:
        dx,dy=detect_collision(dx,dy,ball,platform)
        if ball_speed<10:
            ball_speed+=0.5

    #collision block
    hit_index= ball.collidelist(block_list)
    if hit_index != -1:
        hit_rect=block_list.pop(hit_index)
        hit_color=color_list.pop(hit_index)
        dx,dy=detect_collision(dx,dy,ball,hit_rect)
        

        # special effect
        hit_rect.inflate_ip(ball.width*2,ball.height*2)
        pygame.draw.rect(screen,hit_color,hit_rect)
        fps+=2

    # ball touch bottom
    if ball.bottom > height+10:
        life-=1
        ball_speed = speed_standart
        ball= pygame.Rect(rand(ball_rect,width - ball_rect), height//2, ball_rect, ball_rect)

    # win/game over
    if ball.bottom > height and life == 0:
        print('game over!')
        exit()
    elif not len(block_list):
        print('win!')
        exit()
    # control platform
    key=pygame.key.get_pressed()
    if key[pygame.K_LEFT] and platform.left > 0:
        platform.left-=platform_speed
    if key[pygame.K_RIGHT] and platform.right < width:
        platform.right+=platform_speed
    if key[pygame.K_DOWN] and platform.bottom < height:
        platform.bottom+=platform_speed
    if key[pygame.K_UP] and platform.top > height-50:
        platform.top-=platform_speed

    pygame.display.flip()
    clock.tick(fps)