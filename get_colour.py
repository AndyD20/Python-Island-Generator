from program_variables import ProgramVariables


def get_colour(val):
    colours = ProgramVariables.Colours

    default_colour = colours.snow

    colour = default_colour

    if val < -0.05:
        colour = colours.ocean
    elif val < 0.00:
        colour = colours.beach
    elif val < 0.20:
        colour = colours.grass
    elif val < 0.35:
        colour = colours.mountain
    elif val < 1.00:
        colour = colours.snow

    return colour
