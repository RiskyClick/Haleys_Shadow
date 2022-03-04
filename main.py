# Simple pygame program

# Import and initialize the pygame library
from re import A
from telnetlib import PRAGMA_HEARTBEAT
import pygame
import json
import random
SCREEN_WIDTH = 500
SCREEN_HEIGHT = 750
pygame.init()

# Set up the drawing window
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])   


class game_board():
    def __init__(self, ):
        self.clear()
        self.box_bank = self.create_bank()
        self.select_word()
        self.the_word= ""
        self.guesses = 5
        self.draw_boxes()
        self.tile_pos = 0
        self.letters = []

    def create_letter(self, pressed_key):
        letter = pygame.font.SysFont("comicsansms", 24)
        letter_font = letter.render(pressed_key, True, (128, 128, 128))
        self.letters.append([self.tile_pos, letter_font])

    def draw_boxes(self):
        for key, i in enumerate(self.box_bank):
            pygame.draw.rect(screen, (0,0,0), (i[0], i[1], i[2], i[3]))
            for k, v in enumerate(self.letters):
                if key == k:
                    screen.blit(v[1], (i[0], i[1]))
 
        pygame.display.update()


    def clear(self):
        screen.fill((128, 128, 128))
        
    def create_bank(self):
        bank = []
        for row in range(1, 6):
            for i in range(1, 6):
                bank.append((70 * i, 100 * row, 60, 90))
        return bank

    def select_word(self):
        self.the_word = "token"
            

    def not_in_list(self):
        pass

    def banner(self):
        pass

class welcome():
    def __init__(self, clicked):
        self.clicked = clicked
        self.draw_banner()
        self.play_button()
        self.clicked_play(clicked)
        self.play = False
        

    def draw_banner(self):
        welcome_font = pygame.font.SysFont("comicsansms", 50)
        welcome_banner = welcome_font.render("Welcome", True, (0, 128, 0))
        screen.blit(welcome_banner, (SCREEN_WIDTH / 2 - welcome_banner.get_width() / 2, welcome_banner.get_height() / 2))
    
    def play_button(self):
        pygame.draw.rect(screen, (0,0,0),(SCREEN_WIDTH / 2 - 50, SCREEN_HEIGHT / 2 - 12, 100, 25))
        play_text = pygame.font.SysFont("comicsansms", 24)
        play_button_font = play_text.render("PLAY", True, (128, 128, 128))
        screen.blit(play_button_font, (SCREEN_WIDTH / 2 - 30, SCREEN_HEIGHT / 2 - 17))
    
    def clicked_play(self, clicked):
        mouse = pygame.mouse.get_pos()
        if 300 > mouse[0] > 200 and 390 > mouse[1] > 360:
            pygame.draw.rect(screen, (128,0,0),(SCREEN_WIDTH / 2 - 50, SCREEN_HEIGHT / 2 - 12, 100, 25))
            play_text = pygame.font.SysFont("comicsansms", 24)
            play_button_font = play_text.render("PLAY", True, (0, 0, 0))
            screen.blit(play_button_font, (SCREEN_WIDTH / 2 - 30, SCREEN_HEIGHT / 2 - 17))
            if mouse[0] == clicked[0] and mouse[1] == clicked[1]:
                self.play = True

        
# Run until the user asks to quit
running = True
class whatever:
    clicked = (0, 0)
    welcome_screen = welcome(clicked)
    game_board = game_board()
    pressed_key = ""
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.MOUSEBUTTONUP:
                clicked = pygame.mouse.get_pos()

            if welcome_screen.play:
                if event.type == pygame.KEYDOWN: 
                    if event.key == pygame.K_a:
                        pressed_key = 'A' 
                    if event.key == pygame.K_b:
                        pressed_key = 'B'
                    if event.key == pygame.K_c:
                        pressed_key = 'C'
                    if event.key == pygame.K_d:
                        pressed_key = 'D'
                    if event.key == pygame.K_e:
                        pressed_key = 'E'
                    if event.key == pygame.K_f:
                        pressed_key = 'F'
                    if event.key == pygame.K_g:
                        pressed_key = 'G'
                    if event.key == pygame.K_h:
                        pressed_key = 'H'
                    if event.key == pygame.K_i:
                        pressed_key = 'I'
                    if event.key == pygame.K_j:
                        pressed_key = 'J'
                    if event.key == pygame.K_k:
                        pressed_key = 'K'
                    if event.key == pygame.K_l:
                        pressed_key = 'L'
                    if event.key == pygame.K_m:
                        pressed_key = 'M'
                    if event.key == pygame.K_n:
                        pressed_key = 'N'                        
                    if event.key == pygame.K_o:
                        pressed_key = 'O'
                    if event.key == pygame.K_p:
                        pressed_key = 'P'
                    if event.key == pygame.K_q:
                        pressed_key = 'Q'
                    if event.key == pygame.K_r:
                        pressed_key = 'R'
                    if event.key == pygame.K_s:
                        pressed_key = 'S'
                    if event.key == pygame.K_t:
                        pressed_key = 'T'
                    if event.key == pygame.K_u:
                        pressed_key = 'U'
                    if event.key == pygame.K_v:
                        pressed_key = 'V'
                    if event.key == pygame.K_w:
                        pressed_key = 'W'
                    if event.key == pygame.K_x:
                        pressed_key = 'X'
                    if event.key == pygame.K_y:
                        pressed_key = 'Y'
                    if event.key == pygame.K_z:
                        pressed_key = 'Z'
                    game_board.create_letter(pressed_key)

        # Fill the background with white
        screen.fill((255, 255, 255))
        font = pygame.font.SysFont("comicsansms", 72)
        if welcome_screen.play:
            game_board.clear()
            game_board.draw_boxes()
        else:
            welcome_screen.draw_banner()
            welcome_screen.play_button()
            welcome_screen.clicked_play(clicked)
            pygame.display.update()
        
        # Flip the display
        pygame.display.flip()

    # Done! Time to quit.
    pygame.quit()