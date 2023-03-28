import string

seen_strings = {}


def stringinate():
    while True:
        # Take user input
        inputResult = input(
            'Enter an input string (\'stats\' to see statistics, \'quit\' to exit): ')

        # Handle "quit" input
        if (inputResult.lower() == "quit"):
            print('Exiting...\n')
            break

        # Handle "stats" input
        elif (inputResult.lower() == "stats"):
            print('\nStats:\n %s\n' % seen_strings)

        # Handle an input string
        else:
            handleInputString(inputResult)


def mostFrequentChar(inputResult):
    charCounts = {}
    
    # store punctuation in a string
    punctuation = string.punctuation
    
    # build dictionary with chars as keys and counts as values
    for char in inputResult:
        # ignore punctuation
        if char not in punctuation and char != ' ':
            if char in charCounts:
                charCounts[char] += 1
            else:
                charCounts[char] = 1
            
    # find max of all counts
    maxCount = max(charCounts.values())
    
    # find associated char(s)
    print('The most frequent character(s) is/are:')
    for char, count in charCounts.items(): 
        if count == maxCount:
            print(char, ' ')
    print('Frequency = %d\n' % maxCount)
    


def handleInputString(inputResult):
    print('\nInput = %s' % inputResult)
    print('Length = %s' % len(inputResult))

    mostFrequentChar(inputResult)
    
    if inputResult in seen_strings:
        seen_strings[inputResult] += 1
    else:
        seen_strings[inputResult] = 1


if __name__ == '__main__':
    stringinate()
