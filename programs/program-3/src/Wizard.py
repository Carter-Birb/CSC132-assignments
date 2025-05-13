import pygame
import constants
from Element import Element
from Spell import Spell

class Wizard(Element):
    
    def __init__(self):
        size = 28, 39
        image = pygame.image.load('../assets/images/wizard.png')
        image = pygame.transform.scale(image, size)
        position = (constants.WIDTH / 2, constants.HEIGHT - size[1])
        super().__init__(image, position)

        self.lives = 3
        self.score = 0
        self.spell_cooldown = 1000 # Milliseconds
        self.last_spell_time = pygame.time.get_ticks()

    def shoot_spell(self):
        current_time = pygame.time.get_ticks()
        if current_time - self.last_spell_time >= self.spell_cooldown:
            spell_position = (self.rect.centerx, self.rect.top)
            self.last_spell_time = current_time
            return Spell(spell_position)
    
    def lose_life(self):
        self.lives -= 1
    
    def update(self):
        # Example movement logic
        if pygame.key.get_pressed()[pygame.K_a]:
            self.move("left")
        elif pygame.key.get_pressed()[pygame.K_d]:
            self.move("right")
