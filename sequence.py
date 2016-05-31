# Returns the numbers below a cap that follow any of the requirements
def numbersUnderThat(number, requirements):
    i = 0
    numberSet = []
    while number > i:
        for requirement in requirements:
            if requirement(i):
                numberSet.append(i)
                break
        i+=1
    return numberSet

# Returns the numbers below a cap that follow all of the requirements
def numbersUnderWhich(number, requirements):
    i = 0
    numberSet = []
    while number > i:
        allRequirementsFurfilled = True
        for requirement in requirements:
            if not requirement(i):
                allRequirementsFurfilled = False
                break

        if allRequirementsFurfilled:
            numberSet.append(i)
        i+=1
    return numberSet
