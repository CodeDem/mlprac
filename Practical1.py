# import scipy.integrate as integrate
# from math import cos, exp, pi
from scipy.integrate import quad

def main():
	print("Let f(x) = ((x**3) /5000) * (10 - x) for 0 <= x <= 10")
	print("Find P(1 <= x <= 4)")
	res, err = quad(f, 1, 4)
	print("P(1 <= x <= 4) = {:f} ".format(res))

def f(x):
	return (((x ** 3)/5000) * (10 - x))

if __name__ == '__main__':
	main()