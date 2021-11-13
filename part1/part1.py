# READING FILE
def readFile():
	wordFile = open("Test2.txt","r")
	return list([i.strip("\n") for i in wordFile])

###############
## VARIABLES ##
###############

# DEFINE BUCKET SORT
wordTimes = {}
# DEFINE BUTTON DICTIONARY
buttonMap = {
    'a': 2, 'b': 2, 'c': 2,
    'd': 3, 'e': 3, 'f': 3,
    'g': 4, 'h': 4, 'i': 4,
    'j': 5, 'k': 5, 'l': 5,
    'm': 6, 'n': 6, 'o': 6,
    'p': 7, 'q': 7, 'r': 7, 's': 7,
    't': 8, 'u': 8, 'v': 8,
    'w': 9, 'x': 9, 'y': 9, 'z': 9
}
# DEFINE TIME DICTIONARY
timeMap = {
    'a': 0, 'b': 0.25, 'c': 0.50,
    'd': 0, 'e': 0.25, 'f': 0.50,
    'g': 0, 'h': 0.25, 'i': 0.50,
    'j': 0, 'k': 0.25, 'l': 0.50,
    'm': 0, 'n': 0.25, 'o': 0.50,
    'p': 0, 'q': 0.25, 'r': 0.50, 's': 0.75,
    't': 0, 'u': 0.25, 'v': 0.50,
    'w': 0, 'x': 0.25, 'y': 0.50, 'z': 0.75
}
# DEFINE TIME CONSTANTS
WORD_LIST = readFile()
CAPITAL_TIME = 2.0
TOTAL_TIME_LIST = [0 for i in range(0,len(WORD_LIST))]
CURRENT_TIME_INDEX = 0





###############
## FUNCTIONS ##
###############

# GETTING TIME BETWEEN EACH BUTTON PRESS
def calculateTimeBetween(currentLetter, previousLetter):
  global TOTAL_TIME_LIST
  global CAPITAL_TIME
  # Add 2 seconds if the current letter is a capital
  total = 0
  if currentLetter.isupper():
    total += CAPITAL_TIME
  # Account for wait-time if letters are on the same button
  if (buttonMap[currentLetter.lower()] == buttonMap[previousLetter.lower()]):
    total += 0.5
  else:
    total += 0.25
  # Account for time it takes to press a letter
  total += timeMap[currentLetter.lower()]
  return total

# USE THE calculateTimeBetween FUNCTION TO COMPUTE TIME FOR AN ENTIRE WORD
def calculateWordTime():
	global CURRENT_TIME_INDEX
	currentWord = WORD_LIST[CURRENT_TIME_INDEX]
	for i in range(0,len(currentWord)):
		if i == 0:
			if (currentWord[0].isupper()):
				TOTAL_TIME_LIST[CURRENT_TIME_INDEX] += CAPITAL_TIME
			TOTAL_TIME_LIST[CURRENT_TIME_INDEX] += timeMap[currentWord[i].lower()]
		else:
			TOTAL_TIME_LIST[CURRENT_TIME_INDEX] += calculateTimeBetween(currentWord[i],currentWord[i-1])

	if (TOTAL_TIME_LIST[CURRENT_TIME_INDEX] not in wordTimes.keys()):
		wordTimes[TOTAL_TIME_LIST[CURRENT_TIME_INDEX]] = [currentWord]
	else:
		wordTimes[TOTAL_TIME_LIST[CURRENT_TIME_INDEX]].append(currentWord)

##########
## MAIN ##
##########

for word in WORD_LIST:
  calculateWordTime()
  CURRENT_TIME_INDEX+= 1
minTime = min(wordTimes.keys())
for i in wordTimes[min(wordTimes.keys())]:
	print(f"{i} = {minTime}s")
