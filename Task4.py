# Написать рекурсивную функцию, которая по заданному целому числу возвращает n-e
# число Фибоначчи. Ряд Фибоначчи 0, 1, 1, 2, 3, 5, 8, 13,……
# Output:
# fibonacci number 1 = 1
# fibonacci number 2 = 1
# fibonacci number 3 = 2
# fibonacci number 4 = 3
# fibonacci number 5 = 5
# fibonacci number 6 = 8
# fibonacci number 7 = 13
# fibonacci number 8 = 21
# fibonacci number 9 = 34
# fibonacci number 10 = 55

def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# Вывод
for i in range(1, 11):
    print(f"fibonacci number {i} = {fibonacci(i)}")
