import pygame
import random

pygame.init()

width = 500
height = 400
canvas = pygame.display.set_mode((width, height))
pygame.display.set_caption("Движение")

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
player_x = width // 2
player_y = height - 80
player_speed = 1

rect1 = pygame.Rect(player_x, player_y, 50, 50)

current_color = RED

x_block = random.randint(50, 16)
y_block = 50


moving_left = False
moving_right = False

clock = pygame.time.Clock()
TIME=120

def change_color():
    global current_color
    if current_color == RED:
        current_color = GREEN
    elif current_color == GREEN:
        current_color = BLUE

    else:
        current_color = RED

running = True

while running:
    canvas.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Обработка событий клавиатуры
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                moving_left = True
            elif event.key == pygame.K_RIGHT:
                moving_right = True
            if event.key == pygame.K_SPACE:
                change_color()

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                moving_left = False
            elif event.key == pygame.K_RIGHT:
                moving_right = False

    pygame.draw.rect(canvas, (255, 255, 0), (x_block, y_block, 50, 50))

    if y_block == 600:
        y_block = 50
        x_block = random.randint(50, 650)
    else:
        y_block += 1

    # Изменение позиции игрока на основе состояния клавиш
    if moving_left:
        rect1.left -= player_speed
    if moving_right:
        rect1.right += player_speed

    pygame.draw.rect(canvas, current_color, rect1)
    if rect1.left < 50:
        rect1.left = 50
    if rect1.right > 750:
        rect1.right = 750
    pygame.display.update()
    clock.tick(TIME)

pygame.quit()