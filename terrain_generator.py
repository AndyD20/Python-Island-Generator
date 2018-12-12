import pygame
import sys
from game_state import GameState
from program_variables import ProgramVariables
from pygame_helpers import initialise_pygame, running_loop
from generate_noise import generate_noise, circle_filter
from set_terrain_colours import set_terrain_colours


def main():

    display_surface = initialise_pygame()
    ProgramVariables.game_state = GameState.RUNNING

    noise_array = generate_noise()

    set_terrain_colours(display_surface, noise_array)

    running_loop()

    pygame.quit()
    sys.exit()


if __name__ == '__main__':
    main()
