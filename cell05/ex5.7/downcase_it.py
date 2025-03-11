#!/usr/bin/env python3
import sys

# Check if exactly one parameter is passed
if len(sys.argv) == 2:
    # Display the string in lowercase
    print(sys.argv[1].lower())
else:
    # Display 'none' if the number of parameters is different from 1
    print('none')
