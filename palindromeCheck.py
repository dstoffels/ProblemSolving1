def checkPalindrome():
  userStr = input('Enter text to check if it is a palindrome: ').upper()

  reversedStr = ''
  i = len(userStr) -1
  while i >= 0:
    reversedStr += userStr[i]
    i -= 1

  if(userStr == reversedStr):
    print(f'{userStr} is a palindrome!')
  else:
    print(f'{userStr} backward is {reversedStr}, it is not a palindrome')

checkPalindrome()