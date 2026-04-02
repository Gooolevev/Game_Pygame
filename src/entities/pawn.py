import math
from src.core.game_map import GameMap
from src.defs.models import BasePawnDef



class Pawn:
    def __init__(self, pawn_id: str, x: float, y: float, definition: BasePawnDef):
        self.pawn_id = pawn_id
        self.def_data = definition
        
        self.x = float(x)
        self.y = float(y)
        
        self.health = definition.base_health
        self.hunger = 100.0
        self.energy = 100.0
        
        self.path = []
        self.target_tile = None 

    def update(self, dt: float, game_map: GameMap):
        """Логика обновления (ИИ и движение)"""
        self._update_needs(dt)
        self._move(dt)

    def _update_needs(self, dt: float):
        self.hunger -= 0.01 * dt
        self.energy -= 0.005 * dt

    def _move(self, dt: float):
        if not self.path:
            return

        tx, ty = self.path[0]
        dx = tx - self.x
        dy = ty - self.y
        dist = math.hypot(dx, dy)

        speed = self.def_data.base_speed * dt
        
        if dist < speed:
            self.x, self.y = tx, ty
            self.path.pop(0)
        else:
            self.x += (dx / dist) * speed
            self.y += (dy / dist) * speed