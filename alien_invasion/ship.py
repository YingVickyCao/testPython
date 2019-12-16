import pygame


class Ship:
    def __init__(self, settings, screen):
        self.settings = settings
        self.screen = screen

        self.screen_rect = screen.get_rect()

        # load ship
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        # Put ship to bottom of screen
        # self.rect.centerx = self.screen_rect.centerx
        # self.rect.bottom = self.screen_rect.bottom
        self.rect.centerx = float(self.screen_rect.centerx)
        self.rect.bottom = float(self.screen_rect.bottom)

        self.center = float(self.rect.centerx)

        # Moving tag
        self.moving_left = False
        self.moving_right = False

    # draw ship at set position
    def blit_me(self):
        self.screen.blit(self.image, self.rect)

    def update(self):
        if self.moving_left and self.rect.left > 0:
            # if self.moving_left:
            # self.rect.centerx -= 1
            self.center -= self.settings.ship_speed_factor

        # control ship scope of activity: can not out of screen
        if self.moving_right and self.rect.right < self.screen_rect.right:
            # if self.moving_right:
            # self.rect.centerx += 1
            self.center += self.settings.ship_speed_factor

        self.rect.centerx = self.center
