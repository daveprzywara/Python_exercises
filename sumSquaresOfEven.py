'''
Python function which, when called with a list of integers, 
returns the sum of the squares of all even members of that list.
'''


def sumList(lst):
	newTab = []
	for i in lst:
		if i % 2 == 0:
			i *= i
			newTab.append(i)
	return sum(newTab)
