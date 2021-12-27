def splitWords(inputStr, delimiter):
  word = ''
  words = []

  for char in inputStr:
    if(char == delimiter):
      words.append(word)
      word = ''
    else:
      word += char
  words.append(word)

  return words

def capitalizeFirstLetter(word: str):
  capitalizedWord = ''
  i = 0
  while i < len(word):
    char = ''
    if(i == 0):
      char = word[i].upper()
    else:
      char = word[i]
    capitalizedWord += char
    i += 1
  return capitalizedWord

def capitalizeEachWord(words : list[str]):
  i = 0
  for word in words:
    words[i] = capitalizeFirstLetter(word)
    i += 1
  return words

def concatenateWords(words: list[str], delimiter):
  concatenatedStr = ''
  for word in words:
    concatenatedStr += word + delimiter
  return concatenatedStr