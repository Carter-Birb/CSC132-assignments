# Spider.py

import pygame
import constants
from Element import Element

class Spider(Element):
    """
    Enemy character that moves across the screen and resets after reaching the end.
    """

    def __init__(self):
        size = (75, 52)
        image = pygame.image.load(constants.SPIDER_IMAGE)
        image = pygame.transform.scale(image, size)
        self.position = (0, 100)
        super().__init__(image, self.position)

        self.speed = 1
        self.move_delay = 10  # Time between steps (ms)
        self.last_move_time = pygame.time.get_ticks()
        self.reappear_delay = 1000
        self.waiting_to_reappear = False
        self.reappear_timer_start = 0

    def update(self):
        """
        Handle movement logic and reappearance delay after going off screen.
        """
        current_time = pygame.time.get_ticks()

        if self.waiting_to_reappear:
            # Reappear after delay
            if current_time - self.reappear_timer_start >= self.reappear_delay:
                self.rect.right = 0
                self.waiting_to_reappear = False
        else:
            if current_time - self.last_move_time >= self.move_delay:
                self.rect.x += self.speed
                self.last_move_time = current_time

                # Check if spider left screen
                if self.rect.left > constants.WIDTH:
                    self.waiting_to_reappear = True
                    self.reappear_timer_start = current_time
