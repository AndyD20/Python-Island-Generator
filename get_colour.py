from program_variables import ProgramVariables


def get_colour(val):
    colours = ProgramVariables.Colours

    default_colour = colours.snow

    colour = default_colour

    shade_modifier = val + ProgramVariables.contrast

    threshold = 0.2

    if val < threshold + 0.05:
        colour = [shade * shade_modifier for shade in colours.blue]
    elif val < threshold + 0.055:
        colour = [shade * shade_modifier for shade in colours.sandy]
    elif val < threshold + 0.1:
        colour = [shade * shade_modifier for shade in colours.beach]
    elif val < threshold + 0.25:
        colour = [shade * shade_modifier for shade in colours.green]
    elif val < threshold + 0.6:
        colour = [shade * shade_modifier for shade in colours.darkgreen]
    elif val < threshold + 0.7:
        colour = [shade * shade_modifier for shade in colours.mountain]
    elif val < threshold + 1:
        colour = [shade * shade_modifier for shade in colours.snow]

    # Make sure that no colour value is greater than 255 (else Pygame will complain)
    colour = [col if col <= 255 else 255 for col in colour]

    return colour
