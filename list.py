def removeodd(numbers):
    return [n for n in numbers if n % 2 == 0]

numbers = [1, 2, 3, 4, 5]
even_numbers = removeodd(numbers)

print("Original:", numbers)
print("Even only:", even_numbers)