import math
from src.core.game_map import GameMap
from src.defs.models import BasePawnDef


class Pawn:
    def __init__(self, pawn_id: str, x: float, y: float, definition: BasePawnDef):
        self.pawn_id = pawn_id
        self.def_data = definition

        self.x = x
        self.y = y

        self.health = 100.0
        self.hunger = 100.0

        self.path = []
        self.target_tile = None

    def update(self, tick: float, game_map: GameMap):
        """Logic updates (AI and movement)"""
        self._update_needs(tick)
        self._move(tick)

    def _update_needs(self, tick: float):
        self.hunger -= 0.01 * tick
        self.energy -= 0.005 * tick

    def _move(self, tick: float):
        if not self.path:
            return

        print(
            f"Pawn {self.pawn_id} moving to {self.path[0]}, now in ({self.x:.2f}, {self.y:.2f})"
        )

        tx, ty = self.path[0]
        dx = tx - self.x
        dy = ty - self.y
        dist = math.hypot(dx, dy)

        speed = self.def_data.base_speed * tick

        if dist < speed:
            self.x, self.y = tx, ty
            self.path.pop(0)
        else:
            self.x += (dx / dist) * speed
            self.y += (dy / dist) * speed
