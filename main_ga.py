from GA import genetic_algorithm


def main():
    scenario_path = "case_generator/scenarios"
    scenario_num = 4

    best_chromosome = genetic_algorithm(scenario_path, scenario_num)

    print("Best Chromosome: ", best_chromosome["population"])
    print("Best Fitness: ", best_chromosome["fitness"])


if __name__ == '__main__':
    main()
