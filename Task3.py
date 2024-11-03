# Напишите программу СV (резюме), которая будет считывать данные пользователя,
# через функцию, и выведет полученные данные, при вызове в основном теле программы.
# Шаблон резюме ниже:

def read_cv_from_file(filename):
    # Функция для считывания данных из файла
    cv_data = {}
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            key, value = line.strip().split(': ', 1)  # Разделяем ключ и значение
            cv_data[key] = value
    return cv_data

def display_cv(cv_data):
    # Функция для вывода данных в формате резюме
    print("\nРезюме:")
    for key, value in cv_data.items():
        print(f"{key}: {value}")

# Основная программа
filename = 'cv_data.txt'  # Имя файла с данными резюме
cv_data = read_cv_from_file(filename)
display_cv(cv_data)