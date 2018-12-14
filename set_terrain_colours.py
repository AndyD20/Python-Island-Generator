from program_variables import ProgramVariables
from get_colour import get_colour


def set_terrain_colours(noise_array):

    return [[get_colour(noise_array[x][y])
             for x in range(ProgramVariables.shape[0])]
            for y in range(ProgramVariables.shape[1])]


