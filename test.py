

a = [9, 2, 5, 3, 6, 8, 4]

array = [1, 2, 5, 3, 6, 8, 4]
for i in range(len(array) - 1, 0, -1):
    print i
    for j in range(0, i):
        print j
        if array[j] > array[j + 1]:
            array[j], array[j + 1] = array[j + 1], array[j]
print array

----------



test = [x ** 2 for x in range(8) if not x % 2]


for i in test:
	print i
print test


12322323213123123
