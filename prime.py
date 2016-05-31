
# returns the prime factors of a number in the form of an array
def primeFactor(number):
    divisor = 2
    while(number != divisor):
        if(number % divisor == 0):
            primes = primeFactor(divisor)
            primes.extend(primeFactor(number / divisor))
            return primes
        divisor+=1
    return [number]

# returns if the number is prime or not
def isPrime(number):
    divisor = 2
    while(number != divisor):
        if(number % divisor == 0):
            return False
        divisor+= 1
    return True

# returns all the primes under a certain number
def getPrimesUnder(number):
    i = 2
    primes = []
    while(number > i):
        if(isPrime(i)):
            primes.append(i)
        i+=1
    return primes
