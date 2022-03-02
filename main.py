# Simple pygame program

# Import and initialize the pygame library
import pygame
SCREEN_WIDTH = 500
SCREEN_HEIGHT = 750
pygame.init()

# Set up the drawing window
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])

def welcome():
    red = (200,0,0)
    green = (0,200,0)

    bright_red = (255,0,0)
    bright_green = (0,255,0)
    mouse = pygame.mouse.get_pos()
    welcome_font = pygame.font.SysFont("comicsansms", 50)
    welcome_banner = welcome_font.render("Welcome", True, (0, 128, 0))
    screen.blit(welcome_banner, (SCREEN_WIDTH / 2 - welcome_banner.get_width() / 2, welcome_banner.get_height() / 2))
    
    pygame.draw.rect(screen, (0,0,0),(SCREEN_WIDTH / 2 - 50,
                                      SCREEN_HEIGHT / 2 - 12,
                                      100, 25))
    play_text = pygame.font.SysFont("comicsansms", 24)
    play_button_font = play_text.render("PLAY", True, (0, 128, 0))
    #play_button.fill((0, 0, 0))
    #screen.blit(play_button, (SCREEN_WIDTH / 2 - 50, SCREEN_HEIGHT / 2 - 12))
    screen.blit(play_button_font, (SCREEN_WIDTH / 2 - 30, SCREEN_HEIGHT / 2 - 17))

    if 150+100 > mouse[0] > 150 and 450+50 > mouse[1] > 450:
        print(mouse[0], mouse[1])
        pygame.draw.rect(screen, bright_green,(150,450,100,50))
        pygame.draw.rect(screen, (0,0,0),(SCREEN_WIDTH / 2 - 50,
                                    SCREEN_HEIGHT / 2 - 12,
                                    100, 25))
    else:
        pygame.draw.rect(screen, green,(150,450,100,50))
        play_button_font = play_text.render("PLAY", True, (0, 128, 0))
        pygame.draw.rect(screen, (0,128,0),(SCREEN_WIDTH / 2 - 50,
                                    SCREEN_HEIGHT / 2 - 12,
                                    100, 25))
    pygame.draw.rect(screen, red,(550,450,100,50))
    pygame.display.update()

# Run until the user asks to quit
running = True
class whatever:
    while running:

        # Did the user click the window close button?
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False


        # Fill the background with white
        screen.fill((255, 255, 255))
        font = pygame.font.SysFont("comicsansms", 72)

        welcome()
        
        # Flip the display
        pygame.display.flip()

    # Done! Time to quit.
    pygame.quit()