import random

"""
In genetic algorithms and evolutionary computation, crossover, also called recombination,
is a genetic operator used to combine the genetic information of two parents to generate new offspring.
"""


def crossover(parent1, parent2, num_points=2):
    # Create a list of crossover points
    points = sorted(random.sample(range(1, len(parent1)), num_points))

    child1 = parent1.copy()
    child2 = parent2.copy()

    for point in points:
        child1, child2 = one_point_crossover(child1, child2, point)

    return child1, child2


def one_point_crossover(parent1, parent2, point):
    child1 = parent1[:point] + parent2[point:]
    child2 = parent2[:point] + parent1[point:]

    return child1, child2
