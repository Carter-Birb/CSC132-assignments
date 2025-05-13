import pygame
import constants
from Wizard import Wizard
from Spell import Spell
from Spider import Spider
from random import randint

# Logic variables
wizard_lost_life = False
spider_hit_time = None  # Track the time the spider was hit
spider_respawn_delay = 2000  # Delay before spider teleports back (in milliseconds)

# Initialize Pygame
pygame.init()

# Create a screen
screen = pygame.display.set_mode((constants.WIDTH, constants.HEIGHT))

# Create sprite groups
all_sprites = pygame.sprite.Group()
spells = pygame.sprite.Group()  # Create a group for spells

# Create Wizard, Spider, and Spell instances
wizard = Wizard()  # Add to the all_sprites group
spider = Spider()  # Add to the all_sprites group

all_sprites.add(wizard, spider)

# Text Config
pygame.font.init()
font = pygame.font.SysFont("Arial", 20)

# Main game loop
running = True
while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if pygame.key.get_pressed()[pygame.K_SPACE]:
        spell = wizard.shoot_spell()
        if spell:  # Only proceed if a spell was actually created
            spells.add(spell)
            all_sprites.add(spell)
    
    # Update all sprites (including the wizard, spider, and spell)
    all_sprites.update()

    # Check if any spell collides with the spider
    for spell in spells:
        if pygame.sprite.collide_rect(spell, spider):
            spell.kill()  # Remove the spell
            # Move the spider off-screen (left)
            spider.rect.x = randint(-400, -100)  # Move it off-screen to the left
            wizard.score += 1

    # Logic for losing lives
    if spider.waiting_to_reappear:
        if not wizard_lost_life:
            wizard.lose_life()
            wizard_lost_life = True
    elif not spider.waiting_to_reappear:
        wizard_lost_life = False
    
    # Draw all sprites
    screen.fill(constants.GREY)  # Clear the screen with grey
    all_sprites.draw(screen)  # Draw all sprites to the screen
    spells.draw(screen)  # Draw all spells to the screen
    
    # Draw text (lives, etc.)
    text_score = font.render(f"Score: {wizard.score}", True, (constants.BLACK))
    screen.blit(text_score, (5, constants.HEIGHT - 45))
    text_lives = font.render(f"Lives: {wizard.lives}", True, (constants.BLACK))
    screen.blit(text_lives, (5, constants.HEIGHT - 25))

    pygame.display.flip()  # Update the display

# Quit Pygame
pygame.quit()