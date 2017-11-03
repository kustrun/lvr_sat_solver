from boolean import *

def readDimacsFormat(fileName):
    with open(fileName, 'r') as f:
        while True:
            line = f.readline()

            #Read until the end of the file
            if not line:
                break

            if line[0] == "c": #Print out comment
                print(fileName + ": comment=" + line[2:])
            elif line[0] == "p": #Print out data parameters
                parameters = line[2:].split()  # 0 = clauses format, 1 = number of variables, 2 = number of clauses
                print(fileName + ": clauses format=" + parameters[0] + ", number of variables=" + parameters[
                    1] + ", number of clauses=" + parameters[2])

                conjunctiveClause = And([]) #Variable for storing CNF
                #Read clauses and convert them to conjunctive normal form
                for i in range(0,int(parameters[2])):
                    clause = f.readline()   #Read whole line
                    splitClause = clause.split()    #Split data at space
                    del splitClause[-1] #Remove last array element - 0 element

                    for i in range(0,splitClause.__len__()):    #Iterate over elements
                        number = int(splitClause[i])    #Get element int value
                        splitClause[i] = (number if number > 0 else Not(abs(number))) #Rewrite element as element or its negation

                    conjunctiveClause.conjunctionLiterals.append(Or(splitClause))   #Append Or clause to CNF

                return conjunctiveClause #Return CNF

def writeDimacsFormat(fileName, values):
    with open(fileName, 'w') as f:
        for key, value in values.items(): #Iterate over dictonary keys and values
            if value:   #If values is true
                f.write(str(key) + " ") #Return element
            else: #If value is false
                f.write(str(-key) + " ") #Return negation of element