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
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])   
class game_board():
    def __init__(self):
        self.clear()
        self.letters = []
        self.box_bank = self.create_bank()
        self.select_word()
        self.the_word = "TOKEN"
        self.guesses = 0
        self.draw_boxes()
        self.tile_pos = 0
        self.check
        self.in_word_list
        self.same_letters

    def in_word_list(self, guess):
        return True
    
    def same_letters(self, guess):
        for key, val in enumerate(self.the_word):
            for k , v in enumerate(guess):
                if key == k and val == v:
                    self.letters[key][3] = True
        for key, el in enumerate(guess):
            if el in self.the_word:
                self.letters[key + (5 * self.guesses)][2] = True

    def check(self):
        guess = ""
        for el in self.letters:
            guess += el[1]
        if guess == self.the_word:
            print("YOU WIN")
        else:
            if self.in_word_list(guess):
                self.same_letters(guess)



    def create_letter(self, pressed_key):
        letter = pygame.font.SysFont("comicsansms", 64)
        letter_font = letter.render(pressed_key, True, (255, 255, 255))
        self.letters.append([letter_font, pressed_key, False, False])

    def draw_boxes(self):
        for key, box in enumerate(self.box_bank):
            pygame.draw.rect(screen, (0,0,0), (box[0], box[1], box[2], box[3]))
            for k, v in enumerate(self.letters):
                if key == k:
                    if self.letters[k][2] and self.letters[k][3]:
                        pygame.draw.rect(screen, (0,128,0), (box[0], box[1], box[2], box[3]))
                    elif self.letters[k][2] and not self.letters[k][3]:
                        pygame.draw.rect(screen, (128,128,0), (box[0], box[1], box[2], box[3]))
                    screen.blit(v[0], (box[0] + 5, box[1]))
        pygame.display.update()

    def draw_letters(self):
        pass

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
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.MOUSEBUTTONUP:
                clicked = pygame.mouse.get_pos()

            if welcome_screen.play:
                if event.type == pygame.KEYDOWN: 
                    if event.key == pygame.K_a:
                        game_board.create_letter('A') 
                    if event.key == pygame.K_b:
                        game_board.create_letter('B')
                    if event.key == pygame.K_c:
                        game_board.create_letter('C')
                    if event.key == pygame.K_d:
                        game_board.create_letter('D')
                    if event.key == pygame.K_e:
                        game_board.create_letter('E')
                    if event.key == pygame.K_f:
                        game_board.create_letter('F')
                    if event.key == pygame.K_g:
                        game_board.create_letter('G')
                    if event.key == pygame.K_h:
                        game_board.create_letter('H')
                    if event.key == pygame.K_i:
                        game_board.create_letter('I')
                    if event.key == pygame.K_j:
                        game_board.create_letter('J')
                    if event.key == pygame.K_k:
                        game_board.create_letter('K')
                    if event.key == pygame.K_l:
                        game_board.create_letter('L')
                    if event.key == pygame.K_m:
                        game_board.create_letter('M')
                    if event.key == pygame.K_n:
                        game_board.create_letter('N')                        
                    if event.key == pygame.K_o:
                        game_board.create_letter('O')
                    if event.key == pygame.K_p:
                        game_board.create_letter('P')
                    if event.key == pygame.K_q:
                        game_board.create_letter('Q')
                    if event.key == pygame.K_r:
                        game_board.create_letter('R')
                    if event.key == pygame.K_s:
                        game_board.create_letter('S')
                    if event.key == pygame.K_t:
                        game_board.create_letter('T')
                    if event.key == pygame.K_u:
                        game_board.create_letter('U')
                    if event.key == pygame.K_v:
                        game_board.create_letter('V')
                    if event.key == pygame.K_w:
                        game_board.create_letter('W')
                    if event.key == pygame.K_x:
                        game_board.create_letter('X')
                    if event.key == pygame.K_y:
                        game_board.create_letter('Y')
                    if event.key == pygame.K_z:
                        game_board.create_letter('Z')
                    if event.key == pygame.K_BACKSPACE:
                        if len(game_board.letters) > 0:
                            game_board.letters.pop()
                    if event.key == pygame.K_RETURN:
                        if len(game_board.letters) % 5 == 0:
                            game_board.check()
                        else:
                            print("NOT CMPLEATE")


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