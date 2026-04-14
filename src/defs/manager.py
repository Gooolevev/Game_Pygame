import pygame
import os
from src.defs.defs_items import ITEMS
from src.defs.defs_maps import TILES_MAP, OBJECT_MAP

class DefManager:
    def __init__(self):
        self.items = ITEMS
        self.tiles = TILES_MAP
        self.objects = OBJECT_MAP
        self.images = {}

        self.tiles_str_to_int = {"grass": 0, "sand": 1, "water": 2, "plowland": 3,"rock_granite": 4}
        self.tiles_int_to_str = {a: b for b, a in self.tiles_str_to_int.items()}

        self.obj_str_to_int = {"none": 0, "tree": 1, "rock": 2, "wall_wood": 3, "wall_stone": 4}
        self.obj_int_to_str = {a: b for b, a in self.obj_str_to_int.items()}

    def load_all_assets(self):
        "loaded all images, specified in defs"
        all_defs = (list(self.items.values()) + list(self.tiles.values()) + list(self.objects.values()))

        for d in all_defs:
            try:
                full_path = os.path.join("assets", "images", d.image_path)
                img = pygame.image.load(full_path).convert_alpha()
                img = pygame.transform.scale(img, d.visual_size)
                self.images[d.id] = img
            except Exception as e:
                self.images[d.id] = self._generate_fallback(d)
                print(f"⚠️ Нет картинки для {d.id}: {e}")    

    def _generate_fallback(self, d):
        w, h = d.visual_size
        surf = pygame.Surface((w, h), pygame.SRCALPHA)  
        
        if "rock" in d.id:
            cx, cy = w // 2, h // 2
            r = min(cx, cy) - 2
            pygame.draw.circle(surf, (75, 75, 85), (cx, cy), r)          # Основа
            pygame.draw.circle(surf, (55, 55, 65), (cx - 4, cy + 3), r - 4) # Тень
            pygame.draw.circle(surf, (95, 95, 105), (cx + 4, cy - 4), r - 6)# Блик
            return surf

    def get_image(self, def_id) -> pygame.Surface:
        return self.images.get(def_id)


image = DefManager()        