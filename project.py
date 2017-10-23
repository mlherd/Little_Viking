import game
import pygame
from vicky import record_voice, speech_recognition
import os

# set the enviroment variables for the speech recognition library
os.environ["LD_LIBRARY_PATH"] = "/usr/local/lib"
os.environ["PKG_CONFIG_PATH"] = "/usr/local/lib/pkgconfig"

# set the sound settings for pygame.sound
pygame.mixer.init(22050, -16, 2, 4096)

# creat a new game
new_game = game.Game()
new_game.initilize()
new_game.food_creator(5)

#game loop
while True:
    new_game.fill_display()
    #record_voice()
    #result = speech_recognition()
    result = "nope"
    new_game.event(result)
