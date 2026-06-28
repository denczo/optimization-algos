# Optimization Algorithms

Three small Python programs that find the shortest route to visit a set of cities.
Each one uses a different method to solve the same problem.

| Algorithm | Script |
|-----------|--------|
| Hill Climbing | `HillClimbing.py` |
| Hill Climbing with Simulated Annealing | `HillClimbing_SimulatedAnnealing.py` |
| Genetic Algorithm | `GeneticAlgorithm.py` |

---

## Hill Climbing

In this implementation the algorithm is searching for the most efficient tour to visit a number of cities.

**Cities:** A, B, C

**Distances between Cities:**

| |A|B|C|
|-|-|-|-|
|**A**|0|3|2|
|**B**|3|0|1|
|**C**|2|1|0|

**Possible Tours:**

 **A** --[3 km]--> **B** --[1 km]--> **C** | **[4 km]**

 **A** --[2 km]--> **C** --[1 km]--> **B** | **[3 km]** (most efficient)

If you change the amount of cities (countCities = x), you have to change the threshold aswell. For 20 cities, a threshold between 15-25 is recommended. For 100 cities, a threshold between 100-175 is recommended. The higher the threshold, the more time the algorithm will need to find an optimum.

---

## Hill Climbing with Simulated Annealing

In this implementation the algorithm is searching for the most efficient tour to visit a number of cities.

**Cities:** A, B, C

**Distances between Cities:**

| |A|B|C|
|-|-|-|-|
|**A**|0|3|2|
|**B**|3|0|1|
|**C**|2|1|0|

**Possible Tours:**

 **A** --[3 km]--> **B** --[1 km]--> **C** | **[4 km]**

 **A** --[2 km]--> **C** --[1 km]--> **B** | **[3 km]** (most efficient)

**propability calculation** for simulated annealing: ![asd](http://latex.codecogs.com/png.latex?%5Cdpi%7B200%7D%20e%5E%7B%5Cfrac%7BcurrentFitness%20-%20lastFitness%7D%7Btemperature%7D%7D)

If you change the amount of cities (countCities = x), you have to change the temperature aswell. You have to experiment with the epsilon value and the value for temperature. Remember, epsilon should be small!

---

## Genetic Algorithm

Solves the same problem by keeping a group of possible routes and improving
them over many rounds — combining the good ones and making small random
changes to find shorter routes.

Key parameters (top of `GeneticAlgorithm.py`):

- `individuals` — population size
- `crossoverShare` — share of the population produced by crossover
- `mutationRate` — mutation rate
