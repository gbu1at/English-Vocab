
def percentageMatches(correctAnswer: str, usersAnswer: str):
    n = correctAnswer.__len__()
    m = usersAnswer.__len__()

    line = [i for i in range(n + 1)]
    nextLine = [0] * (n + 1)

    for i in range(m):
        for j in range(1, n + 1):
            if correctAnswer[j - 1] == usersAnswer[i]:
                nextLine[j] = line[j - 1]
            else:
                nextLine[j] = min(nextLine[j - 1], line[j], line[j - 1]) + 1
        line = nextLine
        nextLine = [0] * (n + 1)

    cnt = line[n]

    return (100 * m) // (m + cnt ** 2)
