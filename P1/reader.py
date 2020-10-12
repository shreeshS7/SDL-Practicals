
"""1) Getting Started with Python (Example Word count exercise)"""

file = open('file.txt','rt')
data = file.read()
word_list = data.split()

word = input("Enter word : ")

count = 0

for item in word_list:
	if item == word:
		count += 1

print(count)
