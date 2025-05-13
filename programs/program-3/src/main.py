import pygame
import constants
from Wizard import Wizard
from Spell import Spell
from Spider import Spider
from random import randint


#### INITIALIZATION ####
pygame.init()
pygame.font.init()
screen = pygame.display.set_mode((constants.WIDTH, constants.HEIGHT))

# Fonts
font = pygame.font.SysFont("Arial", 20)
title_font = pygame.font.SysFont("Arial", 40)
small_font = pygame.font.SysFont("Arial", 24)

# Sound effects
spider_sound = pygame.mixer.Sound(constants.SPIDER_SOUND)
spider_sound.set_volume(0.8)


#### START SCREEN FUNCTION ####
def show_start_screen():
    screen.fill(constants.GREY)
    
    title_text = title_font.render("Wizard Spider Blaster!", True, constants.BLACK)
    prompt_text = small_font.render("Press any key to start", True, constants.BLACK)
    
    screen.blit(title_text, (constants.WIDTH // 2 - title_text.get_width() // 2, constants.HEIGHT // 2 - 100))
    screen.blit(prompt_text, (constants.WIDTH // 2 - prompt_text.get_width() // 2, constants.HEIGHT // 2))
    pygame.display.flip()
    
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                waiting = False


#### DEATH SCREEN FUNCTION ####
def show_death_screen():
    screen.fill(constants.GREY)
    
    death_text = title_font.render("YOU DIED!", True, constants.BLACK)
    prompt_text = small_font.render("Press any key to restart", True, constants.BLACK)
    
    screen.blit(death_text, (constants.WIDTH // 2 - death_text.get_width() // 2, constants.HEIGHT // 2 - 100))
    screen.blit(prompt_text, (constants.WIDTH // 2 - prompt_text.get_width() // 2, constants.HEIGHT // 2))
    pygame.display.flip()
    
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                waiting = False


#### STARTING THE GAME ####
show_start_screen()

# Sprite groups
all_sprites = pygame.sprite.Group()
spells = pygame.sprite.Group()

# Create game objects
wizard = Wizard()
spider = Spider()
all_sprites.add(wizard, spider)

# Game state
running = True
wizard_lost_life = False


#### MAIN LOOP ####
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Shoot spell
    if pygame.key.get_pressed()[pygame.K_SPACE]:
        spell = wizard.shoot_spell()
        if spell:
            spells.add(spell)
            all_sprites.add(spell)

    # Update logic: prevent wizard from going offscreen
    if (wizard.rect.left <= 0 and pygame.key.get_pressed()[pygame.K_a]) or (wizard.rect.right >= constants.WIDTH and pygame.key.get_pressed()[pygame.K_d]):
        # Update all except wizard
        for sprite in all_sprites:
            if sprite != wizard:
                sprite.update()
    else:
        all_sprites.update()

    # Collision: spell hits spider
    for spell in spells:
        if pygame.sprite.collide_rect(spell, spider):
            spider_sound.play()
            spell.kill()
            spider.rect.x = randint(-400, -100)
            spider.move_delay = randint(1, 10)
            wizard.score += 1

    # Life loss when spider escapes
    if spider.waiting_to_reappear:
        if not wizard_lost_life:
            wizard.lose_life()
            wizard_lost_life = True
            spider.move_delay = randint(1, 10)
    else:
        wizard_lost_life = False
    
    # Logic for Wizard losing all lives
    if wizard.lives == 0:
        wizard.lives = 3
        wizard.score = 0
        wizard.rect.x = constants.WIDTH // 2
        show_death_screen()

    # Draw everything
    screen.fill(constants.GREY)
    all_sprites.draw(screen)
    spells.draw(screen)

    # HUD
    score_text = font.render(f"Score: {wizard.score}", True, constants.BLACK)
    lives_text = font.render(f"Lives: {wizard.lives}", True, constants.BLACK)
    screen.blit(score_text, (5, constants.HEIGHT - 45))
    screen.blit(lives_text, (5, constants.HEIGHT - 25))

    pygame.display.flip()

pygame.quit()