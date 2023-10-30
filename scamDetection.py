import numpy as np
from sklearn.neural_network import MLPClassifier


# functions to prepare data to train the model

# input: string of length one word
# output: string of modified ascii codes (each char has its unique code) corresponding
#         to each character in string, so each word has a unique encoding
def convert(s):
  result = ""
  if (s == None or len(s) == 0):
    return
  for char in s:
    encoding = ord(char)
    if (encoding < 58):
      encoding = encoding - 38
    else:
      encoding = encoding - 25
    result = result + str(encoding)
  return int(result)

# input: string of one text message
# output: array of characters grouped in words in the message, displayed in ascii
def inputText(text):
  while (len(text) > 2**63 - 1):
    print("Error: text file is too large, please reenter: \n")
    text = input()
  text = text + ' '
  textToNum = []
  word = []
  for char in text:
    num = ord(char)
    if (num > 47 and num < 58 or num > 64 and num < 91 or num > 96 and num < 123):
      word.append(char)
    else:
      if (len(word) != 0):
        textToNum.append(int(convert(word)))
        if (len(textToNum) == inputLength):
          break
        word = []
  while (len(textToNum) < inputLength):
    textToNum.append(0)
  return textToNum


# inputting training data into model

clf = MLPClassifier(hidden_layer_sizes=(25,50))

numTrains = 5000  # out of 5324
numTests = 50     # out of 250
inputLength = 100

# for y in model.fit(X,y)
result = [] # 2d array

# for X in model.fit(X,y)
inputs = [] # 2d array

with open('SMSSpamCollection.txt','r') as file:

  # reading each line
  for line in file:

    # reading each word
    for item in line.split('\t'):
      if (item == 'ham'):
        result.append(0)
      elif (item =='spam'):
        result.append(1)
      else:
        inputs.append(inputText(item))

#for i in range(len(result)):
#  print(inputs[i])
#  print(result[i])


# training the model
clf.fit(inputs[0:numTrains], result[0:numTrains])

# testing the model
for i in range(numTests):
    print(np.array(inputs[5250+numTests]).shape)
    print(clf.predict([inputs[5250+numTests]]))
#score(inputs[5250:5250+numTests], result[5250:5250+numTests])
