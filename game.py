import pygame
import random
from pygame import mixer 

# Initialize the game
pygame.init()

# Create the screen
screen = pygame.display.set_mode((800, 700))

# Title and Icon
pygame.display.set_caption("Catcher")
icon = pygame.image.load('data/images/icon.png')
pygame.display.set_icon(icon)


background = pygame.image.load('data/images/background.jpg')

# Player
playerImg = pygame.image.load('data/images/trash-bin.png')
playerX = 350
playerY = 550
playerX_change = 0

# Paper
paperImg = pygame.image.load('data/images/paper.png')
paperX = random.randint(50, 750)
paperY = random.randint(0, 15)
paperY_y = random.randint(0, 15)
num_of_enemies = 6
Y_paper_velocity = 2
gravity = 0.05

score = 0
font = pygame.font.Font('data/font/Inconsolata_Expanded-Bold.ttf', 32)
score_x = 30
score_y = 500

mixer.music.load('data/music/background_music.mp3')
mixer.music.play(-1)

color =  238, 255, 0
def show_score(x, y):
    font_score = font.render("Score: " + str(score), True, (color))
    screen.blit(font_score, (x, y))

# Game loop
clock = pygame.time.Clock()
running = True
while running:
    clock.tick(60)
    # RGB
    screen.fill((242, 212, 160))
    
    screen.blit(background, (0, 0))

    player_rect = screen.blit(playerImg, (playerX, playerY))
    paper_rect = screen.blit(paperImg, (paperX, paperY))
    # To quit when close is pressed
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -7
            if event.key == pygame.K_RIGHT:
                playerX_change = 7
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

    playerX += playerX_change

    if playerX <= 0:
        playerX = 0
    elif playerX >= 672:
        playerX = 672

    Y_paper_velocity += gravity
    paperY += Y_paper_velocity
    if paperY > 608:
        paperX = random.randint(50, 750)
        paperY = random.randint(0, 15)
        Y_paper_velocity = 2
        gravity = 0.05

    if player_rect.colliderect(paper_rect):
        paperX = random.randint(50, 750)
        paperY = random.randint(0, 15)
        Y_paper_velocity = 2
        gravity = 0.05
        score += 1
        collect_sound = mixer.Sound('data/music/collect_sound.wav')
        collect_sound.play()

    show_score(score_x, score_y)

    
    if paperY > 600:
        music = pygame.mixer.Sound('data/music/over.wav')
        music.play()
        mixer.music.play()
        game_over = pygame.image.load('data/images/game_over.jpg')
        screen.blit(game_over, (0, 200))
        pygame.display.flip()
        pygame.time.wait(2000)  
        mixer.music.load('data/music/background_music.mp3')
        mixer.music.play(-1)

    # To update the screen
    pygame.display.update()

# Quit the game
pygame.quit()