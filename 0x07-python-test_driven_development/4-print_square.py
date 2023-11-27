#!/usr/bin/python3
"""Defining a function of  square-printing."""


def print_square(size):
	"""Printing a square with the char #.
		Raises:
TypeError: If the size is not an int.
	ValueError: If size is less than 0
	 """
	 if not isinstance(size, int):
		 raise TypeError("size must be an integer")
		 if size < 0:
		 raise ValueError("size must be >= 0")

		 for y in range(size):
			 [print("#", end="") for u in range(size)]
			  print("")

