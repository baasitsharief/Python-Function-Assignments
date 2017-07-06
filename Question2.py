import math

def yikes(x):
	m = math.exp(-x)
	return float(x*m+ math.sqrt(1-m))
