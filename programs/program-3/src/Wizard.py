# Wizard.py

import pygame
import constants
from Element import Element
from Spell import Spell

class Wizard(Element):
    """
    The player-controlled character that can shoot spells and lose lives.
    """

    def __init__(self):
        self.size = (28, 39)
        image = pygame.image.load(constants.WIZARD_IMAGE)
        image = pygame.transform.scale(image, self.size)
        self.position = (constants.WIDTH / 2, constants.HEIGHT - self.size[1])
        super().__init__(image, self.position)

        self.lives = 3
        self.score = 0
        self.spell_cooldown = 250  # Cooldown time in milliseconds
        self.last_spell_time = pygame.time.get_ticks()
        
        # Sound effects
        self.hurt_sound = pygame.mixer.Sound(constants.LIFE_LOST_SOUND)
        self.spell_sound = pygame.mixer.Sound(constants.SPELL_SOUND)
        self.hurt_sound.set_volume(0.2)
        self.spell_sound.set_volume(0.2)

    def shoot_spell(self):
        """
        Shoot a spell if cooldown has passed.
        """
        current_time = pygame.time.get_ticks()
        if current_time - self.last_spell_time >= self.spell_cooldown:
            self.spell_sound.play()
            self.last_spell_time = current_time
            spell_position = (self.rect.centerx, self.rect.top)
            return Spell(spell_position)

    def lose_life(self):
        """
        Decrease the wizard's life count.
        """
        self.hurt_sound.play()
        self.lives -= 1

    def update(self):
        """
        Handle left/right movement based on key input.
        """
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.move("left")
        elif keys[pygame.K_d]:
            self.move("right")
