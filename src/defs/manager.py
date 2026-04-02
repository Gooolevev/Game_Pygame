import pygame
from src.defs.defs_items import ITEMS
from src.defs.defs_maps import TILES_MAP, OBJECT_MAP


class DefManager:
    def __init__(self):
        self.items = ITEMS
        self.tiles = TILES_MAP
        self.objects = OBJECT_MAP
        self.images = {}

        self.tiles_str_to_int = {"grass": 0, "sand": 1, "water": 2, "plowland": 3,"rock_granite": 4}
        self.tiles_int_to_str = {v: k for k, v in self.tiles_str_to_int.items()}
        
        self.obj_str_to_int = {"none": 0, "tree": 1, "rock": 2, "wall_wood": 3, "wall_stone": 4}
        self.obj_int_to_str = {v: k for k, v in self.obj_str_to_int.items()}

    def load_all_assets(self):
        """Загружает все картинки, указанные в дефах"""
        all_defs = (
            list(self.items.values())
            + list(self.tiles.values())
            + list(self.objects.values())
        )

        for d in all_defs:
            try:
                full_path = f"assets/images/{d.image_path}"
                img = pygame.image.load(full_path).convert_alpha()
                img = pygame.transform.scale(img, d.visual_size)
                self.images[d.id] = img
            except Exception as e:
                print(f"⚠️ Нет картинки для {d.id}: {e}")

    def get_image(self, def_id):
        return self.images.get(def_id)


image = DefManager()