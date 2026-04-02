import random
import array
from src.defs.manager import DefManager
from src.systems.perlin_noise import PerlinNoise


class GameMap:
    """Управление всей картой через плоские массивы (Data Locality)"""

    def __init__(self, width: int, height: int, defs: DefManager):
        self.width = width
        self.height = height
        self.defs = defs

        total_tiles = width * height
        self.tile = array.array("H", [0] * total_tiles)
        self.objects = array.array("H", [0] * total_tiles)
        self.buildings = array.array("H", [0] * total_tiles)

        self._generate()

    def get_index(self, x: int, y: int) -> int:
        """Перевод 2D координат в 1D индекс"""
        return y * self.width + x

    def _generate(self):

        perlin = PerlinNoise(seed=random.randint(1, 99999))

        scale = 60

        for y in range(self.height):
            for x in range(self.width):
                idx = self.get_index(x, y)

                val = perlin.noise(x / scale, y / scale)

                if val < -0.1:
                    self.tile[idx] = self.defs.tiles_str_to_int["water"]
                elif val < 0.0:
                    self.tile[idx] = self.defs.tiles_str_to_int["sand"]
                elif val > 0.3:
                    self.tile[idx] = self.defs.tiles_str_to_int["rock_granite"]
                else:
                    self.tile[idx] = self.defs.tiles_str_to_int["grass"]

                    self.objects[idx] = self.defs.obj_str_to_int["none"]

                if val > 0.1 and random.random() < 0.08 and self.tile[idx] != 4:
                    self.objects[idx] = self.defs.obj_str_to_int["tree"]

    def is_valid(self, x: int, y: int) -> bool:
        return 0 <= x < self.width and 0 <= y < self.height

    def is_passable(self, x: int, y: int) -> bool:
        if not self.is_valid(x, y):
            return False

        idx = self.get_index(x, y)

        b_id = self.buildings[idx]
        if b_id != 0:
            b_str = self.defs.obj_int_to_str.get(b_id)
            b_def = self.defs.objects.get(b_str)
            if b_def and not b_def.passable:
                return False

        o_id = self.objects[idx]
        if o_id != 0:
            o_str = self.defs.obj_int_to_str.get(o_id)
            o_def = self.defs.objects.get(o_str)
            if o_def and not o_def.passable:
                return False

        return True
