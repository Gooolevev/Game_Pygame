import array
import random
from opensimplex import OpenSimplex
from config.settings import WORLD_HEIGHT, WORLD_WIDTH
from src.defs.defs_pawn import PAWNS
from entities.pawn import Pawn



class GameMap:
    def __init__(self, widht, height, defs):
        self.width = widht
        self.height = height
        self.defs = defs

        self.total_tiles = self.width * height
        self.tile = array.array("H", self.total_tiles *[0])
        self.objects = array.array("H", self.total_tiles *[0])
        self.buildings = array.array("H", self.total_tiles *[0])

    def get_index(self, x, y):
        return self.width * x + y
    
    def _generate(self):
        gen = OpenSimplex(seed=random.randint(1, 99999))
        scale = 60.0
        
        for y in range(self.height):
            for x in range(self.width):
                index = self.get_index(x,y)
                noise = gen.noise2(x / scale, y / scale)

                if noise < -0.1:
                    self.tile[index] = self.defs.tiles_str_to_int["water"]
                elif noise < 0.0:
                    self.tile[index] = self.defs.tiles_str_to_int["sand"]
                elif noise > 0.3:
                    self.tile[index] = self.defs.tiles_str_to_int["rock_granite"]
                else:
                    self.tile[index] = self.defs.tiles_str_to_int["grass"]
                
                if noise > 0.1 and random.random() < 0.08 and self.tile[index] != 4:
                    self.objects[index] = self.defs.obj_str_to_int["tree"]
                
                if noise > 0.1 and random.random() < 0.04 and self.tile[index] != 4:
                    self.objects[index] = self.defs.obj_str_to_int["rock"]

    def _spawn_initial_colonists(self):
        cx, cy = WORLD_WIDTH // 2, WORLD_HEIGHT // 2
        start_pos = [(cx, cy),(cx + 1, cy),(cx + 2, cy)]
        new_colonist = []

        for i, (px, py) in enumerate(start_pos):
            pawn_def = PAWNS[f"pawn_{i}"]
            new_pawn = Pawn(f"colonist_{i}", px, py, pawn_def)
            new_colonist.append(new_pawn)
            
        return new_colonist
                
    def is_valid(self, x, y):
        return 0 <= x < self.width and 0 <= y < self.height
    
    def is_passable(self, x, y):
        if not self.is_valid(x, y):
            return False
        
        index = self.get_index(x, y)

        b_id = self.buildings[index]
        if b_id != 0:
            b_str = self.defs.obj_int_to_str.get(b_id)
            b_def = self.defs.objects.get(b_str)
            if b_def and not b_def.passable:
                return False
            
        o_id = self.objects[index]
        if o_id != 0:
            o_str = self.defs.obj_int_to_str.get(o_id)
            o_def = self.defs.objects.get(o_str)
            if o_def and not o_def.passable:
                return False

        
