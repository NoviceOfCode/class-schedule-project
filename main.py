# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import random
import math

faculty = ("Gharibi", "Gladback", "Hare", "Nait-Abdesselam", "Shah", "Song", "Uddin", "Xu", "Zaman", "Zein el Din")
classesUMKC = ("CS101A", "CS101B", "CS191A", "CS191B", "CS201", "CS291", "CS303", "CS304", "CS394", "CS449", "CS451")
rooms = ("Katz 003", "FH 216", "Royall 206", "Royall 201", "FH 310", "Haag 201", "Haag 301", "MNLC 325", "Bloch 119")
classTimes = ("10 AM", "11 AM", "12 Noon", "1 PM", "2 PM", "3 PM")
scheduleSolutions = []
rankedSolutions = []
EULER_NUMBER = math.e

capacityDictionary = {'Katz 003': 45, 'FH 216': 30, 'Royall 206': 75, 'Royall 201': 50,
                      'FH 310': 108, 'Haag 201': 60, 'Haag 301': 75, 'MNLC 325': 450, 'Block 119': 60}
enrollmentDictionary = {'CS101A': 50, 'CS101B': 50, 'CS191A': 50, 'CS191B': 50, 'CS201': 50,
                        'CS291': 50, 'CS303': 60, 'CS304': 25, 'CS394': 20, 'CS449': 60}
MUTATION = 0.01

# This function is to create a tuple for each class assignment in a solution
def classroom_list(faculty, rooms, classTimes):
    listHolder = [faculty[random.randint(0, 9)], rooms[random.randint(0, 8)], classTimes[random.randint(0, 5)]]
    return listHolder
def mutation(newGen, m, g):
    if random.random() <= MUTATION:
        # Mutating faculty
        newGen[m][g][1][0] = faculty[random.randint(0, 9)]
    if random.random() <= MUTATION:
        # Mutating Room
        newGen[m][g][1][1] = rooms[random.randint(0, 8)]
    if random.random() <= MUTATION:
        # Mutating Time
        newGen[m][g][1][2] = classTimes[random.randint(0, 5)]


# Measure the fitness
def fitness(solution):
    # Iterating through each classroom tuple
    fitnessValue = 0
    # iterating through each class in a solution
    for classess in range(11):
        solution[classess][1][2]

        # Comparing double booking in other classess
        for matches in range(11):
            # Affecting fitness value by the class
            if classess != matches and solution[classess][1][2] == solution[matches][1][2] \
                    and solution[classess][1][1] == solution[matches][1][1]:
                fitnessValue -= 0.5

    for classess in range(11):
        if capacityDictionary.get([classess][0]):
            print("Dude")

    return fitnessValue


if __name__ == '__main__':
    print(len(faculty))
    print(len(classesUMKC))
    print(len(rooms))
    # Generating a population
    for s in range(1000):
        scheduleSolutions.append([
            [classesUMKC[0], classroom_list(faculty, rooms, classTimes)],
            [classesUMKC[1], classroom_list(faculty, rooms, classTimes)],
            [classesUMKC[2], classroom_list(faculty, rooms, classTimes)],
            [classesUMKC[3], classroom_list(faculty, rooms, classTimes)],
            [classesUMKC[4], classroom_list(faculty, rooms, classTimes)],
            [classesUMKC[5], classroom_list(faculty, rooms, classTimes)],
            [classesUMKC[6], classroom_list(faculty, rooms, classTimes)],
            [classesUMKC[7], classroom_list(faculty, rooms, classTimes)],
            [classesUMKC[8], classroom_list(faculty, rooms, classTimes)],
            [classesUMKC[9], classroom_list(faculty, rooms, classTimes)],
            [classesUMKC[10], classroom_list(faculty, rooms, classTimes)]
        ])
#Start of Loop

    # loop to iterate to add fitness value to each solution
    softmaxTotal = 0
    softmaxProbHolder = []
    possibilityList = []

    for s in range(1000):
        rankedSolutions.append([fitness(scheduleSolutions[s]), scheduleSolutions[s]])
        softmaxTotal += EULER_NUMBER ** rankedSolutions[s][0]
    for q in range(1000):
        e = ((EULER_NUMBER ** rankedSolutions[q][0]) / softmaxTotal)
        possibilityList.append(e)

parentsChromosomes = []
for chromosome in range(1000):
    parentsChromosomes.append(random.choices(scheduleSolutions, weights=possibilityList, k=2))
newGen = []
for t in range(1000):
    newGenTupleHolder = [parentsChromosomes[t][0][0], parentsChromosomes[t][0][1],parentsChromosomes[t][0][2],
                          parentsChromosomes[t][0][3],parentsChromosomes[t][0][4],parentsChromosomes[t][1][5],
                          parentsChromosomes[t][1][6],parentsChromosomes[t][1][7],parentsChromosomes[t][1][8],
                          parentsChromosomes[t][1][9],parentsChromosomes[t][1][10]]
    newGen.append(newGenTupleHolder)


print(newGen[999])
for m in range(1000):
    for g in range(11):
        mutation(newGen,m,g,)
    if m == 999:
        print(newGen[999])
scheduleSolutions = newGen
