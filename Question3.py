import math
import cmath

def roots(a,b,c):
	D = pow(b,2) - 4*a*c
	if D<0:
		print(complex((b+cmath.sqrt(D))/2))
		print(complex((b-cmath.sqrt(D))/2))
	else:
		print((b+math.sqrt(D))/2)
		print((b-math.sqrt(D))/2)
	