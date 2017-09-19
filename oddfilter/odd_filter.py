# Create a function that takes a list as a parameter,
# and returns a new list with every odd number from the orignal list
# example: [1, 2, 3, 4, 5] should produce [1, 3, 5]

# print(odd_filter([1, 2, 3, 4, 5]))  # should print [1, 3, 5]

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def odd_filter(numbers_list):
    odd_list = [i for i in numbers_list if i % 2 != 0]
    print(odd_list)

odd_filter(numbers)
