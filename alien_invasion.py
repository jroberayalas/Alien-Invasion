import pygame
from pygame.sprite import Group

from settings import Settings
from ship import Ship
import game_functions as gf

def run_game():
    # Initialize pygame, settings, and create a screen object.
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
            (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    
    # Make a ship, a group of bullets, and a group of alients.
    ship = Ship(ai_settings, screen)
    bullets = Group()
    aliens = Group()

    # Create the fleet of aliens.
    gf.create_fleet(ai_settings, screen, ship, aliens)

    # Start the main loop for the game
    while True:
        # Check events.
        gf.check_events(ai_settings, screen, ship, bullets)
        # Update ship.
        ship.update()
        # Update bullets.
        gf.update_bullets(bullets)
        # Update screen.
        gf.update_screen(ai_settings, screen, ship, aliens, bullets)

run_game()