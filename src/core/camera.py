from config.settings import SCREEN_WIDTH, SCREEN_HEIGHT


class Camera:
    def __init__(self, screen_widht: int, screen_height: int, tile_size: int, map_widht: int, map_height: int) -> tuple[int, int]:
        self.x = 0
        self.y = 0
        self.screen_widht = screen_widht
        self.screen_height = screen_height
        self.tile_size = tile_size
        self.map_widht = map_widht
        self.map_height = map_height

    def world_to_screen(self, world_x: int, world_y: int) -> tuple[int, int]:
        return ((world_x * self.tile_size - self.x), (world_y * self.tile_size - self.y))

    def screen_to_world(self, screen_x: int, screen_y: int) -> tuple[float, float]:
        return (((screen_x + self.x) / self.tile_size), ((screen_y + self.y) / self.tile_size))

    def follow(self, target_x: float, target_y: float) -> None:
        self.x = target_x * self.tile_size - self.screen_widht // 2
        self.y = target_y * self.tile_size - self.screen_height // 2
        self.clamp()
    
    def move(self, distance_x: float, distance_y: float) -> None:
        self.x += distance_x
        self.y += distance_y
        self.clamp()
    
    def clamp(self) -> None:
        max_x = self.map_widht * self.tile_size - self.screen_widht
        max_y = self.map_height * self.tile_size - self.screen_height
        self.x = max(0.0, min(self.x, max_x))
        self.y = max(0.0, min(self.y, max_y))
    
    def get_visible_range(self) -> tuple[int, int, int, int]:
        start_x = max(0, int(self.x // self.tile_size))
        start_y = max(0, int(self.y // self.tile_size))
        end_x = min(self.map_widht, int((self.x + self.screen_widht) // self.tile_size) + 1)
        end_y = min(self.map_height, int((self.y + self.screen_height) // self.tile_size) + 1)
        return (start_x, start_y, end_x, end_y)





    
