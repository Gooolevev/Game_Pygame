from config.settings import WORLD_WIDTH, WORLD_HEIGHT

class Camera:
    """Камера для отрисовки видимой области"""
    def __init__(self, screen_w: int, screen_h: int, tile_size: int):
        self.x = 0
        self.y = 0
        self.screen_w = screen_w
        self.screen_h = screen_h
        self.tile_size = tile_size

    def world_to_screen(self, wx: int, wy: int) -> tuple[int, int]:
        """Координаты мира → координаты экрана"""
        return wx * self.tile_size - self.x, wy * self.tile_size - self.y

    def update(self, target_x: int, target_y: int, map_w: int, map_h: int):
        """Камера следует за целью"""
        self.x = target_x * self.tile_size - self.screen_w // 2
        self.y = target_y * self.tile_size - self.screen_h // 2
        
        map_px_w = map_w * self.tile_size
        map_px_h = map_h * self.tile_size
        self.x = max(0, min(self.x, map_px_w - self.screen_w))
        self.y = max(0, min(self.y, map_px_h - self.screen_h))

    def get_visible_range(self) -> tuple[int, int, int, int]:
        """Какие клетки видны на экране (для оптимизации отрисовки)"""
        start_x = max(0, self.x // self.tile_size)
        start_y = max(0, self.y // self.tile_size)
        end_x = min(WORLD_WIDTH, (self.x + self.screen_w) // self.tile_size + 1)
        end_y = min(WORLD_HEIGHT, (self.y + self.screen_h) // self.tile_size + 1)
        return start_x, start_y, end_x, end_y
