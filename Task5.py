# Напишите функцию, которая проверяет является ли число степенью двойки. Если
# истинно выведите True, иначе False.
# Input
# 8
# Output
# True 

def is_power_of_two(n):
    return n > 0 and (n & (n - 1)) == 0

number = 8
print(is_power_of_two(number))  # True

number = 12
print(is_power_of_two(number))  # False