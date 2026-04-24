import pygame
import os
import sys

from config.settings import *
from src.defs.manager import DefManager
from src.ui.ui import UIManager
from src.core.game_map import GameMap
from src.systems.pathfinding import Pathfinder
from src.entities.pawn import Pawn
from src.core.camera import Camera

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Rimworld Lite")

        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.running = True

        self.defs = DefManager()

        self.game_map = GameMap(WORLD_WIDTH, WORLD_HEIGHT, self.defs)

        self.ui_manager = UIManager()
        self.ui_font = pygame.font.SysFont("arial", 18, bold=True)
        self.small_ui_font = pygame.font.SysFont("arial", 14, bold=True)
        self.resources = {"wood": 0, "stone": 0, "food": 0}

        self.camera = Camera(SCREEN_WIDTH, SCREEN_HEIGHT, TILE_SIZE, WORLD_WIDTH, WORLD_HEIGHT)
        self.camera.follow(WORLD_WIDTH // 2, WORLD_HEIGHT // 2)

        self.pawns = self.game_map._spawn_initial_colonists()
        self.selected_pawn = self.pawns[0]
        self.pathfinder = Pathfinder(self.game_map)

        self.show_fps = True
        self.debug_text = []

    def get_pawn_at(self, mouse_x, mouse_y):
        wx = (mouse_x + self.camera.x) / TILE_SIZE
        wy = (mouse_y + self.camera.y) / TILE_SIZE

        for pawn in self.pawns:
            if pawn.covers_point(wx, wy):
                return pawn
        
        return None

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                mx, my = pygame.mouse.get_pos()

                if event.button == 1:
                    clicked_pawn = self.get_pawn_at(mx, my)
                    if clicked_pawn:
                        self.selected_pawn = clicked_pawn
                    else:
                        pass
                
                elif event.button == 3:
                    if self.selected_pawns:
                        wx, wy = self.camera.screen_to_world(mx, my)
                        target_tx, target_ty = int(wx), int(wy)

                        if self.game_map.is_valid(target_tx, target_ty):
                            path = self.pathfinder.find_path(int(self.selected_pawn.x),int(self.selected_pawn.y), target_tx, target_ty)
                            if path:
                                self.selected_pawn.path = path
    
    def update(self):
        dt = self.clock.tick(FPS) / 1000
        self._handle_camera_input(dt)

        for pawn in self.pawns:
            pawn.update(dt, self.game_map)

    def _handle_camera_input(self, dt):
        keys = pygame.key.get_pressed()
        speed = 1000 * dt 

        dx, dy = 0, 0
        if keys[pygame.K_w]: dy -= speed
        if keys[pygame.K_s]: dy += speed
        if keys[pygame.K_a]: dx -= speed
        if keys[pygame.K_d]: dx += speed

        if dx != 0 or dy != 0:
            self.camera.move(dx, dy)

    def draw(self):
        self.screen.fill(COLOR_BG)
        start_x, start_y, end_x, end_y = self.camera.get_visible_range()
        
        for y in range(int(start_y), int(end_y)):
            for x in range(int(start_x), int(end_x)):
                if not self.game_map.is_valid(x, y): continue
                    
                idx = self.game_map.get_index(x, y)
                screen_x, screen_y = self.camera.world_to_screen(x, y)
                
                tile_id = self.game_map.tile[idx]
                tile_str = self.defs.tiles_int_to_str.get(tile_id, "grass")
                
                img = self.defs.get_image(tile_str)
                if img:
                    self.screen.blit(img, (screen_x, screen_y))
                else:
                    color = COLORS.get(tile_str, COLORS["missing"])
                    pygame.draw.rect(self.screen, color, (screen_x, screen_y, TILE_SIZE, TILE_SIZE))
                
                obj_id = self.game_map.objects[idx]
                if obj_id != 0:
                    obj_str = self.defs.obj_int_to_str.get(obj_id)
                    obj_img = self.defs.get_image(obj_str)
                    
                    if obj_img:
                        offset_y = TILE_SIZE - obj_img.get_height()
                        offset_x = (TILE_SIZE - obj_img.get_width()) // 2
                        self.screen.blit(obj_img, (screen_x + offset_x, screen_y + offset_y))
                    else:
                        color = OBJ_COLORS.get(obj_id, COLORS["missing"])
                        pygame.draw.rect(self.screen, color, (screen_x + 4, screen_y + 4, TILE_SIZE - 8, TILE_SIZE - 8))
        
        for pawn in self.pawns:
            screen_x, screen_y = self.camera.world_to_screen(pawn.x, pawn.y)
            
            if -TILE_SIZE < screen_x < SCREEN_WIDTH and -TILE_SIZE < screen_y < SCREEN_HEIGHT:
                pygame.draw.circle(self.screen, COLOR_COLONIST, (int(screen_x + TILE_SIZE//2), int(screen_y + TILE_SIZE//2)), 12)
                
                hp_width = (pawn.health / pawn.def_data.base_health) * 20
                pygame.draw.rect(self.screen, COLOR_HP_RED, (screen_x + 6, screen_y - 5, 20, 4))
                pygame.draw.rect(self.screen, COLOR_HP_GREEN, (screen_x + 6, screen_y - 5, hp_width, 4))

        self.ui_manager.draw(self.screen, self.ui_font, self.small_ui_font, self.selected_pawn, self.resources)
        pygame.display.flip()

    def run(self):
        while self.running:
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(FPS)
        pygame.quit()


