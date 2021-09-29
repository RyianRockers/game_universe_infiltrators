import random
import pygame


screen = pygame.display.set_mode((800, 600))
playerX = 370
playerY = 480
playerX_change = 0
enemyX = random.randint(0, 800)
enemyY = random.randint(50, 150)
enemyX_change = 1.5
enemyY_change = 50
playerImg = pygame.image.load('assets/condom.png')
enemyImg = pygame.image.load('assets/virus.png')
pygame.display.set_caption("Pussy Infiltrators")
icon = pygame.image.load('assets/condom_icon.png')
pygame.display.set_icon(icon)


def main():
    pygame_init()


def pygame_init():
    pygame.init()
    pygame_main_loop()


def player(x, y):
    global screen
    screen.blit(playerImg, (x, y))


def enemy(x, y):
    global screen
    screen.blit(enemyImg, (x, y))


def pygame_main_loop():
    global screen
    global playerX
    global playerY
    global playerX_change
    global enemyX
    global enemyY
    global enemyX_change
    global enemyY_change
    running = True

    while running:
        screen.fill((0, 0, 0))
        for event in pygame.event.get():
            #player movement
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    playerX_change = -1
                if event.key == pygame.K_RIGHT:
                    playerX_change = 1
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or pygame.K_RIGHT:
                    playerX_change = 0
            if event.type == pygame.QUIT:
                running = False

        playerX += playerX_change

        #player boundary
        if playerX <= 0:
            playerX = 0
        elif playerX >= 736:
            playerX = 736

        enemyX += enemyX_change

        #enemy boundary
        if enemyX <= 0:
            enemyX_change = 1
            enemyY += enemyY_change
        elif enemyX >= 736:
            enemyX_change = -1
            enemyY += enemyY_change

        player(playerX, playerY)
        enemy(enemyX, enemyY)

        pygame.display.update()


if __name__ == '__main__':
    main()
