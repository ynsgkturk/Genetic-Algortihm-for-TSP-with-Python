import random

from crossover import crossover
from mutation import two_opt_mutation
from elitism import elitism
from problem_terminate import problem_terminate
from problem import problem
from generate_population import generate_population
from fix_child import fix_child


def genetic_algorithm(scenario_path, scenario_num, cp=0.85, Er=0.2):
    """
    Run a genetic algorithm to find a solution to our customized TSP problem.

    Parameters:
    scenario_path (str): The path where the scenario stored.
    scenario_number (int): The number of the scenario to read.
    cp (float): probability of crossover, default is 0.85
    Er (float): elitism rate, default is 0.2

    Returns:
    best population (dict): a dict contains the best population and fitness
    """

    # problem initialization
    m, dimension, lb, ub, distance_matrix, maxFE = problem_terminate(scenario_path,
                                                                     scenario_num)

    # ecosystem initialization
    ecosystem = []
    population = generate_population(m, dimension)

    # calculate fitness values
    for pop in population:
        ecosystem.append({
            "population": pop,
            "fitness": problem(pop, distance_matrix),
        })

    best_chromosome = sorted(ecosystem, key=lambda x: x["fitness"], reverse=False)[0]

    # Main Loop
    for _ in range(maxFE):

        new_ecosystem = []

        for i in range(0, len(ecosystem), 2):
            # Selection
            parent1, parent2 = random.sample(ecosystem, 2)

            # Crossover
            child1, child2 = crossover(parent1["population"], parent2["population"], num_points=2)

            # handle constraint
            child1 = fix_child(child1, lb, ub)
            child2 = fix_child(child2, lb, ub)

            # Mutation
            child1 = two_opt_mutation(child1)
            child2 = two_opt_mutation(child2)

            # calculate fitness values and add children to the new population
            new_ecosystem.append({
                "population": child1,
                "fitness": problem(child1, distance_matrix),
            })

            new_ecosystem.append({
                "population": child2,
                "fitness": problem(child2, distance_matrix),
            })

        # Elitism and update ecosystem
        ecosystem = elitism(ecosystem, new_ecosystem, Er)

        # Update the best chromosome
        best_candidate = sorted(ecosystem, key=lambda x: x["fitness"], reverse=False)[0]

        if best_candidate["fitness"] < best_chromosome["fitness"]:
            best_chromosome = best_candidate

    return best_chromosome
