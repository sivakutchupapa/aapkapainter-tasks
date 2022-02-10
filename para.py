'''
# Python code to check if two strings are
# anagram
from collections import Counter

def anagram(input1, input2):
	return Counter(input1) == Counter(input2)
string_ = input('Enter Anagram String:')
input1 = string_.split()[0].lower()
input2 = string_.split()[1].lower()

print(anagram(input1, input2))

'''



