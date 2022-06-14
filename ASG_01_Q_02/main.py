import sys
import json


def LCS(s1, s2, result = "", i = None, j = None):
    if i == None or j == None:
        i, j = len(s1) - 1, len(s2) - 1
    if i == -1 or j == -1:
        return 0, ""
    if s1[i] == s2[j]:
        r = LCS(s1, s2, result, i-1, j-1)
        return r[0] + 1, r[1] + s1[i]
    r1 = LCS(s1, s2, result, i-1, j)
    r2 = LCS(s1, s2, result, i, j-1)
    return r1 if r1[0] > r2[0] else r2


if __name__ == "__main__":
    src = "TestCases_LCS.txt" if len(sys.argv) == 1 else sys.argv[1]
    with open(src, 'r') as tc:
        lines = tc.readlines()
        for index, line in enumerate(lines, start=1):
            if line != "\n":
                line = line.rstrip('\n')
                line = f'[ { line } ]'
                obj = json.loads(line)
                testCase, expectedResult = obj[0], obj[1]
                testResult = LCS(testCase[0], testCase[1])
                print(f"{index}.Is valid: {( expectedResult == testResult[1])} | Case: {testCase} | Answer: '{expectedResult}' | Result Value: '{testResult[1]}' | Result Length: {testResult[0]}")