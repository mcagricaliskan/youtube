import time
import random


class Genetic:
    def __init__(self, Target, Population_Number):
        self.Gene_Pool = '''abcçdefgğhıijklmnoöpqrsştuüvwxyzABCÇDEFGĞHİIJKLMNOÖPQRŞSTUÜVWXYZ 1234567890,.-;:_!"#%&/()=?@${[]}'''
        self.Target = Target
        self.Population_Number = Population_Number
        self.Target_Text_Lenght = len(Target)
        self.Population = []
        self.Next_Generation = []
        self.Found = False
        self.Generation_Timer = 0

    class Member:
        def __init__(self,chromosome):
            self.Chromosome = chromosome
            self.Fitness = 0

    def random_gene(self):
        Gene = random.choice(self.Gene_Pool)
        return Gene

    def create_chromosome(self):
        chromosome = [self.random_gene() for i in range(self.Target_Text_Lenght)]
        return chromosome

    def calculate_fitness(self):
        for Member in self.Population:
            Member.Fitness = 0
            for i in range(self.Target_Text_Lenght):
                if Member.Chromosome[i] == self.Target[i]:
                    Member.Fitness += 1

            if Member.Fitness == self.Target_Text_Lenght:
                self.Found_Text = Member.Chromosome
                self.Found = True

    def crossover(self):
        last_best = int(( 90 * self.Population_Number) / 100)

        self.Next_Generation = []
        self.Next_Generation.extend(self.Population[last_best:])

        while True:
            if len(self.Next_Generation) < self.Population_Number:
                member_1 = random.choice(self.Population[last_best:]).Chromosome
                member_2 = random.choice(self.Population[last_best:]).Chromosome
                new_member = []

                for gene1,gene2 in zip(member_1, member_2):
                    prob = random.random() # 0 - 1
                    if prob < 0.47:
                        new_member.append(gene1)
                    elif prob < 0.94:
                        new_member.append(gene2)
                    else:
                        new_member.append(self.random_gene())

                self.Next_Generation.append(self.Member(new_member))


            else:
                break

        self.Population = self.Next_Generation



    def main(self):
        for i in range(self.Population_Number):
            self.Population.append(self.Member(self.create_chromosome()))


        while not self.Found:
            self.calculate_fitness()
            self.Population = sorted(self.Population, key=lambda Member: Member.Fitness)
            self.crossover()
            self.Generation_Timer += 1

        print(f"You found = {self.Found_Text}, you did it {self.Generation_Timer} steps."
              f"\n Your Target = {self.Target}")

Target = "Mustafa Kemal Atatürk"
Population_Number = 1000

Go = Genetic(Target, Population_Number)
Go.main()
