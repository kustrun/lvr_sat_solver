from boolean import *
from random import randint
import copy

def solveSat(clause, values, remainingVariables):
    if clause == T:
        return T, values
    elif clause == F:
        return F, {}

    unitStatus, unitValues = getUnitValues(clause)
    if unitStatus == F:
        return F, {}

    for key in unitValues:
        values[key] = unitValues[key]

        if int(key) in remainingVariables:
            remainingVariables.remove(int(key))

    randomVariable = pickRandomVariable(remainingVariables)

    values[randomVariable] = True
    leftClause = And([])
    leftClause = clause.simplify(values, leftClause)
    leftRemainingVariables = getRemainingVariables(leftClause)

    leftStatus, leftValues = solveSat(leftClause, values, leftRemainingVariables)
    if leftStatus == T:
        return T, leftValues

    values[randomVariable] = False
    rightClause = And([])
    rightClause = clause.simplify(values, rightClause)
    rightRemainingVariables = getRemainingVariables(rightClause)

    rightStatus, rightValues = solveSat(rightClause, values, rightRemainingVariables)
    if rightStatus == T:
        return T, rightValues

    del values[randomVariable]

    for key in unitValues:
        if key in values:
            del values[key]

    return F, {}

def pickRandomVariable(remainingVariables):
    return remainingVariables[randint(0, len(remainingVariables) - 1)]

def getUnitValues(clause):
    unitValues = {}
    for orLiteral in clause.conjunctionLiterals:
        literals = orLiteral.disjunctionLiterals
        if len(literals) == 1:
            if isinstance(literals[0], Literal):

                if literals[0].literal in unitValues and unitValues[literals[0].literal] == False:
                    return F, {}

                unitValues[literals[0].literal] = True
            elif isinstance(literals[0], Not):

                if literals[0].negatedLiteral.literal in unitValues and unitValues[literals[0].negatedLiteral.literal] == True:
                    return F, {}

                unitValues[literals[0].negatedLiteral.literal] = False

    return T, unitValues

def getRemainingVariables(clause):

    if clause == F:
        return []

    remainingVariables = []
    for orLiteral in clause.conjunctionLiterals:
        for literal in orLiteral.disjunctionLiterals:
            if isinstance(literal, Literal):
                value = literal.literal
                if value not in remainingVariables:
                    remainingVariables.append(value)
            elif isinstance(literal, Not):
                value = literal.negatedLiteral.literal
                if value not in remainingVariables:
                    remainingVariables.append(value)

    return remainingVariables
