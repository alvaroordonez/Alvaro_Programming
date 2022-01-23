# Imports
import pygame, sys
from pygame.locals import *
import random, time

# initialize program
pygame.init()

# Setting up color objects
BLACK = (0, 0, 0)  # Black
WHITE = (255, 255, 255)  # White
GRAY = (128, 128, 128)  # Gray
RED = (255, 0, 0)  # Red
BLUE = (0, 0, 255)  # Blue
GREEN = (0, 255, 0)  # Green

# assigning FPS Value
FPS = 60
FramePerSec = pygame.time.Clock()

# Setting up other variables that will be used in program
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SPEED = 5
SCORE_1 = 0
SCORE_2 = 0

# Setting up Fonts
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game_Over", True, BLACK)

background = pygame.image.load("space.png")

# Create white screen
DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("Alvy Game: Pong")


class Ball(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Enemy.png")
        self.rect = self.image.get_rect()
        #self.rect.center = (random.randint(40, SCREEN_WIDTH-40), 0)

        self.velocity = [random.randint(4, 8), random.randint(-8, 8)]

    def move(self):
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]

        # Check if the ball is bouncing against any of the 4 walls:
        if self.rect.x >= 750:
            self.velocity[0] = -self.velocity[0]
        if self.rect.x <= 0:
            self.velocity[0] = -self.velocity[0]
        if self.rect.y > 510:
            self.velocity[1] = -self.velocity[1]
        if self.rect.y < 0:
            self.velocity[1] = -self.velocity[1]

    def bounce(self):
        self.velocity[0] = -self.velocity[0]
        self.velocity[1] = random.randint(-8, 8)

class Player_1(pygame.sprite.Sprite):
    def __init__(self, coord):
        super().__init__()
        self.image = pygame.image.load("Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = coord

    def move(self):
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[K_UP] and self.rect.top > 0:
            self.rect.move_ip(0, -5)
        if pressed_keys[K_DOWN] and self.rect.bottom < SCREEN_HEIGHT:
            self.rect.move_ip(0, 5)


class Player_2(pygame.sprite.Sprite):
    def __init__(self, coord):
        super().__init__()
        self.image = pygame.image.load("Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = coord

    def move(self):
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[K_w] and self.rect.top > 0:
            self.rect.move_ip(0, -5)
        if pressed_keys[K_s] and self.rect.bottom < SCREEN_HEIGHT:
            self.rect.move_ip(0, 5)

start_coord_1 = (35, 520)
start_coord_2 = (765, 100)

# Setting up Sprites
P1 = Player_1(start_coord_1)
P2 = Player_2(start_coord_2)
E1 = Ball()

# Creating Sprites Groups
enemies = pygame.sprite.Group()
enemies.add(E1)
all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(P2)
all_sprites.add(E1)

# Adding a new User event
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)

# Beginning of game: GAME LOOP
while True:
    # Cycles through all events occuring
    for event in pygame.event.get():
        if event.type == INC_SPEED:
            SPEED += 2

        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    DISPLAYSURF.blit(background, (0, 0))
    pygame.draw.line(background, WHITE, [380, 0], [380, 600], 5)
    score_1 = font_small.render(str(SCORE_1), True, RED)
    score_2 = font_small.render(str(SCORE_2), True, RED)
    DISPLAYSURF.blit(score_1, (10, 10))
    DISPLAYSURF.blit(score_2, (770, 10))

    # Moves and Re-draws all Sprites
    for entity in all_sprites:
        DISPLAYSURF.blit(entity.image, entity.rect)
        entity.move()

    # To be run if collision occurs between Player and Ball
    if pygame.sprite.spritecollideany(P1, enemies):
        pygame.mixer.Sound("crash.wav").play()
        E1.bounce()
        SCORE_1 += 1

    if pygame.sprite.spritecollideany(P2, enemies):
        pygame.mixer.Sound("crash.wav").play()
        E1.bounce()
        SCORE_2 += 1

    pygame.display.update()
    FramePerSec.tick(FPS)
