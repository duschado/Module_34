#!/usr/bin/python3

def control_(i):
	"""
	Checks whether the list is sorted.

	Checks whether the list is sorted in ascending order (recursive).
	"""
	
	if i < n - 1:
		
		if lst[i] > lst[i + 1]:
			return('The list is not sort.')
		
		elif lst[i] <= lst[i + 1]:
			return control_(i + 1)
			
			
i = 0	

n = input('Enter the number of items in the list\n > ')
n = int(n)

lst = []

for el in range(n):
	el = int(input('Enter the next element in the list\n > '))
	lst.append(el)

print(lst)

control_(i)

if control_(i) == 'The list is not sort.':
	print('The list is not sort.')
else:
	print ('The list is sort.')