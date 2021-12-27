def validateIntInput(prompt):
  while True:
    try:
      response = int(input(prompt))
      return response
    except:
      prompt = 'Please enter a number'

def checkPrime(num) -> str:
  i = 2

  while i < num:
    if(num % i == 0):
      return ''
    i += 1

  return f'{num} '