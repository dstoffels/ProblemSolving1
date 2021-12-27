from helpers import validateIntInput, checkPrime


def primeNumbers():
  upperRange = validateIntInput('Enter a number and I will count all primes between 1 and your number: ')
  numOutputStr = ''
  i = 2
  
  while i <= upperRange:
    numOutputStr += checkPrime(i)
    i += 1 
  print(numOutputStr)

primeNumbers()