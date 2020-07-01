#h stands for hypotenuse#
#hypotenuse is the longest side of a pythogorean triangle#


while True:
	a = int(input('Enter the first side: '))
	b = int(input('Enter the second side: '))
	c = int(input('Enter the third side: '))
	h = max(a, b, c)
	

	if h == c and (a**2) + (b**2) == h**2:
		print(' Triangle is a pythogorean tripple ')
	elif h == b and (a**2) + (c**2) == h**2:
		print(' Triangle is a pythogorean tripple ')
	elif h == a and (c**2) + (b**2) == h**2:
		print(' Triangle is a pythogorean tripple ')
	else:
		print(' Triangle is not a pythogorean tripple ')