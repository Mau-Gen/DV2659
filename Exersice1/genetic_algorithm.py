import random

POPUL_Size = 50

Gen_Mat = '''ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz 1234567890, .-;:_!"#%&/()=?@${[]}'''
  
TARGET = "Mauritz Almgren 2005-01-14"

class Individual:
    
    def __init__(self, chromosome): 
        self.chromosome = chromosome  
        self.fitness = self.cal_fitness() 
  
    @classmethod
    def mutated_genes(self): 
        gene = random.choice(Gen_Mat) 
        return gene 
  
    @classmethod
    def create_genome(self): 
        genome_len = len(TARGET) 
        return [self.mutated_genes() for _ in range(genome_len)] 
  
    def mate(self, par2): 
        child_chromosome = [] 
        for gp1, gp2 in zip(self.chromosome, par2.chromosome):     
  
            prob = random.random() 
  
            if prob < 0.45: 
                child_chromosome.append(gp1) 
  
            elif prob < 0.90: 
                child_chromosome.append(gp2) 
  
            else: 
                child_chromosome.append(self.mutated_genes()) 
  
        return Individual(child_chromosome) 
  
    def cal_fitness(self):
        fitness = 0
        for gs, gt in zip(self.chromosome, TARGET): 
            if gs != gt:
                fitness+= 1
        return fitness

def main():
# fill the implementation

    population = []

    for _ in range(POPUL_Size):
        genome = Individual.create_genome()
        population.append(Individual(genome))

    generation = 0

    found = False

    while not found:

        population = sorted(population, key=lambda x: x.fitness)

        print(
            "Gen: {}\tSolution: {}\tFitness Score: {}".format(
                generation, "".join(population[0].chromosome), 
                population[0].fitness
                )
            )   
        if population[0].fitness == 0:
            found = True
            break

        new_generation = []

        s = (0.1 * POPUL_Size)

        for i in range(int(s)):
            new_generation.append(population[i])

        s = (0.9 * POPUL_Size)

        for _ in range(int(s)):

            parent1 = random.choice(population[:int(0.1 * POPUL_Size)])
            parent2 = random.choice(population[:int(0.1 * POPUL_Size)])

            child = parent1.mate(parent2)

            new_generation.append(child)

        population = new_generation

        generation += 1

    population = sorted(population, key=lambda x: x.fitness)

    print("\nFinal Solution:")
    print("".join(population[0].chromosome))
    print("Fitness:", population[0].fitness)
    print("Generations:", generation)

if __name__ == "__main__":
    main()
