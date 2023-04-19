import random


def fix_child(child, lower_bound, upper_bound):
    # Create a set of all unique values in the parents
    all_unique_values = set([*range(lower_bound, upper_bound+1)])

    # Create a set of unique values in particle
    particle_unique_values = set(child)

    # Find the non-existing unique values in each child
    non_existing_values_particle = list(all_unique_values - particle_unique_values)

    # Replace duplicate values in particle
    for i in range(len(child)):
        if child.count(child[i]) > 1:
            point = random.choice(non_existing_values_particle)
            non_existing_values_particle.remove(point)
            child[i] = point

    return child
