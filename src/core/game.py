import pygame
import os
import sys

from config.settings import *
from src.defs.manager import DefManager
from src.ui.ui import UIManager
from src.core.game_map import GameMap
from src.systems.pathfinding import Pathfinder
from src.entities.pawn import Pawn

class Game:
    def __init__(self):
        print(Pathfinder())
