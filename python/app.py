import string
import datetime

seen_strings = {}


def stringinate():
    while True:
        # Take user input
        inputResult = input(
            'Enter an input string (\'stats\' to see statistics, \'quit\' to exit): ')

        # Handle "quit" input
        if (inputResult.lower() == "quit"):
            outputEndStats(seen_strings)
            print('Exiting...\n')
            break

        # Handle "stats" input
        elif (inputResult.lower() == "stats"):
            handleStats(seen_strings)
            
        # Handle an input string
        else:
            handleInputString(inputResult)

def handleStats(seen_strings):
    print('\nStats:\n %s\n' % seen_strings)
    mostPopularString(seen_strings, quit_status=False)
    longestString(seen_strings, quit_status=False) 
            
def mostPopularString(seen_strings, quit_status):
    # find max of all string counts
    maxCount = max(seen_strings.values())
    
    # find associated string(s)
    print('Most popular strings(s): ', end='')
    for string, count in seen_strings.items(): 
        if count == maxCount:
            print(string, ' ', end='')
    print('\n')
    
def longestString(seen_strings, quit_status):
    # find max length
    maxLength = 0
    for string in seen_strings.keys():
        if len(string) > maxLength:
            maxLength = len(string)
    
    # find longest string(s)
    longest = [] # account for multiple strings to be of max length
    for string in seen_strings.keys():
        if len(string) == maxLength:
            longest.append(string)
            
    print("Longest input received: ", end='')
    for string in longest:
        print(string)
        
        

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
    print('Most frequent character(s): ', end='')
    for char, count in charCounts.items(): 
        if count == maxCount:
            print(char, ' ', end='')
    print('\nFrequency = %d\n' % maxCount)
    


def handleInputString(inputResult):
    print('\nInput = %s' % inputResult)
    print('Length = %s' % len(inputResult))

    mostFrequentChar(inputResult)
    
    # add input string to seen_strings dict and increment count
    if inputResult in seen_strings:
        seen_strings[inputResult] += 1
    else:
        seen_strings[inputResult] = 1

def outputEndStats(seen_strings):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("stats.txt", "a") as f:
        f.write(f"Timestamp: {timestamp}\n")
        f.write(f"Stats: {seen_strings}\n")
        
        
    
    
    
if __name__ == '__main__':
    stringinate()
