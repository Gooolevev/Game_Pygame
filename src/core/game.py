import pygame
import os
import sys

from config.settings import *
from src.defs.manager import DefManager
from src.ui.ui import UIManager
from src.core.game_map import GameMap
from src.systems.pathfinding import Pathfinder
from src.entities.pawn import Pawn
from src.core.camera import Camera

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Rimworld Lite")

        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.running = True

        self.defs = DefManager()
        self.game_map = GameMap(WORLD_WIDTH, WORLD_HEIGHT, self.defs)
        self.camera = Camera()
        self.pathfinder = Pathfinder(self.game_map)
        self.ui_manager = UIManager()



