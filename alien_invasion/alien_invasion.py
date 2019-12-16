import sys

import pygame

from settings import Settings
from ship import Ship
import game_functions as gf


def run_game():
    pygame.init()
    settings = Settings()
    # screen = pygame.display.set_mode((1200, 800)) # set window size. screen is a surface showing game elements.
    screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))  # set window size. screen is a surface showing game elements.
    pygame.display.set_caption("Alien Invasion")  # set window name
    # bg_color = (230,230,230) # RGB

    ship = Ship(settings, screen)

    # start game
    while True:
        # for event in pygame.event.get():
        #     if (event.type == pygame.QUIT):
        #         sys.exit()
        gf.check_events(ship)
        ship.update()

        # screen.fill(bg_color)   # set bg color
        # screen.fill(settings.bg_color)
        # ship.blit_me()

        # 让最近绘制的屏幕可见
        # pygame.display.flip()
        # 它用于在每次执行主循环时都重绘屏幕。
        gf.update_screen(settings, screen, ship)
    return


run_game()
