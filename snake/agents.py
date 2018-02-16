import numpy as np
from pygame.locals import *
import pygame

def max_idx(a):
    one = a == np.max(a)
    col = np.argmax(one.max(axis=0))
    row = np.argmax(one[:,col])
    return row, col

def simple_agent(state):
    y_player, x_player = max_idx(state[:,:,0])
    y_apple, x_apple = max_idx(state[:,:,1])

    if y_player < y_apple:
        return "down"
    elif y_player > y_apple:
        return "up"
    elif x_player < x_apple:
        return "right"
    elif x_player > x_apple:
        return "left"

def keyboard_agent(state=None):
    keys = pygame.key.get_pressed()
    if (keys[K_RIGHT]):
        return "right"

    elif (keys[K_LEFT]):
        return "left"

    elif (keys[K_UP]):
        return "up"

    elif (keys[K_DOWN]):
        return "down"

    elif (keys[K_ESCAPE]):
        return "escape"
