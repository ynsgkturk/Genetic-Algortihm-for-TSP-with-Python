# Genetic Algortihm for Traveling Salesman Problem

This repository contains a Python implementation of a genetic algorithm for the traveling salesman problem (TSP). The TSP is an NP-hard problem, which means that there is no efficient algorithm that can guarantee to find the optimal solution in polynomial time. However, genetic algorithms can be used to find good approximations to the optimal solution in reasonable time.
<br><br>
The genetic algorithm works by iteratively mutating and recombining a population of solutions. The fitness of each solution is evaluated based on its total distance. The solutions with the highest fitness are then selected to create the next generation of solutions. This process is repeated until a satisfactory solution is found.

* The following are the steps involved in the genetic algorithm:

1. Initialize a population of solutions.
2. Evaluate the fitness of each solution.
3. Select the solutions with the highest fitness to create the next generation.
4. Mutate and recombine the solutions in the next generation.
5. Repeat steps 2-4 until a satisfactory solution is found.

# Requirements
To run the code in this repository, you need the following:

* Python (version 3.6 or above)
* Required Python packages: numpy

# Usage
To use the genetic algorithm to solve the TSP, follow these steps:

1. Clone or download this repository to your local machine.
2. Install the required Python packages by running the following command:
3. `pip install numpy`
4. Use `case_generator` to generate scenario if there is none.
5. Change problem settings for your problem in `problem_terminate.py`file.
6. Run the `main.py`.

# Customization

The code provided in this repository offers flexibility for customization and experimentation. You can modify or extend it in several ways:

* This code uses the random selection method but you can use tournament, rulette, Fitness Distance Balance (FDB) method for selection.
* Try different mutation operators, such as swap mutation or inversion mutation.
* Test the algorithm on various TSP instances with different city distributions or sizes.

Feel free to experiment and adapt the code to suit your specific requirements.

# Resources
If you're new to the genetic algorithm or the traveling salesman problem, the following resources may be helpful:
* https://www.tutorialspoint.com/genetic_algorithms/index.htm
