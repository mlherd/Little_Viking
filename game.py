import characters as char
import map as m
import sys
import pygame
import random
from espeak import espeak

class Game():
    
    def __init__ (self):
    
        self.screen = None
        self.player = None
        self.player_lcation_x = 1
        self.player_location_y = 1
        self.map = None
        self.BLACK = (0, 0, 0)
        self.WHITE = (255, 255, 255)
        self.GREEN = (0, 255, 0)
        self.RED = (255, 0, 0)  
        self.screen_height = 320
        self.screen_width = 480
        self.grid_x = 15
        self.grid_y = 10
        self.floor_image = pygame.image.load('images/floor.bmp')
        self.meat = pygame.image.load('images/meat.bmp')
        self.viking = pygame.image.load('images/viking.bmp')
        self.enemy_list = []
        self.food_list = []
        self.meat_flag = 0
        self.newgame_flag = 0
        self.food_number = 0
        self.point = 0
        self.info_text = ""
        self.walk_sound = pygame.mixer.Sound("sounds/walk.wav")
        self.eat_sound = pygame.mixer.Sound("sounds/eat.wav")
        self.new_level_sound = pygame.mixer.Sound("sounds/win.wav")

        
        self.background_color = self.BLACK
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption("Little Viking V 1.0")

    # update the score board
    def update_text(self, point):
        self.info_text = "Score: " + str(point)
        font = pygame.font.Font(None, 30)
        text = font.render(self.info_text, 1, (10, 10, 10))
        textpos = text.get_rect()
        textpos.x = 380
        textpos.y = 10
        self.screen.blit(text, textpos)

    # update game settings
    def update_settings(self, background_color, screen_height, screen_width, caption):  
        
        self.background_color = background_color
        self.screen_height = screen_height
        self.screen_width = screen_width
        pygame.display.set_caption(caption)
        
        return True

    # initilize game variables and create a new player
    def initilize(self):
    
        # player initial location
        self.player_location_x = 1
        self.player_location_y = 1
    
        #pygame settings
        pygame.init()
        #create a map
        self.map = m.Map(self.grid_x,self.grid_y)
        self.map.create_grid()
    
        #add player to the grid 
        self.player = char.Viking(self.player_location_x, self.player_location_y)
        self.map.update(self.player.get_id(), self.player.x, self.player.y, self.player.x, self.player.y)
        
        return True

    # check voice command and keyboard actions
    def event(self, command):
        if command == 'LEFT':
            if self.map.check_nextstep(self.player.x, self.player.y, self.player.x - 1, self.player.y) == 0:
                self.map.update(self.player.get_id(), self.player.x, self.player.y, self.player.x - 1, self.player.y)
                self.player.update_location (-1, 0)
                self.walk_sound.play(-1, 2000)
            elif  self.map.check_nextstep(self.player.x, self.player.y, self.player.x - 1, self.player.y) == 1:
                self.delete_food(self.player.x - 1, self.player.y)
                self.map.update(self.player.get_id(), self.player.x, self.player.y, self.player.x - 1, self.player.y)
                self.player.update_location (-1, 0)
                self.walk_sound.play(-1, 2000)
            elif self.map.check_nextstep(self.player.x, self.player.y, self.player.x - 1, self.player.y) == 2:
                espeak.synth("Ops I cannot move")
                
        elif command == 'RIGHT':
            if self.map.check_nextstep(self.player.x, self.player.y, self.player.x + 1, self.player.y) == 0:
                self.map.update(self.player.get_id(), self.player.x, self.player.y, self.player.x + 1, self.player.y)
                self.player.update_location (1, 0)
                self.walk_sound.play(-1, 2000)
            elif  self.map.check_nextstep(self.player.x, self.player.y, self.player.x + 1, self.player.y) == 1:
                self.delete_food(self.player.x + 1, self.player.y)
                self.map.update(self.player.get_id(), self.player.x, self.player.y, self.player.x + 1, self.player.y)
                self.player.update_location (1, 0)
                self.walk_sound.play(-1, 2000)
            elif  self.map.check_nextstep(self.player.x, self.player.y, self.player.x + 1, self.player.y) == 2:
                espeak.synth("Ops I cannot move")
                
        elif command == 'UP':
            if self.map.check_nextstep(self.player.x, self.player.y, self.player.x, self.player.y - 1) == 0:
                self.map.update(self.player.get_id(), self.player.x, self.player.y, self.player.x, self.player.y - 1)
                self.player.update_location (0, -1)
                self.walk_sound.play(-1, 2000)
            elif  self.map.check_nextstep(self.player.x, self.player.y, self.player.x, self.player.y - 1) == 1:
                self.delete_food(self.player.x, self.player.y - 1)
                self.map.update(self.player.get_id(), self.player.x, self.player.y, self.player.x, self.player.y - 1)
                self.player.update_location (0, -1)
                self.walk_sound.play(-1, 2000)
            elif  self.map.check_nextstep(self.player.x, self.player.y, self.player.x + 1, self.player.y) == 2:
                 espeak.synth("Ops I cannot move")
                 
        elif command == 'DOWN':
            if self.map.check_nextstep(self.player.x, self.player.y, self.player.x , self.player.y + 1) == 0:
                self.map.update(self.player.get_id(), self.player.x, self.player.y, self.player.x, self.player.y + 1)
                self.player.update_location (0, 1)
                self.walk_sound.play(-1, 2000)
            elif  self.map.check_nextstep(self.player.x, self.player.y, self.player.x, self.player.y + 1) == 1:
                self.delete_food(self.player.x, self.player.y + 1)
                self.map.update(self.player.get_id(), self.player.x, self.player.y, self.player.x, self.player.y + 1)
                self.player.update_location (0, 1)
                self.walk_sound.play(-1, 2000)
            elif  self.map.check_nextstep(self.player.x, self.player.y, self.player.x + 1, self.player.y) == 2:
                espeak.synth("Ops I cannot move")

        # TTS ffunctions - used espeak library         
        elif command == 'HOW ARE YOU':
            espeak.synth("I am great. How are you")
            
        elif command == 'WHAT IS YOUR NAME':
            espeak.synth("My name is Vicky")
            
        elif command == 'VICKY':
            espeak.synth("Yes, I am listening")

        else:
            self.walk_sound.stop()

        # keyboard actions
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    if self.map.check_nextstep(self.player.x, self.player.y, self.player.x - 1, self.player.y) == 0:
                        self.map.update(self.player.get_id(), self.player.x, self.player.y, self.player.x - 1, self.player.y)
                        self.player.update_location (-1, 0)
                elif event.key == pygame.K_RIGHT:
                    if self.map.check_nextstep(self.player.x, self.player.y, self.player.x + 1, self.player.y) == 0:
                        self.map.update(self.player.get_id(), self.player.x, self.player.y, self.player.x + 1, self.player.y)
                        self.player.update_location (1, 0)
                elif event.key == pygame.K_UP:
                    if self.map.check_nextstep(self.player.x, self.player.y, self.player.x, self.player.y - 1) == 0:
                        self.map.update(self.player.get_id(), self.player.x, self.player.y, self.player.x, self.player.y - 1)
                        self.player.update_location (0, -1)
                elif event.key == pygame.K_DOWN:
                    if self.map.check_nextstep(self.player.x, self.player.y, self.player.x , self.player.y + 1) == 0:
                        self.map.update(self.player.get_id(), self.player.x, self.player.y, self.player.x, self.player.y + 1)
                        self.player.update_location (0, 1)
                print "\n"
            
        return True

    # create foods and place them on map
    def food_creator(self, food_number):
        self.new_level_sound.play(-1, 3000)
        self.food_number = food_number
        for new_food in range(food_number):
            #find an empty spot for food
            flag = 0
            x = 0
            while flag == 0:
                x = random.randint(0,14)
                y = random.randint(0,9)
                if self.map.check_location(x, y) == True:
                    flag = 1
            self.map.update(2, x, y, x, y)
        return True

    # delete food from map
    def delete_food(self, dead_food_x, dead_food_y):
        self.map.update(0, dead_food_x, dead_food_y, dead_food_x , dead_food_y)
        self.point = self.point + 1
        self.eat_sound.play(-1, 2000)

    # draw everything on the screen   
    def fill_display(self):  
        self.screen.fill(self.background_color)
        self.map.draw_floor(self.screen, self.floor_image)
        self.map.draw_characters(self.screen)
        # if game is over add more food to the display
        if self.map.meat_flag == 0:
            self.food_creator(self.food_number + 2)
        self.update_text(self.point)
        pygame.display.flip()
        return True
