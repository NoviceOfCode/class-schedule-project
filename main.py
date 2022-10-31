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
EULER_NUMBER = math.e

capacityDictionary = {'Katz 003': 45, 'FH 216': 30, 'Royall 206': 75, 'Royall 201': 50,
                      'FH 310': 108, 'Haag 201': 60, 'Haag 301': 75, 'MNLC 325': 450, 'Bloch 119': 60}
enrollmentDictionary = {'CS101A': 50, 'CS101B': 50, 'CS191A': 50, 'CS191B': 50, 'CS201': 50,
                        'CS291': 50, 'CS303': 60, 'CS304': 25, 'CS394': 20, 'CS449': 60, 'CS451': 100}

preferredDictionary = {'CS101A': ("Gladbach", "Gharibi", "Hare", "Zein el Din"),
                       'CS101B': ("Gladbach", "Gharibi", "Hare", "Zein el Din"),
                       'CS191A': ("Gladbach", "Gharibi", "Hare", "Zein el Din"),
                       'CS191B': ("Gladbach", "Gharibi", "Hare", "Zein el Din"),
                       'CS201': ("Gladbach", "Hare", "Zein el Din", "Shah"),
                       'CS291': ("Gharibi", "Hare", "Zein el Din","Song"),
                       'CS303': ("Gladbach", "Hare", "Zein el Din"),
                       'CS304': ("Gladbach", "Hare", "Xu"),
                       'CS394': ("Xu", "Song"),
                       'CS449': ("Xu", "Song", "Shah"),
                       'CS451': ("Xu", "Song", "Shah")}
otherDictionary = {'CS101A': ("Zaman", "Nait-Abdesselam"),
                       'CS101B': ("Zaman", "Nait-Abdesselam"),
                       'CS191A': ("Zaman", "Nait-Abdesselam"),
                       'CS191B': ("Zaman", "Nait-Abdesselam"),
                       'CS201': ("Zaman", "Nait-Abdesselam", "Song"),
                       'CS291': ("Zaman", "Nait-Abdesselam", "Shah", "Xu"),
                       'CS303': ("Zaman", "Song", "Shah"),
                       'CS304': ("Zaman", "Song", "Shah", "Nait-Abdesselam", "Uddin", "Zein el Din"),
                       'CS394': ("Nait-Abdesselam", "Zein el Din"),
                       'CS449': ("Zein el Din", "Uddin"),
                       'CS451': ("Zein el Din", "Uddin", "Nait-Abdesselam", "Hare")}
#Chance of Mutation
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
    for classes in range(11):

        # Comparing double booking in other classess
        for matches in range(11):
            # Affecting fitness value by the class
            if classes != matches and solution[classes][1][2] == solution[matches][1][2] \
                    and solution[classes][1][1] == solution[matches][1][1]:
                fitnessValue -= 0.5
        threeCapBool = False
        sixCapBool = False

        if enrollmentDictionary.get(solution[classes][0]) > (3 * capacityDictionary.get(solution[classes][1][1])):
            fitnessValue -= 0.2
        else:
            threeCapBool = True
        if enrollmentDictionary.get(solution[classes][0]) > (6 * capacityDictionary.get(solution[classes][1][1])):
            fitnessValue -= 0.4
        else:
            sixCapBool = True
        if threeCapBool == True and sixCapBool == True:
            fitnessValue += 0.3
    #Preferred faculty points

        if any(x == solution[classes][1][0] for x in preferredDictionary.get(solution[classes][0])):
            fitnessValue += 0.5
        if any(x == solution[classes][1][0] for x in otherDictionary.get(solution[classes][0])):
            fitnessValue += 0.2
        else:
            fitnessValue -= 0.1

    return fitnessValue


if __name__ == '__main__':
    # Generating a population
    for s in range(10000):
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
for scheduleProgram in range(100):
    # Softmax and Probability setup
    softmaxTotal = 0
    softmaxProbHolder = []
    possibilityList = []
    rankedSolutions = []
    #Looping to link fitness to lists
    for s in range(10000):
        rankedSolutions.append([fitness(scheduleSolutions[s]), scheduleSolutions[s]])
        softmaxTotal += EULER_NUMBER ** rankedSolutions[s][0]
    for q in range(10000):
        e = ((EULER_NUMBER ** rankedSolutions[q][0]) / softmaxTotal)
        possibilityList.append(e)
    #Crossover setup
    parentsChromosomes = []
    for chromosome in range(10000):
        parentsChromosomes.append(random.choices(scheduleSolutions, weights=possibilityList, k=2))
    newGen = []
    for t in range(10000):
        newGenTupleHolder = [parentsChromosomes[t][0][0], parentsChromosomes[t][0][1], parentsChromosomes[t][0][2],
                             parentsChromosomes[t][0][3], parentsChromosomes[t][0][4], parentsChromosomes[t][1][5],
                             parentsChromosomes[t][1][6], parentsChromosomes[t][1][7], parentsChromosomes[t][1][8],
                             parentsChromosomes[t][1][9], parentsChromosomes[t][1][10]]
        newGen.append(newGenTupleHolder)

    #Mutation
    for m in range(10000):
        for g in range(11):
            mutation(newGen, m, g)

    scheduleSolutions = newGen
    winningSchedule = rankedSolutions[0]
    for looper in range(10000):
        if rankedSolutions[looper][0] > winningSchedule[0]:
            winningSchedule = rankedSolutions[looper]

    print(f'Generation{scheduleProgram}')
    print(winningSchedule)
print("Final Schedule")
print(winningSchedule)





