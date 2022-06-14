from operator import truediv
import sys
import json
import time
import string
import random
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np


minList = lambda list: min([len(i) for i in list])


def LCP_BFA(lst):
    result = ""
    for i in range(minList(lst)):
        temp = lst[0][i]
        for j in range(1, len(lst)):
            if (lst[j][i] != temp):
                return result
        result = result + temp
    return (result)


def LCP(lst1, lst2):
    result = ""
    n1, n2 = len(lst1), len(lst2)
    i, j = 0, 0
    while i < n1 and j < n2:
        if lst1[i] != lst2[j]:
            break
        result += lst1[i]
        i, j = i + 1, j + 1
    return result


def LCP_DNC(lst, low, high):
    if low == high:
        return lst[low]
    if high > low:
        # Same as (low + high)/2, but avoids
        # overflow for large low and high
        # Reference: GeeksForGeeks
        mid = low + (high - low) // 2
        return LCP(LCP_DNC(lst, low, mid), LCP_DNC(lst, mid + 1, high))
    return ""


def readFromTestCase():
    src = "TestCases_LCP.txt" if len(sys.argv) == 1 else sys.argv[1]
    with open(src, 'r') as tc:
        lines = tc.readlines()
        for index, line in enumerate(lines, start=1):
             if line != "\n":
                line = line.rstrip('\n')
                line = f'[ { line } ]'
                obj = json.loads(line)
                testCase, expectedResult = obj[0], obj[1]
                print(f'{index}.Test case: {obj[0]}')
                print(f'Expected Result: {obj[1]} | Expected Result Length: {len(obj[1])} ')
                testResultBFA = LCP_BFA(testCase*50)
                print(f'Brute force approach result: {testResultBFA} | Brute force approach result length: {len(testResultBFA)}')
                testResultDNC = LCP_DNC(testCase, 0, len(testCase) - 1)
                print(f'Divide and conquer result: {testResultBFA} | Divide and conquer result length: {len(testResultBFA)}')
                print(100 * "-")


def randomWordGenerator(wordLength, prefix = ""):
    for i in range(wordLength):
        prefix += random.choice(string.ascii_lowercase[0:wordLength])
    return prefix


def randomWordListGenerator(listLength):
    result = []
    prefix = string.ascii_lowercase[random.randint(2, 3) : random.randint(4, 9)]
    for i in range(listLength):
        result.append(randomWordGenerator(random.randint(3, 9), prefix))
    return result


def plotAnalysis(isBfa=True):
    lstTimes = []
    for i in range(10, 101, 10):
        avg = 0
        for j in range(1, i + 1):
            tempList = randomWordListGenerator(i * j)
            if isBfa:
                t0 = time.time()
                LCP_BFA(tempList)
                t1 = time.time()
                avg += (t1 - t0)
            else:
                t0 = time.time()
                LCP_DNC(tempList, 0, len(tempList) - 1)
                t1 = time.time()
                avg += (t1 - t0)
        lstTimes.append((avg / 10))
    plt.plot(list(range(10, 101, 10)), lstTimes)
    plt.xlabel('Array smallest length')
    plt.ylabel('Time')
    plt.title(f'LCB - { "Brute force approach" if isBfa else "Divide and conquer"}')
    plt.show()


def twoPlotAnalysis():
    lstTimes0, lstTimes1 = [], []
    for i in range(10, 101, 10):
        avg0, avg1 = 0, 0
        for j in range(1, i + 1):
            tempList = randomWordListGenerator(i * j)
            t0 = time.time()
            LCP_BFA(tempList)
            t1 = time.time()
            avg0 += (t1 - t0)
            t0 = time.time()
            LCP_DNC(tempList, 0, len(tempList) - 1)
            t1 = time.time()
            avg1 += (t1 - t0)
        lstTimes0.append((avg0 / 10))
        lstTimes1.append((avg1 / 10))
    plt.plot(list(range(10, 101, 10)), lstTimes0, label = "BFA")
    plt.plot(list(range(10, 101, 10)), lstTimes1, label = "DNC")
    plt.legend()
    plt.xlabel('Array smallest length')
    plt.ylabel('Time')
    plt.title('LCB')
    plt.show()


if __name__ == "__main__":
    #readFromTestCase()
    #Experimental Analysis
    #Brute force approach
    #plotAnalysis()
    #Divide and conquer
    #plotAnalysis(False)
    twoPlotAnalysis()
