class Formula:
    pass

class Literal(Formula):
    def __init__(self, literal):
        self.literal = literal #Save literal

    def __str__(self):
        return str(self.literal) #Return literal value

    def evaluate(self, values):
        if self.literal in values:
            return values[self.literal] #Get literal T/F value

        return self

    def simplify(self, values):
        if self.literal in values:
            if values[self.literal]:
                return T
            else:
                return F
        else:
            return self

class Not(Formula):
    def __init__(self, literal):
        self.negatedLiteral = makeFormula(literal) #Save literal

    def __str__(self):
        return "!" + self.negatedLiteral.__str__() #Return negated literal value

    def evaluate(self, values):
        return not self.negatedLiteral.evaluate(values) #Evaluate literal

    def simplify(self, values):
        if self.negatedLiteral.literal in values:
            if values[self.negatedLiteral.literal]:
                return F
            else:
                return T
        else:
            return self

class And(Formula):
    def __init__(self, literals):
        self.conjunctionLiterals = [makeFormula(literal) for literal in literals] #Save all literals from array

    def __str__(self, parenthesis = False):
        if len(self.conjunctionLiterals) == 0:
            return "T"

        return " & ".join(literal.__str__() for literal in self.conjunctionLiterals) #Return all literals joined by conjunction

    def evaluate(self, values):
        return all(literal.evaluate(values) for literal in self.conjunctionLiterals) #Check if all literal evaliations are T

    def simplify(self, values, object):
        object.terms = [literal.simplify(values, Or([])) for literal in self.conjunctionLiterals]
        if F in object.terms:
            return F

        object.conjunctionLiterals = [literal for literal in object.terms if literal != T]
        if len(object.conjunctionLiterals) == 0:
            return T

        return object

class Or(Formula):
    def __init__(self, literals):
        self.disjunctionLiterals = [makeFormula(literal) for literal in literals] #Save all literals from array

    def __str__(self):
        if len(self.disjunctionLiterals) == 0:
            return "F"

        return "(" + " | ".join(literal.__str__() for literal in self.disjunctionLiterals) + ")" #Return all literals joined by disjunction

    def evaluate(self, values):
        return any(literal.evaluate(values) for literal in self.disjunctionLiterals) #Check if at least one literal evaliation is T

    def simplify(self, values, object):
        object.terms = [literal.simplify(values) for literal in self.disjunctionLiterals]
        if T in object.terms:
            return T

        object.disjunctionLiterals = [literal for literal in object.terms if literal != F]
        if len(object.disjunctionLiterals) == 0:
            return F

        return object

T = And([])
F = Or([])



def makeFormula(x):
    if isinstance(x, Formula):
        return x
    else:
        return Literal(x)