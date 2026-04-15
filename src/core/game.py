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

        self.ui_manager = UIManager()
        self.ui_font = pygame.font.SysFont("arial", 18, bold=True)
        self.small_ui_font = pygame.font.SysFont("arial", 14, bold=True)
        self.resources = {"wood": 0, "stone": 0, "food": 0}

        self.camera = Camera(SCREEN_WIDTH, SCREEN_HEIGHT, TILE_SIZE, WORLD_WIDTH, WORLD_HEIGHT)
        self.camera.follow(WORLD_WIDTH // 2, WORLD_HEIGHT // 2)

        self.pawns = self.game_map._spawn_initial_colonists()
        self.selected_pawns = self.pawns[0]
        self.pathfinder = Pathfinder(self.game_map)

        self.show_fps = True
        self.debug_text = []

    def get_pawn_at(self, mouse_x, mouse_y):
        wx = (mouse_x + self.camera.x) / TILE_SIZE
        wy = (mouse_y + self.camera.y) / TILE_SIZE

        for pawn in self.pawns:
            if pawn.covers_point(wx, wy):
                return pawn
        
        return None

        


    def run(self):
        pass


