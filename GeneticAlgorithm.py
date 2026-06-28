import random

individuals = 20 #p
crossoverShare = 0.5 #r
mutationRate = 10 #m
population = [] #P
newGeneration = [] #Ps
fitnesses = [int]*individuals

maxFitness = 0
fitnessThreshold = -6
optimum = 170 #binary 10101010
optimumRandom = random.randint(100,256);

#TODO Code optimization, check logic of selection methode again!

#generates random numbers, converts them into binary strings
#and calculates their fitness
def randomGenes(individuals,optimumRandom):
    genes = [""]*individuals
    for i in range(individuals):
        number = random.randint(0, 256)
        genes[i] = "{0:08b}".format(number)
        fitnesses[i] = calculateFitness(number,optimumRandom)
    return genes

#just like in the pseudocode
def selectIndividual(fitnesses, entireFitness, individuals):
    randNum = random.uniform(0,1)
    sum = 0
    index = random.randint(0,individuals-1)
    while sum < randNum:
        index += 1
        index = index % individuals
        sum += checkFitness(fitnesses,index,entireFitness)
    return index

#fitness function -(value-optimum)^2
def calculateFitness(value, optimumRandom):
    return -1*((value-optimumRandom)**2)

#selects individuals and adds them to a new generation
def selection():
    for i in range(int((1-crossoverShare)*individuals)):
        descendant = int(population[selectIndividual(fitnesses,maxFitness,individuals)],2)
        # to prevent double entries
        while descendant in newGeneration:
            descendant = selectIndividual(fitnesses,maxFitness,individuals)
        newGeneration.append(descendant)

#checks fitness compared to all other binary strings
def checkFitness(fitnesses, individual, entireFitness):
    return fitnesses[individual]/float(entireFitness)

#adds all fitneses up
def getEntireFitness(population, fitnesses):
    sum = 0
    individuals = len(population)-1
    for i in range(individuals-1):
        sum += fitnesses[i]
    return sum

#generates a random positon for cut, performs a single point crossover
#and adds the modified genes to the new generation
def crossover():
    binrayLength = 8
    for i in range(int(crossoverShare*individuals/2)):
        #length of binary number = 8
        randomCut = random.randint(0,binrayLength-1)
        parentA = population[selectIndividual(fitnesses,maxFitness,individuals)]
        parentB = population[selectIndividual(fitnesses,maxFitness,individuals)]
        #print("PARENT A ",parentA)
        #print("PARENT B ",parentB)
        descendantA = parentA[0:randomCut] + parentB[randomCut:binrayLength]
        descendantB = parentB[0:randomCut] + parentA[randomCut:binrayLength]
        #print("DESCENDANT A ",descendantA)
        #print("DESCENDANT B ",descendantB)
        #print("")
        newGeneration.append(int(descendantA,2))
        newGeneration.append(int(descendantB,2))

#flips random bits of the binary strings in the new generation
def mutation():
    global individuals;
    global maxFitness;
    global fitnesses;
    for i in range(mutationRate):

        candidate = "{0:08b}".format(newGeneration[selectIndividual(fitnesses, maxFitness, individuals)])
        #print("CANDIDATE ",candidate)
        randomBit = random.randint(0,7)
        #print("RANDOMBIT ",randomBit)
        candidate = candidate[0:randomBit] + flipBit(candidate[randomBit]) + candidate[randomBit+1:8]
        #print("BIT FLIP ", candidate)
        #print("")
        newGeneration.remove(newGeneration[i])
        newGeneration.insert(i,int(candidate,2))

def flipBit(binary):
    if binary == "0":
        return "1"
    if binary == "1":
        return "0"

#replaces elements with worst fitness
def updatePopulation():
    for i in range(len(newGeneration)):
        worst = fitnesses.index(min(fitnesses))
        population.remove(population[worst])
        population.append("{0:08b}".format(newGeneration[i]))
        fitnesses.remove(min(fitnesses))
        fitnesses.append(calculateFitness(newGeneration[i],optimumRandom))
    newGeneration.clear()


if __name__ == '__main__':
    population = randomGenes(individuals,optimumRandom)
    tries = 0
    oldFitness = 0
    maxFitness = getEntireFitness(population, fitnesses)
    print("START FITNESS:", maxFitness,"OPTIMUM:","{0:08b}".format(optimumRandom))
    print("START POPULATION:",population)
    print()

    while maxFitness < fitnessThreshold and tries < 100:
        selection()
        crossover()
        mutation()
        updatePopulation()
        maxFitness = getEntireFitness(population,fitnesses)
        print("CURRENT FITNESS:",maxFitness," ",population)
        if(oldFitness < maxFitness):
            tries = 0
            oldFitness = maxFitness
        else:
            tries+=1

    print()
    print("CURRENT FITNESS:",maxFitness)
    print("CURRENT POPULATION:",population)
