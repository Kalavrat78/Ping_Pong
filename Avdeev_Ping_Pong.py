from pygame import *
from random import randint

width = 800
height = 480

root = display.set_mode((width, height))

clock = time.Clock()

PLATFORM_WIDTH = 15
PLATFORM_HEIGHT = 120
PLATFORM_SPEED = 10
platform_player1 = rect.Rect(25, height/2-PLATFORM_HEIGHT/2, PLATFORM_WIDTH, PLATFORM_HEIGHT)
platform_player2 = rect.Rect(width-25, height/2-PLATFORM_HEIGHT/2, PLATFORM_WIDTH, PLATFORM_HEIGHT)

LINE_WIDTH = 2
LINE_HEIGHT = 480
line = rect.Rect(width/2, 0, LINE_WIDTH, LINE_HEIGHT)

CIRCLE_RADIUS = 10
CIRCLE_x_SPEED = 5
CIRCLE_y_SPEED = 5
circle_x_speed = CIRCLE_x_SPEED
circle_y_speed = CIRCLE_y_SPEED
circle_rect = rect.Rect(width/2-CIRCLE_RADIUS, height/2-CIRCLE_RADIUS, CIRCLE_RADIUS*2, CIRCLE_RADIUS*2)

player1 = 0
player2 = 0

init()

my_font = font.Font(None, 42)

game_on = True
game_off = False

WTHIT = (255, 255, 255)
GREEN = (0,255,0)
BLACK = (0, 0, 0)

while game_on:
    for e in event.get():
        if e.type == QUIT:
            game_on = False
            continue

    root.fill(BLACK)
        
    if not game_off:
        keys = key.get_pressed()
        if keys[K_w] and platform_player1.top > 0:
            platform_player1.y -= PLATFORM_SPEED
        elif keys[K_s] and platform_player1.bottom < height:
            platform_player1.y += PLATFORM_SPEED
        if keys[K_UP] and platform_player2.top > 0:
            platform_player2.y -= PLATFORM_SPEED
        elif keys[K_DOWN] and platform_player2.bottom < height:
            platform_player2.y += PLATFORM_SPEED

        draw.rect(root, WTHIT, platform_player1)
        draw.rect(root, WTHIT, platform_player2)
        draw.rect(root, WTHIT, line)

        if platform_player1.colliderect(circle_rect):
            circle_x_speed = CIRCLE_x_SPEED
        elif platform_player2.colliderect(circle_rect):
            circle_x_speed = -CIRCLE_x_SPEED

        circle_rect.x += circle_x_speed
        circle_rect.y += circle_y_speed

        text_player1 = my_font.render(f'{player1}', True, WTHIT)
        root.blit(text_player1, (170, 40))
        text_player2 = my_font.render(f'{player2}', True, WTHIT)
        root.blit(text_player2, (630, 40))
        draw.circle(root, WTHIT, circle_rect.center, CIRCLE_RADIUS)

    if circle_rect.right >= width:
        player1 += 1
        print('player1:',player1)
        circle_rect.x = width/2-CIRCLE_RADIUS
        circle_rect.y = height/2-CIRCLE_RADIUS

    elif circle_rect.left <= 0:
        player2 += 1
        print('player2:',player2)
        circle_rect.x = width/2-CIRCLE_RADIUS
        circle_rect.y = height/2-CIRCLE_RADIUS

    elif circle_rect.bottom >= height:
        circle_y_speed = -CIRCLE_y_SPEED
    
    elif circle_rect.top <= 0:
        circle_y_speed = CIRCLE_y_SPEED

    if player1 == 5:
        game_off = True
    elif player2 == 5:
        game_off = True

    clock.tick(60)

    display.flip()

quit()