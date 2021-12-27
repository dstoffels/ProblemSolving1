def compressString():
  userStr = input('Enter text to compress: ')

  outputStr = ''
  i = 0
  cnt = 1

  while i < len(userStr):
    while i < len(userStr) - 1 and userStr[i] == userStr[i+1]:
      cnt += 1 
      i += 1
    if(cnt > 1):
      outputStr += str(cnt) + userStr[i]
      cnt = 1
    else:
      outputStr += userStr[i]
    i += 1
  
  print(outputStr)

compressString()