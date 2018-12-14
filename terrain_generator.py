import pygame
import sys

from colour_array_to_display_surface import colour_array_to_display_surface, noise_array_to_display_surface
from game_state import GameState
from program_variables import ProgramVariables
from pygame_helpers import initialise_pygame, running_loop
from generate_noise import generate_noise
from set_terrain_colours import set_terrain_colours
from timer import timer


def main():

    display_surface = timer('Initialisation', initialise_pygame)

    ProgramVariables.game_state = GameState.RUNNING

    noise_array = timer('Generating Noise', generate_noise)

    colour_array = timer('Settings Colours', set_terrain_colours, [noise_array])

    if not ProgramVariables.view_raw_noise:
        timer('Painting colours to display surface', colour_array_to_display_surface, [colour_array, display_surface])
    else:
        timer('Painting colours to display surface', noise_array_to_display_surface, [noise_array, display_surface])

    running_loop()

    pygame.quit()
    sys.exit()


if __name__ == '__main__':
    main()
