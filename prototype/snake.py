import pygame as pg
from sys import exit
from random import randrange

# Setting the size of the window
window = 750
size = 50
# Setting a range
range = (size // 2, window - size // 2, size)

# lambda function for getting a random position
ranposition = lambda: (randrange(*range), randrange(*range))

# Making the snake and centering it
snake = pg.rect.Rect(0, 0, size - 2, size - 2)
snake.center = ranposition()
length = 1
segments = [tuple(snake)]

# Making the pear and centering it
food = pg.rect.Rect(*ranposition(), size - 2, size - 2)

movement_dir = (0, 0)

time, timestep = 0, 110

# Making the window
pg.init()
screen = pg.display.set_mode((window, window))
clock = pg.time.Clock()

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            exit()

        if event.type == pg.KEYDOWN:
            if event.key == pg.K_w and movement_dir != (0, size):
                movement_dir = (0, -size)
            if event.key == pg.K_s and movement_dir != (0, -size):
                movement_dir = (0, size)
            if event.key == pg.K_a and movement_dir != (size, 0):
                movement_dir = (-size, 0)
            if event.key == pg.K_d and movement_dir != (-size, 0):
                movement_dir = (size, 0)

    screen.fill("black")

    # Making the pears
    pg.draw.rect(screen, 'green', food)
    # Drawing the snake
    for segment in segments:
        pg.draw.rect(screen, 'red', (segment[0], segment[1], size - 2, size - 2))
    pg.display.flip()

    # Moving the snake
    current_time = pg.time.get_ticks()
    if current_time - time > timestep:
        time = current_time
        snake.move_ip(*movement_dir)
        if snake.colliderect(food):
            length += 1
            food.topleft = ranposition()
        segments.append(tuple(snake)[:])
        segments = segments[-length:]

    # Check if snake hits the wall or itself
    if (
        snake.left < 0
        or snake.right > window
        or snake.top < 0``
        or snake.bottom > window
        or len(segments) != len(set(segments))
    ):
        # Game over
        print("Game Over")
        exit()

    clock.tick(60)
