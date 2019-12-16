# 子弹
import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    def __int__(self, settings, screen, ship):
        super().__init__()
        self.screen = screen
        # Bullet is based on Rect,drawed by pygame
        self.rect = pygame.Rect(0, 0, settings.bullet_width, settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        self.y = float(self.rect.y)

        self.color = settings.bullet_color
        self.speed_factor = settings.bullet_speed_factor
