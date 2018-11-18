#!/usr/bin/python3

line = input('Enter the phrase\n > ')

for char in '.,:!?-/':
	line = line.replace(char, '')

LINE = line.split(' ')
LINE.sort()

LINE_1 = []

for  i in range(0, len(LINE)):
	n = LINE.count(LINE[i])
	n = str(n)
	LINE_1.append(LINE[i] + ':' + n)
	n = int(n)
	
for i in range(len(LINE_1) - 1): 
	j = i + 1 
	while j <= len(LINE_1) - 1: 
		if LINE_1[i] == LINE_1[j]: 
			LINE_1.pop(j) 
			j-= 1 
		j += 1 

print(LINE_1)