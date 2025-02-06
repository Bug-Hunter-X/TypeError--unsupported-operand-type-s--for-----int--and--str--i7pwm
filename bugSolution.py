def calculate_average(numbers):
    numeric_numbers = [num for num in numbers if isinstance(num, (int, float))]
    if not numeric_numbers:
        return 0
    total = sum(numeric_numbers)
    average = total / len(numeric_numbers)
    return average

my_list = []
result = calculate_average(my_list) 
print(f"The average is: {result}") #This will return 0 as expected

my_list = [10, 20, 30, 40, 50]
result = calculate_average(my_list) 
print(f"The average is: {result}") #This will return 30.0 as expected

my_list = [10, 20, 30, 40, 50, 'a']
result = calculate_average(my_list)
print(f"The average is: {result}") #This will return 30.0 as expected because it ignores the string