import pygame

pygame.init()

display_width = 800
display_height = 600

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("Franman's Game")
clock = pygame.time.Clock()

space_shuttle_img = pygame.image.load('space_shuttle_3_alpha.png')


x = display_width * 0.45
y = display_height * 0.7

x_change = 0


def shuttle(x, y):
    gameDisplay.blit(space_shuttle_img, (x, y))
a

crashed = False

while not crashed:

    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            crashed = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_change = -5
            elif event.key == pygame.K_RIGHT:
                x_change = 5

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                x_change = 0

    x += x_change
    print(x)

    gameDisplay.fill(white)
    shuttle(x, y)
    pygame.display.update()
    clock.tick(60)

pygame.quit()
quit()