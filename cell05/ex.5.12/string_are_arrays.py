import sys

if len(sys.argv) == 2:
    input_string = sys.argv[1]
    
    occurrences = input_string.count('z')
    
    if occurrences > 0:
        print('z' * occurrences)
    else:
        print('none')
else:
    print('none')
