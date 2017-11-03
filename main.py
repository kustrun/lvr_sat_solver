from readWrite import *
import sys

#Tests
conjunctiveFormula = readDimacsFormat(sys.argv[1])
print(conjunctiveFormula)

values = {1: False, 2:True, 3: True}
print(conjunctiveFormula.evaluate(values))

writeDimacsFormat(sys.argv[2], values)