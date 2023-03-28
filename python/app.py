
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

def handleInputString(inputResult):
    print('\nInput = %s' % inputResult)
    print('Length = %s \n' % len(inputResult))

    if inputResult in seen_strings:
        seen_strings[inputResult] += 1
    else:
        seen_strings[inputResult] = 1
        
if __name__ == '__main__':
    stringinate()



