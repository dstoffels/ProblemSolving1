def reverseString():
  userStr = input('Enter text to reverse it: ')

  reversedStr = ''
  i = len(userStr) -1
  while i >= 0:
    reversedStr += userStr[i]
    i -= 1
  print(reversedStr)

reverseString()
