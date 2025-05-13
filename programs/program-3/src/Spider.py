import pygame
import constants
from Element import Element
from Wizard import Wizard

class Spider(Element):

    def __init__(self):
        size = 75, 52
        image = pygame.image.load('../assets/images/spider.png')
        image = pygame.transform.scale(image, size)
        position = (0, 100)
        super().__init__(image, position)

        self.speed = 1
        self.move_delay = 10  # milliseconds between steps
        self.last_move_time = pygame.time.get_ticks()
        self.reappear_delay = 1000  # wait 1 second before reappearing
        self.waiting_to_reappear = False
        self.reappear_timer_start = 0

    def update(self):
        current_time = pygame.time.get_ticks()

        # Logic for Spider hitting the right side of the screen
        if self.waiting_to_reappear:
            if current_time - self.reappear_timer_start >= self.reappear_delay:
                self.rect.right = 0  # Reappear on the left
                self.waiting_to_reappear = False
        else:
            if current_time - self.last_move_time >= self.move_delay:
                self.rect.x += self.speed
                self.last_move_time = current_time

                if self.rect.left > constants.WIDTH:
                    self.waiting_to_reappear = True
                    self.reappear_timer_start = current_time
