import pygame
import sys
from menu import *
from score import *


class highestScore():
    def __init__(self):
        pygame.init()

    def HighestScore():
        with open("Highest score.txt", "r") as f:
            return f.read()

class Game():
    def __init__(self):
        pygame.init()
        self.running, self.playing = True, False
        self.UP_KEY, self.DOWN_KEY, self.START_KEY, self.BACK_KEY = False, False, False, False
        self.DISPLAY_W, self.DISPLAY_H = 760,820
        self.display = pygame.Surface((self.DISPLAY_W,self.DISPLAY_H))
        self.window = pygame.display.set_mode(((self.DISPLAY_W,self.DISPLAY_H)))
        self.font_name = '8-BIT WONDER.TTF'
        self.title=pygame.display.set_caption('Breakout')
        #self.icon=pygame.image.load('breakouticon-removebg-preview.png')
        #self.icon_set=pygame.display.set_icon(self.icon)
        self.BLACK, self.WHITE = (0, 0, 0), (255, 255, 255)
        self.main_menu = MainMenu(self)
        self.options = OptionsMenu(self)
        self.credits = CreditsMenu(self)
        self.curr_menu = self.main_menu

    @property
    def game_loop(self):
        global highestScore, highestScore
        while self.playing:
            self.check_events()
            if self.START_KEY:
                self.playing= False
            self.display.fill(self.BLACK)


            pygame.init()
            pygame.mixer.init()

            WIDTH = 760
            HEIGHT = 820
            size = (WIDTH, HEIGHT)
            screen = pygame.display.set_mode(size)
            pygame.display.set_caption("Breakout")
            clock = pygame.time.Clock()
            FPS = 60

            white = (255, 255, 255)
            grey = (212, 210, 212)
            black = (0, 0, 0)
            blue = (0, 97, 148)

            red = (162, 8, 0)
            green = (0, 127, 33)
            orange = (183, 119, 0)
            yellow = (197, 199, 37)

            score = 0
            balls = 1
            velocity = 4
            try:
                highestScore = int(HighestScore())
            except:
                highestScore = 0

            paddle_width = 80
            paddle_height = 20



            all_sprites_list = pygame.sprite.Group()

            brick_sound = pygame.mixer.Sound('sounds_brick.wav')
            paddle_sound = pygame.mixer.Sound('sounds_paddle.wav')
            wall_sound = pygame.mixer.Sound('sounds_wall.wav')



            class Brick(pygame.sprite.Sprite):
                def __init__(self, color, width, height):
                    super().__init__()
                    self.image = pygame.Surface([width, height])
                    pygame.draw.rect(self.image, color, [0, 0, width, height])
                    self.rect = self.image.get_rect()

            class Paddle(pygame.sprite.Sprite):
                def __init__(self, color, width, height):
                    super().__init__()
                    self.image = pygame.Surface([width, height])
                    pygame.draw.rect(self.image, color, [0, 0, width, height])
                    self.rect = self.image.get_rect()

                def moveRight(self, pixels):
                    self.rect.x += pixels
                    if self.rect.x > WIDTH - wall_width - paddle_width:
                        self.rect.x = WIDTH - wall_width - paddle_width

                def moveLeft(self, pixels):
                    self.rect.x -= pixels
                    if self.rect.x < wall_width:
                        self.rect.x = wall_width

            class Ball(pygame.sprite.Sprite):
                def __init__(self, color, width, height):
                    super().__init__()
                    self.image = pygame.Surface([width, height])
                    pygame.draw.rect(self.image, color, [0, 0, width, height])
                    self.rect = self.image.get_rect()
                    self.velocity = [velocity, velocity]

                def update(self):
                    self.rect.x += self.velocity[0]
                    self.rect.y += self.velocity[1]


                def bounce(self):
                    self.velocity[0] = self.velocity[0]
                    self.velocity[1] = -self.velocity[1]

            ball = Ball(white, 10, 10)
            ball.rect.x = WIDTH // 2 - 5
            ball.rect.y = HEIGHT // 2 - 5

            paddle = Paddle(blue, paddle_width, paddle_height)
            paddle.rect.x = WIDTH // 2 - paddle_width // 2
            paddle.rect.y = HEIGHT - 65

            all_bricks = pygame.sprite.Group()

            brick_width = 80
            brick_height = 16
            x_gap = 5
            y_gap = 7
            wall_width = 2

            def bricks():
                for j in range(9):
                    for i in range(14):
                        if j < 2:
                            if i == 0:
                                brick = Brick(red, brick_width, brick_height)
                                brick.rect.x = wall_width
                                brick.rect.y = 215 + j * (y_gap + brick_height)
                                all_sprites_list.add(brick)
                                all_bricks.add(brick)
                            else:
                                brick = Brick(red, brick_width, brick_height)
                                brick.rect.x = wall_width + brick_width + x_gap + (i - 1) * (brick_width + x_gap)
                                brick.rect.y = 215 + j * (y_gap + brick_height)
                                all_sprites_list.add(brick)
                                all_bricks.add(brick)
                        if 1 < j < 4:
                            if i == 0:
                                brick = Brick(orange, brick_width, brick_height)
                                brick.rect.x = wall_width
                                brick.rect.y = 215 + j * (y_gap + brick_height)
                                all_sprites_list.add(brick)
                                all_bricks.add(brick)
                            else:
                                brick = Brick(orange, brick_width, brick_height)
                                brick.rect.x = wall_width + brick_width + x_gap + (i - 1) * (brick_width + x_gap)
                                brick.rect.y = 215 + j * (y_gap + brick_height)
                                all_sprites_list.add(brick)
                                all_bricks.add(brick)
                        if 3 < j < 6:
                            if i == 0:
                                brick = Brick(green, brick_width, brick_height)
                                brick.rect.x = wall_width
                                brick.rect.y = 215 + j * (y_gap + brick_height)
                                all_sprites_list.add(brick)
                                all_bricks.add(brick)
                            else:
                                brick = Brick(green, brick_width, brick_height)
                                brick.rect.x = wall_width + brick_width + x_gap + (i - 1) * (brick_width + x_gap)
                                brick.rect.y = 215 + j * (y_gap + brick_height)
                                all_sprites_list.add(brick)
                                all_bricks.add(brick)
                        if 5 < j < 8:
                            if i == 0:
                                brick = Brick(yellow, brick_width, brick_height)
                                brick.rect.x = wall_width
                                brick.rect.y = 215 + j * (y_gap + brick_height)
                                all_sprites_list.add(brick)
                                all_bricks.add(brick)
                            else:
                                brick = Brick(yellow, brick_width, brick_height)
                                brick.rect.x = wall_width + brick_width + x_gap + (i - 1) * (brick_width + x_gap)
                                brick.rect.y = 215 + j * (y_gap + brick_height)
                                all_sprites_list.add(brick)
                                all_bricks.add(brick)

            brick_wall = bricks()

            all_sprites_list.add(paddle)
            all_sprites_list.add(ball)



            def main(score, balls):

                global highestScore
                step = 0

                run = True
                while run:

                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            run = False

                    keys = pygame.key.get_pressed()
                    if keys[pygame.K_LEFT]:
                        paddle.moveLeft(10)
                    if keys[pygame.K_RIGHT]:
                        paddle.moveRight(10)

                    all_sprites_list.update()

                    if ball.rect.y < 40:
                        ball.velocity[1] = -ball.velocity[1]
                        wall_sound.play()

                    if ball.rect.x >= WIDTH - wall_width - 10:
                        ball.velocity[0] = -ball.velocity[0]
                        wall_sound.play()

                    if ball.rect.x <= wall_width:
                        ball.velocity[0] = -ball.velocity[0]
                        wall_sound.play()

                    if ball.rect.y > HEIGHT:
                        ball.rect.x = WIDTH // 2 - 5
                        ball.rect.y = HEIGHT // 2 - 5
                        ball.velocity[1] = ball.velocity[1]
                        balls += 1
                        if balls == 4:
                            font = pygame.font.Font('DSEG14Classic-Bold.ttf', 70)
                            text = font.render("GAME OVER", 1, white)
                            text_rect = text.get_rect(center=(WIDTH / 2, HEIGHT / 2))
                            screen.blit(text, text_rect)
                            pygame.display.update()
                            pygame.time.wait(2000)
                            run = False
                            while  4:
                                restart = False
                                for event in pygame.event.get():
                                    if event.type == pygame.QUIT:
                                        sys.exit()
                                    if event.type == pygame.KEYDOWN:
                                        if event.key == pygame.K_ESCAPE:
                                            sys.exit()
                                        if not (event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT):
                                            restart = True

                                if restart:
                                    screen.fill(black)
                                    # brick_wall(WIDTH)
                                    balls = 4
                                    score = 0
                                    break

                            balls = 0
                    pygame.display.update()
                    if pygame.sprite.collide_mask(ball, paddle):
                        ball.rect.x += ball.velocity[0]
                        ball.rect.y -= ball.velocity[1]
                        ball.bounce()
                        paddle_sound.play()

                    brick_collision_list = pygame.sprite.spritecollide(ball, all_bricks, False)
                    for brick in brick_collision_list:
                        ball.bounce()
                        brick_sound.play()
                        if len(brick_collision_list) > 0:
                            step += 1
                            for i in range(0, 448, 28):
                                if step == i:
                                    ball.velocity[0] += 1
                                    ball.velocity[1] += 1
                        if 380.5 > brick.rect.y > 338.5:
                            score += 1
                            brick.kill()
                        elif 338.5 > brick.rect.y > 294:
                            score += 3
                            brick.kill()
                        elif 294 > brick.rect.y > 254.5:
                            score += 5
                            brick.kill()
                        else:
                            score += 7
                            brick.kill()
                        if len(all_bricks) == 0:
                            font = pygame.font.Font('DSEG14Classic-Bold.ttf', 70)
                            text = font.render("CONGRATULATIONS", 1, white)
                            text_rect = text.get_rect(cener=(WIDTH / 2, HEIGHT / 2))
                            all_sprites_list.add(ball)
                            screen.blit(text, text_rect)
                            pygame.display.update()
                            pygame.time.wait(2000)
                            run = False
                        if (highestScore < score):
                            highestScore = score
                        with open("Highest score.txt", "w") as f:
                            f.write(str(highestScore))

                    screen.fill(black)

                    pygame.draw.line(screen, grey, [0, 19], [WIDTH, 19], 40)
                    pygame.draw.line(screen, grey, [(wall_width / 2) - 1, 0], [(wall_width / 2) - 1, HEIGHT],
                                     wall_width)
                    pygame.draw.line(screen, grey, [(WIDTH - wall_width / 2) - 1, 0],
                                     [(WIDTH - wall_width / 2) - 1, HEIGHT],
                                     wall_width)

                    pygame.draw.line(screen, blue, [(wall_width / 2) - 1, HEIGHT - 65 + paddle_height / 2 - 54 / 2],
                                     [(wall_width / 2) - 1, HEIGHT - 65 + paddle_height / 2 - 54 / 2 + 54], wall_width)
                    pygame.draw.line(screen, blue,
                                     [(WIDTH - wall_width / 2) - 1, HEIGHT - 65 + paddle_height / 2 - 54 / 2],
                                     [(WIDTH - wall_width / 2) - 1, HEIGHT - 65 + paddle_height / 2 - 54 / 2 + 54],
                                     wall_width)

                    pygame.draw.line(screen, red, [(wall_width / 2) - 1, 212.5],
                                     [(wall_width / 2) - 1, 212.5 + 2 * brick_height + 2 * y_gap], wall_width)
                    pygame.draw.line(screen, red, [(WIDTH - wall_width / 2) - 1, 212.5],
                                     [(WIDTH - wall_width / 2) - 1, 212.5 + 2 * brick_height + 2 * y_gap], wall_width)

                    pygame.draw.line(screen, orange, [(wall_width / 2) - 1, 212.5 + 2 * brick_height + 2 * y_gap],
                                     [(wall_width / 2) - 1, 212.5 + 4 * brick_height + 4 * y_gap], wall_width)
                    pygame.draw.line(screen, orange,
                                     [(WIDTH - wall_width / 2) - 1, 212.5 + 2 * brick_height + 2 * y_gap],
                                     [(WIDTH - wall_width / 2) - 1, 212.5 + 4 * brick_height + 4 * y_gap], wall_width)

                    pygame.draw.line(screen, green, [(wall_width / 2) - 1, 212.5 + 4 * brick_height + 4 * y_gap],
                                     [(wall_width / 2) - 1, 212.5 + 6 * brick_height + 6 * y_gap], wall_width)
                    pygame.draw.line(screen, green,
                                     [(WIDTH - wall_width / 2) - 1, 212.5 + 4 * brick_height + 4 * y_gap],
                                     [(WIDTH - wall_width / 2) - 1, 212.5 + 6 * brick_height + 6 * y_gap], wall_width)

                    pygame.draw.line(screen, yellow, [(wall_width / 2) - 1, 212.5 + 6 * brick_height + 6 * y_gap],
                                     [(wall_width / 2) - 1, 212.5 + 8 * brick_height + 8 * y_gap], wall_width)
                    pygame.draw.line(screen, yellow,
                                     [(WIDTH - wall_width / 2) - 1, 212.5 + 6 * brick_height + 6 * y_gap],
                                     [(WIDTH - wall_width / 2) - 1, 212.5 + 8 * brick_height + 8 * y_gap], wall_width)

                    font = pygame.font.Font('DSEG14Classic-Bold.ttf', 40)
                    text = font.render(str(f"score {score}"), 1, white)
                    screen.blit(text, (20, 120))
                    text = font.render(str(balls), 1, white)
                    screen.blit(text, (520, 41))
                    #text = font.render('000', 1, white)
                    #screen.blit(text, (580, 120))
                    text = font.render(f"High Score {highestScore}", 1, white)
                    screen.blit(text, (20, 40))

                    all_sprites_list.draw(screen)

                    pygame.display.update()

                    clock.tick(FPS)
                    pygame.display.update()
                pygame.quit()

            main(score, balls)

        self.reset_keys()



    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running, self.playing = False, False
                self.curr_menu.run_display = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    self.START_KEY = True
                if event.key == pygame.K_BACKSPACE:
                    self.BACK_KEY = True
                if event.key == pygame.K_DOWN:
                    self.DOWN_KEY = True
                if event.key == pygame.K_UP:
                    self.UP_KEY = True

    def reset_keys(self):
        self.UP_KEY, self.DOWN_KEY, self.START_KEY, self.BACK_KEY = False, False, False, False

    def draw_text(self, text, size, x, y ):
        font = pygame.font.Font(self.font_name,size)
        text_surface = font.render(text, True, self.WHITE)
        text_rect = text_surface.get_rect()
        text_rect.center = (x,y)
        self.display.blit(text_surface,text_rect)
