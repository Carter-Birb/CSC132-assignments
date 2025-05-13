# Element.py

import pygame

class Element(pygame.sprite.Sprite):
    """
    Base class for all game entities with movement and alive status.
    """

    def __init__(self, image: pygame.Surface, position: tuple[int, int]):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect(topleft=position)
        self.alive = True

    def move(self, direction: str):
        """
        Move the sprite in the specified direction.
        """
        match direction:
            case "up": self.rect.y -= 1
            case "down": self.rect.y += 1
            case "left": self.rect.x -= 1
            case "right": self.rect.x += 1
            case _: print(f"Unknown direction: {direction}")

    def kill(self):
        """
        Mark sprite as not alive and remove from groups.
        """
        self.alive = False
        super().kill()