x = 2555
e = 0.0001
high = x
low = 0
ans = (low + high) / 2.0
numGuesses = 0

while abs(ans**2 - x) > e:

	numGuesses += 1
	if ans**2 - x > e:
		high = ans
	
	elif ans**2 - x < e:
	
		low = ans
	
	ans = (low + high) / 2.0
	
print(str(ans) + 'is close to the square root of ' + str(x))