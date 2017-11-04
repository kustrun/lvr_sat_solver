from readWrite import *
from dpllSolver import *
import sys
import copy

#Tests
remainingVariables, conjunctiveClause = readDimacsFormat(sys.argv[1])

values = {}
status, solution = solveSat(conjunctiveClause, values, remainingVariables)

print(status)
print(solution)
print(conjunctiveClause.evaluate(solution))