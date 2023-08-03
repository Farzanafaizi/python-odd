numbers = [1, 2, 3, 4, 5, 6, 7, 8, 10]
print(numbers[4])

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 10]
numbers.remove(8)

print(numbers)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 10]
numbers.insert(3, 33)

print(numbers)


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 10]
numbers2 = [11, 12, 13, 14, 15, 16, 17, 18, 19]
numbers.extend(numbers2)

print(numbers)