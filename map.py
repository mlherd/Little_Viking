import pygame
from espeak import espeak
class Map():
    
    # initilize the map
    # width is the x axis
    # height is the y axis
    # grid[row][column] row = y column = x
    def __init__(self, width, height):
        self.grid = []
        self.width = width
        self.height = height
        self.viking_image = pygame.image.load('images/viking.bmp')
        self.meat_image =  pygame.image.load('images/meat.bmp')
        self.enemy_image = pygame.image.load('images/viking.bmp')
        self.meat_flag = 0

    # Creat 2D array
    
    def create_grid(self):
        for row in range(self.height):
            self.grid.append([])
            for column in range(self.width):
                self.grid[row].append(0)

    # Print the map on the console
    def print_map(self): 
        line = ""
        for row in range(self.height):
            for column in range(self.width):
                line = line + str(self.grid[row][column])
            print line
            line = ""

    # Add the floors to the map, 0 = map
    def draw_floor(self, screen, image):
        self.screen = screen
        self.floor_image = image
        rect = self.floor_image.get_rect()
        
        for row in range(self.height):
            for column in range(self.width):
                if self.grid[row][column] == 0:
                    rect.x = column * 32
                    rect.y = row * 32
                    self.screen.blit(self.floor_image, rect)
        return True
                    
    # Draw the characters on the map
    # 1 = Player
    # 2 = meat
    # 3 = Enemy
    def draw_characters(self, screen):
        self.screen = screen
        self.meat_flag = 0
        for row in range(self.height):
            for column in range(self.width):
                if self.grid[row][column] == 1:
                    rect = self.viking_image.get_rect()
                    rect.x = column * 32
                    rect.y = row * 32
                    self.screen.blit(self.viking_image, rect)
                
                elif self.grid[row][column] == 2:
                    rect = self.meat_image.get_rect()
                    rect.x = column * 32
                    rect.y = row * 32
                    self.screen.blit(self.meat_image, rect)
                    self.meat_flag = 1

                elif self.grid[row][column] == 3:
                    rect = self.enemy_image.get_rect()
                    rect.x = column * 32
                    rect.y = row * 32
                    self.screen.blit(self.enemy_image, rect)
        return True

    # check the location on the map if it is already occupied.
    def check_location(self, x, y):
        if self.grid[y][x] == 0:
            return True #everything is fine
        else:
            return False #you are in boundries, but there is an other object

    # check the next step the move
    # 0 = next step is empty
    # 1 = next step is in boundries, but there is an other object
    # 2 = next step is out of boundries
    
    def check_nextstep(self, current_location_x, current_location_y, next_location_x, next_location_y):
        if next_location_x < self.width and next_location_y < self.height and next_location_x >= 0 and next_location_y >= 0:
            if self.grid[next_location_y][next_location_x] == 0:
                return 0 #everything is fine
            else:
                return 1 #in boundries, but there is an other object
        return 2 # out of boundries
        
    def update(self, char_number, prev_location_x, prev_location_y, new_location_x, new_location_y):
        self.grid[prev_location_y][prev_location_x] = 0
        self.grid[new_location_y][new_location_x] = char_number
    
        return True 
