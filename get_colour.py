from program_variables import ProgramVariables


def get_colour(val):
    colours = ProgramVariables.Colours

    default_colour = colours.snow

    colour = default_colour

    shade_modifier = val + ProgramVariables.contrast

    threshold = 0.1

    if val < threshold + 0.05:
        colour = [shade * shade_modifier for shade in colours.ocean]
    elif val < threshold + 0.055:
        colour = [shade * shade_modifier for shade in colours.dark_sand]
    elif val < threshold + 0.10:
        colour = [shade * shade_modifier for shade in colours.beach]
    elif val < threshold + 0.25:
        colour = [shade * shade_modifier for shade in colours.grass]
    elif val < threshold + 0.60:
        colour = [shade * shade_modifier for shade in colours.jungle]
    elif val < threshold + 0.80:
        colour = [shade * shade_modifier for shade in colours.mountain]
    elif val < threshold + 1:
        colour = [shade * shade_modifier for shade in colours.snow]

    # Make sure that no colour value is greater than 255 (else Pygame will complain)
    colour = [col if col <= 255 else 255 for col in colour]

    return colour
