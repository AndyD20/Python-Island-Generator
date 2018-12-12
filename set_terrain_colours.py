from game_state import GameState
from program_variables import ProgramVariables
from get_colour import get_colour


def set_terrain_colours(display_surface, noise_array):

    for x in range(ProgramVariables.shape[0]):
        for y in range(ProgramVariables.shape[1]):
            val = noise_array[x][y]
            colour = get_colour(val)

            try:
                display_surface.set_at((x, y), colour)
            except TypeError as e:
                print(e)
                print(colour)
                ProgramVariables.game_state = GameState.STOPPING
                return
