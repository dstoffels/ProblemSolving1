from helpers import validateIntInput

def runFibonacciSequence():
  MAX = 20

  num = validateIntInput('Enter a number to begin a 20-digit fibonacci sequence: ')
  i = 0
  prevNum1 = 0
  prevNum2 = 0
  outputStr = ''

  while i < MAX:
    outputStr += f'{num} '
    prevNum2 = prevNum1
    prevNum1 = num
    num = prevNum1 + prevNum2
    i += 1
  
  print(outputStr)

runFibonacciSequence()