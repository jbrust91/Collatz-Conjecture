"""
Reproduce the Collatz Conjecture, which
states that you can take any number, n,
and if even, divide by 2, but if odd, 
multiply by 3 and add 1, you will 
eventually fall into a loop of 4, 2, 1.
"""

number=int(input("Pick any number:"))
while number>1:
	if number%2==0:
		number=number/2
		print(number)
	else:
		number=number*3+1
		print(number)


