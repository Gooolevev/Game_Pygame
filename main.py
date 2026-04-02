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
from config import settings
from src.core.logger_config import game_logger as logger


class Pawn:
    pass


class Stats:
    pass


class Inventory:
    pass


class TaskManager:
    pass


class Tile:
    pass


class GameMap:
    pass


class Camera:
    pass


class Item:
    pass


class Building:
    pass


class SelectionManager:
    pass


class OrderSystem:
    pass


class Game:
    pass

