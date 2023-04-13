import random


def generate_population(m, n):
    # Create an empty population matrix with the specified number of areas
    population = set()

    # Fill the population matrix with random permutations of the numbers from 1 to n
    while len(population) < m:
        population.add(tuple(random.sample(range(1, n + 1), n)))

    return list(population)
