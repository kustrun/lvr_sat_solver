from readWrite import *
from dpllSolver import *
from generator import *
import sys

writeDimacsFormat("input/45-queens.txt", 45, queensProblem(45))

# Tests
remainingVariables, conjunctiveClause = readDimacsFormat(sys.argv[1])

values = {}
status, solution = solveSat(conjunctiveClause, values, remainingVariables)

writeResultDimacsFormat (sys.argv[2], values)