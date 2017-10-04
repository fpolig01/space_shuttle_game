import pygame,time

pygame.init()

display_width = 800
display_height = 600

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)

car_width = 105

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("Frans Space Game")
clock = pygame.time.Clock()

space_shuttle_img = pygame.image.load('space_shuttle_3_alpha.png')


def shuttle(x, y):
    gameDisplay.blit(space_shuttle_img, (x, y))


def message_display(text):
    font = pygame.font.Font('freesansbold.ttf', 115)
    gameDisplay.blit(font.render(text, True, (0, 0, 0)), ((display_width / 2) - len(text) * 32, 50))
    pygame.display.update()
    time.sleep(2)

    game_loop()


def game_loop():

    x = display_width * 0.45
    y = display_height * 0.7

    x_change = 0

    game_exit = False

    while not game_exit:

        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

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

        if x > display_width - car_width or x < 0:
            message_display('You Crashed')


        pygame.display.update()
        clock.tick(60)


game_loop()
pygame.quit()
quit()