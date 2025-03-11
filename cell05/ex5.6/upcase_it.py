import sys

# Check if exactly one parameter is passed
if len(sys.argv) == 2:
    # Display the string in uppercase
    print(sys.argv[1].upper())
else:
    # Display 'none' if the number of parameters is different from 1
    print('none')
