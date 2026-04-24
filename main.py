import sys
import os
import json
import random

import pygame
import pygame_gui

from pydantic import BaseModel, Field, PositiveInt
from opensimplex import OpenSimplex

from pathfinding.core.grid import Grid
from pathfinding.finder.a_star import AStarFinder

from src import ITEMS, TILES_MAP, OBJECT_MAP, PAWNS, BUILD, COOK, image
from src.core.game import Game
from config import settings

if __name__ == "__main__":
    game = Game()
    game.run()


