import pygame
import math
from player import Player
from environment import Evironment

class Game:
    def __init__(self):
        self.GRAVITY = 9.81
        self.environment = Evironment("assets/ground.png", "assets/background.png")
        self.grenade_group = pygame.sprite.Group()
        self.box_group = pygame.sprite.Group()
        self.explosion_group = pygame.sprite.Group()
        self.worm_group = pygame.sprite.Group()
        self.player1 = Player(self, 500, 330, (255, 0, 0))
        self.player2 = Player(self, 780, 330, (0, 0, 255))
        self.end_turn = False
        self.turn = 0

    def aiming(self, screen, worm):
        WHITE = (255, 255, 255)
        worm_to_cursor = (pygame.mouse.get_pos()[0] - worm.rect.centerx, pygame.mouse.get_pos()[1]-30 - worm.rect.centery)
        x_0 = worm.rect.centerx
        y_0 = worm.rect.centery

        #print(vector[0]);
        factor = 100
        direction_x = 1
        direction_y = 1
        if worm_to_cursor[0] < 0:
            direction_x = -1
        if worm_to_cursor[1] < 0:
            direction_y = -1

        #linear
        #v = (worm_to_cursor[0]/2, worm_to_cursor[1]/2)
        # square root
        #v = (factor * direction_x * math.sqrt(abs(worm_to_cursor[0])), factor * direction_y * math.sqrt(abs(worm_to_cursor[1])))
        # ease out sine
        if abs(worm_to_cursor[0]/300) > 1:
            worm_to_cursor = (direction_x * 300, worm_to_cursor[1])
        if abs(worm_to_cursor[1]/300) > 1:
            worm_to_cursor = (worm_to_cursor[0], direction_y * 300)
        v = (factor * direction_x * math.sin((abs(worm_to_cursor[0]/300) * math.pi) / 2), 100 * direction_y * math.sin((abs(worm_to_cursor[1]/300) * math.pi) / 2))
        v_norme = math.sqrt(v[0] ** 2 + v[1] ** 2)

        size = 8
        t = .5
        while t <= 5:
            x = v[0] * t + x_0
            y = -0.5 * -self.GRAVITY * t ** 2 + v[1] * t + y_0
            point = pygame.Rect(x, y, size, size)
            pygame.draw.ellipse(screen, WHITE, point, 0)
            t += .5
            size -= .2

        #pygame.draw.line(screen, WHITE, (worm.rect.centerx, worm.rect.centery), (pygame.mouse.get_pos()))