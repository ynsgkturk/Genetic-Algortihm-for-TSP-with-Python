import random

"""
The two-opt mutation operator is a simple yet effective mutation operator for TSP.
It randomly selects two positions in the chromosome and reverses the order of the
cities between those positions.
"""


def two_opt_mutation(chromosome):
    """
    Perform a two-opt (also called inversion) mutation on the given chromosome.

    Parameters:
    chromosome (list): a list of integers representing the order of cities in the TSP route.

    Returns:
    list: the mutated chromosome
    """
    # Select two random positions in the chromosome
    pos1 = random.randint(0, len(chromosome)-1)
    pos2 = random.randint(0, len(chromosome)-1)
    while pos1 == pos2:
        pos2 = random.randint(0, len(chromosome)-1)
    # Reverse the order of the cities between the two positions
    if pos1 > pos2:
        pos1, pos2 = pos2, pos1

    chromosome[pos1:pos2] = list(reversed(chromosome[pos1:pos2]))
    return chromosome
