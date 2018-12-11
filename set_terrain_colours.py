from program_variables import ProgramVariables
from get_colour import get_colour


def set_terrain_colours(display_surface, noise_array):

    colour_array = []

    for x in range(ProgramVariables.shape[0]):
        colour_row = []
        for y in range(ProgramVariables.shape[1]):
            val = noise_array[x][y]
            colour = get_colour(val)
            colour_row.append(colour)

            display_surface.set_at((x, y), colour)
        colour_array.append(colour_row)
    return colour_array
