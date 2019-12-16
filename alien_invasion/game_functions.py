import sys

import pygame

'''
def check_events(ship):
    # 监视键盘和鼠标事件
    for event in pygame.event.get():  # event:  pygame.event.get()
        if (event.type == pygame.QUIT):
            sys.exit()

        elif event.type == pygame.KEYDOWN:  # key down event
            if event.key == pygame.K_LEFT:  # key name
                ship.moving_left = True

            if event.key == pygame.K_RIGHT:  # key name
                # ship.rect.centerx += 1
                ship.moving_right = True

        elif event.type == pygame.KEYUP:  # key up event
            if event.key == pygame.K_LEFT:
                ship.moving_left = False

            if event.key == pygame.K_RIGHT:
                ship.moving_right = False
'''


def check_events(ship):
    # 监视键盘和鼠标事件
    for event in pygame.event.get():  # event:  pygame.event.get()
        if (event.type == pygame.QUIT):
            sys.exit()

        elif event.type == pygame.KEYDOWN:  # key down event
            check_keydown_event(event, ship)

        elif event.type == pygame.KEYUP:  # key up event
            check_keyup_events(event, ship)


def check_keyup_events(event, ship):
    if event.key == pygame.K_LEFT:
        ship.moving_left = False

    if event.key == pygame.K_RIGHT:
        ship.moving_right = False


def check_keydown_event(event, ship):
    if event.key == pygame.K_LEFT:  # key name
        ship.moving_left = True

    if event.key == pygame.K_RIGHT:  # key name
        # ship.rect.centerx += 1
        ship.moving_right = True


def update_screen(settings, screen, ship):
    # screen.fill(bg_color)   # set bg color
    screen.fill(settings.bg_color)
    ship.blit_me()

    # 让最近绘制的屏幕可见
    pygame.display.flip()
