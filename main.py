#Task20
def Factorial(n):
	if (n == 1):
		return 1
	return n*Factorial(n - 1)

NUMBER = 100
prelim = Factorial(100)
result = 0

for i in str(prelim):
	result += int(i)

print("THE RESULT:\t" + str(result))