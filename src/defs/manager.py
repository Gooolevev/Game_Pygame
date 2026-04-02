import pygame
from src.defs.defs_items import ITEMS
from src.defs.defs_maps import TILES_MAP, OBJECT_MAP


class DefManager:
    def __init__(self):
        self.items = ITEMS
        self.tiles = TILES_MAP
        self.objects = OBJECT_MAP
        self.images = {}


    def load_all_assets(self):
        """Загружает все картинки, указанные в assests"""
        all_defs = (list(self.items.values()) + list(self.tiles.values()) + list(self.objects.values()))

        for d in all_defs:
            try:
                full_path = f"assets/images/{d.image_path}"
                img = pygame.image.load(full_path).convert_alpha()
                img = pygame.transform.scale(img, d.visual_size)
                self.images[d.id] = img
            except Exception as e:
                print(f"⚠️ Нет картинки для {d.id}: {e}")
                surf = pygame.Surface(d.visual_size)
                surf.fill((255, 0, 255))
                self.images[d.id] = surf

    def get_image(self, def_id):
        return self.images.get(def_id)


image = DefManager()