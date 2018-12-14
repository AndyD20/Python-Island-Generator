

def colour_array_to_display_surface(colour_array, display_surface):
    for x in range(len(colour_array)):
        for y in range(len(colour_array[0])):
            display_surface.set_at((x, y), colour_array[x][y])
