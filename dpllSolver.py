from boolean import *
from random import randint
import copy

def solveSat(clause, values, remainingVariables):
    if isinstance(clause, type(T)) and clause == T:
        return T, values
    elif isinstance(clause, type(F)) and clause == F:
        return F, {}

    randomVariable = pickRandomVariable(remainingVariables)

    values[randomVariable] = True
    leftClause = And([])
    leftClause = clause.simplify(values, leftClause)
    leftRemainingVariables = getRemainingVariables(leftClause)

    leftStatus, leftValues = solveSat(leftClause, values, leftRemainingVariables)
    if isinstance(leftStatus, type(T)) and leftStatus == T:
        return T, leftValues

    values[randomVariable] = False
    rightClause = And([])
    rightClause = clause.simplify(values, rightClause)
    rightRemainingVariables = getRemainingVariables(rightClause)

    rightStatus, rightValues = solveSat(rightClause, values, rightRemainingVariables)
    if isinstance(rightStatus, type(T)) and rightStatus == T:
        return T, rightValues

    del values[randomVariable]

    return F, {}

def pickRandomVariable(remainingVariables):
    return remainingVariables[randint(0, len(remainingVariables) - 1)]

def getRemainingVariables(clause):

    if isinstance(clause, type(F)) and clause == F:
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
