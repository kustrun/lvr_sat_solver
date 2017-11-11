# Each field is represented by value from 1 to n*n
# n = 4
# 1   2   3   4
# 5   6   7   8
# 9   10  11  12
# 13  14  15  16

def queensProblem(n):
    problem = []

    # generator rule
    for i in range(0, n):
        clause = []
        for j in range(1, n + 1):
            clause.append(j + n * i)

        problem.append(clause)
    # end of generator rule

    # constraints on rows
    for i in range(0, n):
        for j in range(1, n):
            number = j + n * i
            for k in range(1, n - j + 1):
                problem.append([-number, -(number+k)])
    # END of constraints on rows

    # constraints on columns
    for j in range(1, n + 1):
        for i in range(0, n):
            number = j + n * i
            for k in range(1, n - i):
                problem.append([-number, -(number+n*k)])
    # END of constrains on columns

    # constraints on NW->SE diagonal
    # part 1, upper bound triangle
    for i in range(0, n - 1):
        for j in range(i, n - 1):
            number = j + 1 + n * i
            for k in range(1, n - j):
                problem.append([-number, -(number + k * (n + 1))])

    # part 2, lower bound triangle
    for i in range(0, n - 1):
        for j in range(0, i):
            number = j + 1 + n * i
            for k in range(1, n - i):
                problem.append([-number, -(number + k * (n + 1))])
    # END of constraints on NW->SE diagonal

    # constraints on NE->SW diagonal
    # part 1, upper bound triangle
    for i in range(0, n):
        for j in range(0, n - i):
            number = j + 1 + n * i
            for k in range(1, j + 1):
                problem.append([-number, -(number + k * (n - 1))])

    # part 2, lower bound triangle
    for i in range(0, n):
        for j in range(n - i, n):
            number = j + 1 + n * i
            if (number != n * n):
                for k in range(1, n - i):
                    problem.append([-number, -(number + k * (n - 1))])
    # END of constraints on NE->SW diagonal

    return problem