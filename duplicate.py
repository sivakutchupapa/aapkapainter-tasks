def printFirstRepeating(arr, n):

	Min = -1

	myset = dict()

	for i in range(n - 1, -1, -1):
	
		if arr[i] in myset.keys():
			Min = i

		else: 
			myset[arr[i]] = 1
	
	if (Min != -1):
		print("The first repeating element is",
									arr[Min])
	else:
		print("There are no repeating elements")


arr = [1, 2, 3, 2, 4]
n = len(arr)
printFirstRepeating(arr, n)



