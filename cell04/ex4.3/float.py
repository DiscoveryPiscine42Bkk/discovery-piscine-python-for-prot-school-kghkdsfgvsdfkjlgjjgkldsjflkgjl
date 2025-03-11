#!/usr/bin/env python3

def main():
    number = input("Give me a number: ")
    try:
        num = float(number)
        if num.is_integer():
            print("This number is an integer.")
        else:
            print("This number is a decimal.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    main()
