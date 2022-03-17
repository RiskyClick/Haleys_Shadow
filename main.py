import pygame
import json
import random


SCREEN_WIDTH = 500
SCREEN_HEIGHT = 750
pygame.init()
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])   


fart1 = pygame.mixer.Sound("sounds/rude-raspberry.wav")
fart2 = pygame.mixer.Sound("sounds/balloon_on_the_loose.wav")
fart3 = pygame.mixer.Sound("sounds/balloon-fart.wav")
fart4 = pygame.mixer.Sound("sounds/fartysnap.wav")
fart5 = pygame.mixer.Sound("sounds/R2D2-fart.wav")
fart6 = pygame.mixer.Sound("sounds/R2D2-fart2.wav")
divawav = pygame.mixer.Sound("sounds/diva-bwaaaow-chorus.wav")
diva = True

class win_game():
    def __init__(self):
        self.game_over_banner
    
    def game_over_banner(self, word):
        win_font = pygame.font.SysFont("comicsansms", 35)
        win_banner = win_font.render("CONGRADULATIONS!", True, (0, 128, 0))
        screen.blit(win_banner, (SCREEN_WIDTH / 2 - win_banner.get_width() / 2, win_banner.get_height() / 2 + 200))
        font = pygame.font.SysFont("comicsansms", 35)
        banner = font.render("The Secret Word Was!", True, (0, 128, 0))
        screen.blit(banner, (SCREEN_WIDTH / 2 - banner.get_width() / 2, banner.get_height() / 2 + 250))
        word_font = pygame.font.SysFont("comicsansms", 35)
        word_banner = word_font.render(word, True, (0, 128, 0))
        screen.blit(word_banner, (SCREEN_WIDTH / 2 - word_banner.get_width() / 2, word_banner.get_height() / 2 + 300))
        
class game_board():
    def __init__(self):
        self.win = False
        self.clear()
        self.letters = []
        self.box_bank = self.create_bank()
        self.select_word()
        self.the_word, self.the_list = self.select_word()
        self.guesses = 0
        self.nots = False
        self.not_list = False
        self.draw_boxes()
        self.tile_pos = 0
        self.check
        self.not_in_word_list
        self.same_letters
        self.not_compleate
        self.play_fart

    def play_fart(self):
        num = random.randint(1, 6)
        if num == 1:
            pygame.mixer.Sound.play(fart1)
        elif num == 2:
            pygame.mixer.Sound.play(fart2)
        elif num == 3:
            pygame.mixer.Sound.play(fart3)
        elif num == 4:
            pygame.mixer.Sound.play(fart4)
        elif num == 5:
            pygame.mixer.Sound.play(fart5)
        else:
            pygame.mixer.Sound.play(fart6)
        
    def not_compleate(self):
        not_font = pygame.font.SysFont("comicsansms", 35)
        not_banner = not_font.render("Thats not 5 lettars idot!", True, (0, 128, 0))
        screen.blit(not_banner, (SCREEN_WIDTH / 2 - not_banner.get_width() / 2, not_banner.get_height() / 2 + 600))

    def not_in_word_list(self):
        not_font = pygame.font.SysFont("comicsansms", 35)
        not_banner = not_font.render("NOT A WORD STOOPID!", True, (0, 128, 0))
        screen.blit(not_banner, (SCREEN_WIDTH / 2 - not_banner.get_width() / 2, not_banner.get_height() / 2 + 600))
    
    def same_letters(self, guess):
        for key, val in enumerate(self.the_word):
            for k , v in enumerate(guess):
                if key == k and val == v:
                    self.letters[key + (self.guesses * 5)][3] = True
        for key, el in enumerate(guess):
            if el in self.the_word:
                self.letters[key + (self.guesses * 5)][2] = True

    def check(self):
        guess = ""
        self.not_list = False
        for el in range(len(self.letters) - 5, len(self.letters)):
            guess += self.letters[el][1]
        if guess in self.the_list:
            if guess == self.the_word:
                self.win = True
                pygame.mixer.music.load('097_super-slappy-bass.wav')
                pygame.mixer.music.play(-1)
            else:
                self.same_letters(guess)
            self.guesses += 1
        else:
            self.letters = self.letters[:-5]
            self.not_list = True
            print(random.randint(1, 100) % 2)
            self.play_fart()

    def create_letter(self, pressed_key):
        letter = pygame.font.SysFont("comicsansms", 64)
        letter_font = letter.render(pressed_key, True, (255, 255, 255))
        self.letters.append([letter_font, pressed_key, False, False])

    def draw_boxes(self):
        for key, box in enumerate(self.box_bank):
            pygame.draw.rect(screen, (0,0,0), (box[0], box[1], box[2], box[3]), 5)
            for k, v in enumerate(self.letters):
                if key == k:
                    if self.letters[k][2] and self.letters[k][3]:
                        pygame.draw.rect(screen, (0,255,0), (box[0], box[1], box[2], box[3]), 5)
                    elif self.letters[k][2] and not self.letters[k][3]:
                        pygame.draw.rect(screen, (255,255,0), (box[0], box[1], box[2], box[3]), 5)
                    screen.blit(v[0], (box[0] + 5, box[1]))
        if self.nots:
            self.not_compleate()
        if self.not_list and self.nots == False:
            self.not_in_word_list()
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
        with open('word_list.json', 'r') as textFile:
            wordList = json.loads(textFile.read())
            secretWord = random.choice(wordList[0])
            wordList = set(wordList[1])
            print(secretWord)
            return secretWord, wordList


class end_game():
    def __init__(self):
        self.game_over_banner
        self.clicked_retry
        self.clicked_quit
        self.restart
    
    def restart(self, game_board):
        game_board.guesses = 0
        game_board.letters = []
        game_board.win = False
        diva = True
        game_board.the_word, game_board.the_list = game_board.select_word()
        pygame.mixer.music.pause()
    
    def game_over_banner(self, word):
        loser_font = pygame.font.SysFont("comicsansms", 50)
        loser_banner = loser_font.render("GAME OVER LOSER", True, (0, 128, 0))
        screen.blit(loser_banner, (SCREEN_WIDTH / 2 - loser_banner.get_width() / 2, loser_banner.get_height() / 2 + 75))
        should_font = pygame.font.SysFont("comicsansms", 50)
        should_banner = should_font.render("THE WORD IS", True, (0, 128, 0))
        screen.blit(should_banner, (SCREEN_WIDTH / 2 - should_banner.get_width() / 2, should_banner.get_height() / 2 + 175))
        word_font = pygame.font.SysFont("comicsansms", 50)
        word_banner = word_font.render(word, True, (0, 128, 128))
        screen.blit(word_banner, (SCREEN_WIDTH / 2 - word_banner.get_width() / 2, word_banner.get_height() / 2 + 275))
        
    def clicked_retry(self, clicked):
        pygame.draw.rect(screen, (0,0,0),(SCREEN_WIDTH / 2 - 125, SCREEN_HEIGHT / 2 + 50, 250, 50), 5)
        retry_text = pygame.font.SysFont("comicsansms", 40)
        retry_font = retry_text.render("Play Again?", True, (0, 0, 0))
        screen.blit(retry_font, (SCREEN_WIDTH / 2 - 100, SCREEN_HEIGHT / 2 + 40))
        mouse = pygame.mouse.get_pos()
        if 375 > mouse[0] > 125 and 475 > mouse[1] > 425:
            pygame.draw.rect(screen, (128,0,0),(SCREEN_WIDTH / 2 - 125, SCREEN_HEIGHT / 2 + 50, 250, 50), 5)
            retry_text = pygame.font.SysFont("comicsansms", 40)
            retry_font = retry_text.render("Play Again!", True, (0, 0, 0))
            screen.blit(retry_font, (SCREEN_WIDTH / 2 - 100, SCREEN_HEIGHT / 2 + 40))
            if mouse[0] == clicked[0] and mouse[1] == clicked[1]:
                return True
            return False

    def clicked_quit(self):
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
        welcome_banner = welcome_font.render("WORDLE", True, (0, 128, 0))
        screen.blit(welcome_banner, (SCREEN_WIDTH / 2 - welcome_banner.get_width() / 2, welcome_banner.get_height() / 2 + 50))
        welcome_font = pygame.font.SysFont("comicsansms", 50)
        welcome_banner = welcome_font.render("BUT WAAYYYY", True, (0, 128, 0))
        screen.blit(welcome_banner, (SCREEN_WIDTH / 2 - welcome_banner.get_width() / 2, welcome_banner.get_height() / 2 + 100))
        welcome_font = pygame.font.SysFont("comicsansms", 50)
        welcome_banner = welcome_font.render("WORSE", True, (0, 128, 0))
        screen.blit(welcome_banner, (SCREEN_WIDTH / 2 - welcome_banner.get_width() / 2, welcome_banner.get_height() / 2 + 150))
    
    def play_button(self):
        pygame.draw.rect(screen, (0,0,0),(SCREEN_WIDTH / 2 - 50, SCREEN_HEIGHT / 2 - 12, 100, 25), 5)
        play_text = pygame.font.SysFont("comicsansms", 24)
        play_button_font = play_text.render("PLAY", True, (128, 128, 128))
        screen.blit(play_button_font, (SCREEN_WIDTH / 2 - 30, SCREEN_HEIGHT / 2 - 17))
    
    def clicked_play(self, clicked):
        mouse = pygame.mouse.get_pos()
        if 300 > mouse[0] > 200 and 390 > mouse[1] > 360:
            pygame.draw.rect(screen, (128,0,0),(SCREEN_WIDTH / 2 - 50, SCREEN_HEIGHT / 2 - 12, 100, 25), 5)
            play_text = pygame.font.SysFont("comicsansms", 24)
            play_button_font = play_text.render("PLAY", True, (0, 0, 0))
            screen.blit(play_button_font, (SCREEN_WIDTH / 2 - 30, SCREEN_HEIGHT / 2 - 17))
            if mouse[0] == clicked[0] and mouse[1] == clicked[1]:
                self.play = True

        
running = True
class whatever:
    clicked = (0, 0)
    welcome_screen = welcome(clicked)
    game_board = game_board()
    game_over = end_game()
    win = win_game()
    
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
                            game_board.nots = False
                            game_board.not_list = False
                            game_board.check()
                        else:
                            game_board.play_fart()
                            game_board.nots = True

        screen.fill((255, 255, 255))
        font = pygame.font.SysFont("comicsansms", 72)
        if welcome_screen.play:
            if game_board.guesses >= 5:
                if diva:
                    diva = False
                    pygame.mixer.Sound.play(divawav)
                game_board.clear()
                end_game.game_over_banner(None, game_board.the_word)
                if end_game.clicked_retry(None, clicked):
                    end_game.restart(None, game_board)
                pygame.display.update()
            elif game_board.win:
                game_board.clear()
                win_game.game_over_banner(None, game_board.the_word)
                if end_game.clicked_retry(None, clicked):
                    end_game.restart(None, game_board)
            else:
                game_board.clear()
                game_board.draw_boxes()
                pygame.display.update()
        else:
            welcome_screen.draw_banner()
            welcome_screen.play_button()
            welcome_screen.clicked_play(clicked)
            pygame.display.update()
        pygame.display.flip()
    pygame.quit()