import pygame
import random

window_x = 1280
window_y = 720

screen = pygame.display.set_mode((window_x,window_y))
pygame.display.set_caption("Rainbow-Tic Tac Toe")
clock = pygame.time.Clock()

def get_rand_colour():
    colour_r = random.randint(0,255)
    colour_g = random.randint(0,255)
    colour_b = random.randint(0,255)
    return (colour_r,colour_g,colour_b)

done = False
counter = 100
colour = get_rand_colour()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    counter += 1
    if counter > 5:
        colour = get_rand_colour()
        counter = 100

    screen.fill(colour)
    pygame.display.flip()
    clock.tick(10)

pygame.quit()