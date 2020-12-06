"""
Middle Grade Stem - Python
Assignment 8.8

INSTRUCTIONS:
Ask the user for a number; then, print out that number.
However, make it so that if they accidentally enter not a number,
the error is contained, and the program prints out an error message.

EXAMPLE OUTPUT:
420

"""
try:
	x = int(input("Enter a number: "))
	print(x)
except ValueError:
	print("an error message")

