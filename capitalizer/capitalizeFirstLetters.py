from helpers import splitWords, capitalizeEachWord, concatenateWords

def capitalizeFirstLetters():
  userStr = input('Enter text to captitalize the first letter of each word: ')  

  words = splitWords(userStr, ' ')
  capitalizedWords = capitalizeEachWord(words)
  output = concatenateWords(capitalizedWords, ' ')

  print(output)

capitalizeFirstLetters()