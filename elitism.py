
def elitism(population, new_population, Er):
    elite_population = []
    num_elite = round(len(population) * Er)

    population = sorted(population, key=lambda x: x["fitness"], reverse=False)
    new_population = sorted(new_population, key=lambda x: x["fitness"], reverse=True)

    # The elites from the previous population
    for k in range(num_elite):
        elite_population.append(population[k])

    # The rest from the new population
    for k in range(num_elite, len(new_population)):
        elite_population.append(new_population[k])

    # finally return elite population
    return elite_population
