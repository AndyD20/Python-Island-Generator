import noise
from program_variables import ProgramVariables
from random import randint

octaves = 6
persistence = 0.5
lacunarity = 2.0


def generate_noise():
    base = randint if ProgramVariables.random else 0

    noise_array = []

    for x in range(ProgramVariables.shape[0]):
        noise_row = []
        for y in range(ProgramVariables.shape[1]):

            val = (noise.pnoise2(x / ProgramVariables.scale,
                                 y / ProgramVariables.scale,
                                 octaves=octaves,
                                 persistence=persistence,
                                 lacunarity=lacunarity,
                                 repeatx=1024,
                                 repeaty=1024,
                                 base=base))

            noise_row.append(val)
        noise_array.append(noise_row)
    return noise_array
