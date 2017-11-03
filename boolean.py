class Formula:
    pass

class Literal(Formula):
    def __init__(self, literal):
        self.literal = literal #Save literal

    def __str__(self):
        return str(self.literal) #Return literal value

    def evaluate(self, values):
        return values[self.literal] #Get literal T/F value

class Not(Formula):
    def __init__(self, literal):
        self.negatedLiteral = makeFormula(literal) #Save literal

    def __str__(self):
        return "!" + self.negatedLiteral.__str__() #Return negated literal value

    def evaluate(self, values):
        return not self.negatedLiteral.evaluate(values) #Evaluate literal

class And(Formula):
    def __init__(self, literals):
        self.conjunctionLiterals = [makeFormula(literal) for literal in literals] #Save all literals from array

    def __str__(self, parenthesis = False):
        return " & ".join(literal.__str__() for literal in self.conjunctionLiterals) #Return all literals joined by conjunction

    def evaluate(self, values):
        return all(literal.evaluate(values) for literal in self.conjunctionLiterals) #Check if all literal evaliations are T

class Or(Formula):
    def __init__(self, literals):
        self.disjunctionLiterals = [makeFormula(literal) for literal in literals] #Save all literals from array

    def __str__(self):
        return "(" + " | ".join(literal.__str__() for literal in self.disjunctionLiterals) + ")" #Return all literals joined by disjunction

    def evaluate(self, values):
        return any(literal.evaluate(values) for literal in self.disjunctionLiterals) #Check if at least one literal evaliation is T

def makeFormula(x):
    if isinstance(x, Formula):
        return x
    else:
        return Literal(x)