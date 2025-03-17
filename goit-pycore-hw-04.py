# filename = "salary_file.txt"

# # Данные для записи
# data = """Alex Korp,3000
# Nikita Borisenko,2000
# Sitarama Raju,1000
# """

# # Создание и запись файла
# with open(filename, 'w', encoding='utf-8') as file:
#     file.write(data)

# print(f"Файл '{filename}' успешно создан.")

# import os
# print("Поточна робоча директорія:", os.getcwd())

# Завдання 1

def total_salary(path):
    try:
        with open(path, 'r', encoding='utf-8') as file:
            salaries = []
            for line in file:
                try:
                    name, salary = line.strip().split(',')
                    salaries.append(int(salary))
                except ValueError:
                    print(f"Помилка у форматі даних у рядку: {line.strip()}")
        
        if not salaries:
            return 0, 0
        
        total = sum(salaries)
        average = total / len(salaries)
        return total, average
    
    except FileNotFoundError:
        print("Файл не знайдено.")
        return None, None
    except Exception as e:
        print(f"Сталася помилка: {e}")
        return None, None

# Приклад використання:
path = "path/to/salary_file.txt"
total, average = total_salary("salary_file.txt")
if total is not None:
    print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")



# Завдання 2

