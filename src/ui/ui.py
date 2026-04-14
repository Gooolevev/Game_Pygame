import pygame
import pygame_gui
from pygame_gui.elements import UIPanel, UILabel, UIStatusBar
import os
import sys
from config.settings import *


class UIManager:
    def __init__(self, screen_w, screen_h):
        self.panel_h = 128
        self.margin = 4

        self.screen_w = screen_w
        self.screen_h = screen_h


    def draw(self, screen, font, small_font, select_pawn, resources = None):
        if resources is None: resources = {"wood": 0, "stone": 0, "food": 0}

        panel_rect = pygame.Rect(
            self.margin,
            self.screen_w - self.panel_h - self.margin,
            self.screen_h - self.margin * 2,
            self.panel_h,
        )

        pygame.draw.rect(screen, BG, panel_rect)
        res_text = f"WOOD: {resources['wood']}, STONE: {resources['stone']}, FOOD: {resources['food']}"
        screen.blit(font.render(res_text, True, TEXT), (10, panel_rect.y + 8))

        if select_pawn:
            pawn = select_pawn
            base_y = panel_rect.y

            screen.blit(font.render(f"{pawn.def_data.name}", True, NAME))

            stats = [("Hunger", pawn.hunger / 100.0),("Energy", pawn.energy / 100.0)]

            for i, (n, val) in enumerate(stats):
                val = max(0.0, min(1.0, val))
                x = 10 + i * 160
                y = panel_rect.y + 64
                bar_w, bar_h = 140, 12

                pygame.draw.rect(screen, BAR_BG, (x, y, bar_w, bar_h))

                if val > 0.4: clr = BAR_OK
                elif val > 0.2: clr = BAR_WARN
                else: clr = self.BAR_LOW

                pygame.draw.rect(screen, clr, (x, y, int(bar_w * val), bar_h))
                screen.blit(small_font.render(n, True, STATUS), (x, y + 14))

        
            job_text = "It's coming..." if pawn.path else "It's idle"
            screen.blit(small_font.render(job_text, True, STATUS), (10, base_y + 96))
            

        screen.blit(font.render("ПКМ — движение", True, NAME), (self.screen_w - 260, base_y  + 4))
        screen.blit(small_font.render("WASD — камера | ПКМ — идти | ЛКМ — выбрать", True, STATUS), 
                    (self.screen_w - 420, panel_rect.y + 36))