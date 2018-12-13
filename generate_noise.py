import noise
from program_variables import ProgramVariables
from random import randint
import math

octaves = 6
persistence = 0.5
lacunarity = 2.0
base = randint(1, 100) if ProgramVariables.random else 0


def generate_noise():
    circle = circle_filter()

    filtered_noise = [[(gen_noise(x, y) * circle[x][y]) * 20
                      if (gen_noise(x, y) * circle[x][y]) > 0
                      else (gen_noise(x, y) * circle[x][y])
                      for x in range(ProgramVariables.shape[0])] for y in range(ProgramVariables.shape[1])]

    max_grad = max([max(elem) for elem in filtered_noise])

    return [[abs(elem) / max_grad for elem in row] for row in filtered_noise]


def circle_filter():
    centre_point = (ProgramVariables.shape[0] / 2, ProgramVariables.shape[1] / 2)

    circle_array = [[calc_distance(centre_point, x, y)
                     for x in range(ProgramVariables.shape[0])] for y in range(ProgramVariables.shape[1])]

    max_grad = max([max(elem) for elem in circle_array])

    circle_array = [[-(((elem / max_grad) - 0.5) * 2) for elem in row] for row in circle_array]

    circle_array = [[elem * 20 if elem > 0 else elem for elem in row] for row in circle_array]

    max_grad = max([max(elem) for elem in circle_array])
    circle_array = [[elem / max_grad for elem in row] for row in circle_array]

    return circle_array


def gen_noise(x, y):
    return noise.pnoise2(x / ProgramVariables.scale,
                         y / ProgramVariables.scale,
                         octaves=octaves,
                         persistence=persistence,
                         lacunarity=lacunarity,
                         repeatx=1024,
                         repeaty=1024,
                         base=base)


def calc_distance(centre_point, x, y):
    return math.sqrt(math.pow(abs(x - centre_point[0]), 2) + math.pow(abs(y - centre_point[1]), 2))
