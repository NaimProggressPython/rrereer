import time, sys


for i in range (1000, -1, -1):
	print (i, '\r', end= '')
	time.sleep(0.04)
if i == 0:
	print('Я тебя люблю')

input()