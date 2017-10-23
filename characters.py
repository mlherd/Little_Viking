import pygame

class Character(object):
    
    def __init__ (self, x, y):
        self.hp = 100
        self.x = x
        self.y = y
        self.screen_x = 32 * x
        self.screen_y = 32 * y
        self.id = None
        
    def update_location(self, loc_x, loc_y):
        self.x = self.x + loc_x
        self.y = self.y + loc_y
        
        return True
        
    def get_location(self):
        return self.x, self.y
    
    def get_character_info(self):
        return self.hp, self.x, self.y, 
    
    def update_hp(self, point):
        self.hp = self.hp + point
        return True
        
    def get_image(self):
        return self.image
    
    def get_id(self):
        return self.id
       
class Viking (Character):
    
    def __init__ (self, x, y):
        super(Viking, self).__init__(x, y)
        self.id = 1
        self.hp = 200
        
class Enemy(Character):
    
    def __init__ (self, x, y, id, hp):
        super(Enemy, self).__init__(x, y)
        self.id = id
        self.hp = hp

class Food(Character):
    
    def __init__ (self, x, y, id):
        super(Food, self).__init__(x, y)
        self.id = id
