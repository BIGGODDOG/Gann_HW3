# Напишите программу для создания списка, длина которого равна N. После создания
# списка нужно подсчитать нечетные и четные числа. Если нечетных чисел больше, чем четных,
# вывод должен быть «Нет», в остальных ключах «Да».

# Input
# 5
# 4 16 19 31 2
# Output
# 19 31
# 4 16 2
# YES

def process_list(N):
    lst = []

    print(f"Введите {N} чисел:")
    for i in range(N):
        number = int(input(f"Элемент {i+1}: "))
        lst.append(number)
    
    # Разделяем числа на четные и нечетные
    odd_numbers = [x for x in lst if x % 2 != 0]
    even_numbers = [x for x in lst if x % 2 == 0]
    
    # Нечетные числа
    print("Нечетные числа:", odd_numbers)
    
    # Четные числа
    print("Четные числа:", even_numbers)
    
    # Проверяем соотношение
    if len(odd_numbers) > len(even_numbers):
        print("NO")
    else:
        print("YES")

N = int(input("Введите длину списка: "))
process_list(N)