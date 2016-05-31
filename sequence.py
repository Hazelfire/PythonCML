# Returns the numbers below a cap that follow a requirement
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
