import pygame

pygame.init()
pygame.mixer.init()

score = 0
balls = 1
velocity = 4

paddle_width = 54
paddle_height = 20

all_sprites_list = pygame.sprite.Group()

WIDTH = 600
HEIGHT = 750
size = (WIDTH,HEIGHT)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Breakout")
clock = pygame.time.Clock()
FPS = 60

white = (255,255,255)
black = (0,0,0)

def main():

    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
    font = pygame.font.Font('D:/College/Atari Breakout/DSEG14Classic-Bold.ttf', 70)
    text = font.render("BREAKOUT", 1, white)
    all_bricks = pygame.sprite.Group()
    screen.fill(black)

    all_sprites_list.draw(screen)
    pygame.display.update()
    clock.tick(FPS)
pygame.quit()



main()
