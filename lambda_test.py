# lambda_test.py

def find_special_numbers(special_selector, limit=10):
	found = []
	n = 0
	while len(found) < limit:
		if special_selector(n):
			found.append(n)
		n += 1
	return found

add = lambda x, y: x + y
print((lambda x, y: x + y(4,5))