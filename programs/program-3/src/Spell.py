# Spell.py

import pygame
from Element import Element

class Spell(Element):
    """
    Spell object shot by the wizard. Moves upward and disappears off screen.
    """

    def __init__(self, position: tuple[int, int]):
        size = (2, 10)
        image = pygame.Surface(size)
        image.fill((0, 0, 255))  # Red spell
        super().__init__(image, position)

        self.speed = 2  # Pixels per frame

    def update(self):
        """
        Move the spell upward and remove it if it goes off screen.
        """
        self.rect.y -= self.speed

        # Kill spell if it moves off-screen
        if self.rect.bottom < 0:
            self.kill()
