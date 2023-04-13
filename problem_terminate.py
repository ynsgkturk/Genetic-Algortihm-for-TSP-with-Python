from generate_population import generate_population
from problem import problem
from read_scenario_from_csv import read_scenario
from calculate_distance_matrix import calculate_distance_matrix


def problem_terminate(scenario_path, scenario_number):
    """
    This function takes scenario path and returns settings about problem (dimension etc.)
    Args:
        scenario_path: Where does scenario stored
        scenario_number: Which scenario you want to work on

    Returns:
        Tuple of m, dimension, lower_bound, upper_bound and distance_matrix
    """
    # Parameter settings:

    # first read the case from csv
    subareas = read_scenario(scenario_path, scenario_number)

    dimension = len(subareas)
    lower_bound = 1
    upper_bound = dimension

    m = 50 if dimension < 50 else 80  # pop_size

    distance_matrix = calculate_distance_matrix(subareas)

    return m, dimension, lower_bound, upper_bound, distance_matrix


if __name__ == '__main__':
    pop_size, dim, lb, ub, distance_matrix = problem_terminate("case_generator/scenarios", 4)

    population = generate_population(pop_size, dim)

    print(population[3])
    # print(distance_matrix)

    fitness = problem(population[3], distance_matrix)

    print(fitness)

