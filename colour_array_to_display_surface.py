

def colour_array_to_display_surface(colour_array, display_surface):
    for x in range(len(colour_array)):
        for y in range(len(colour_array[0])):
            display_surface.set_at((x, y), colour_array[x][y])


def noise_array_to_display_surface(noise_array, display_surface):
    for x in range(len(noise_array)):
        for y in range(len(noise_array[0])):
            val = noise_array[x][y] * 255
            val = val if val < 255 else 255
            display_surface.set_at((x, y), (val, val, val))
