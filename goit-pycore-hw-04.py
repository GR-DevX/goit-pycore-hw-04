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

# def total_salary(path):
#     try:
#         with open(path, 'r', encoding='utf-8') as file:
#             salaries = []
#             for line in file:
#                 try:
#                     name, salary = line.strip().split(',')
#                     salaries.append(int(salary))
#                 except ValueError:
#                     print(f"Помилка у форматі даних у рядку: {line.strip()}")
        
#         if not salaries:
#             return 0, 0
        
#         total = sum(salaries)
#         average = total / len(salaries)
#         return total, average
    
#     except FileNotFoundError:
#         print("Файл не знайдено.")
#         return None, None
#     except Exception as e:
#         print(f"Сталася помилка: {e}")
#         return None, None

# # Приклад використання:
# path = "path/to/salary_file.txt"
# total, average = total_salary("salary_file.txt")
# if total is not None:
#     print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")



# Завдання 2
# # Створюемо текстовий файл, який містить інформацію про котів.
# with open("cats.txt", "w", encoding="utf-8") as file:
#     file.write("60b90c1c13067a15887e1ae1,Tayson,3\n")
#     file.write("60b90c2413067a15887e1ae2,Vika,1\n")
#     file.write("60b90c2e13067a15887e1ae3,Barsik,2\n")
#     file.write("60b90c3b13067a15887e1ae4,Simon,12\n")
#     file.write("60b90c4613067a15887e1ae5,Tessi,5\n")


# def get_cats_info(path):
#     cats = []  # Список для зберігання інформації про котів

#     try:
#         with open(path, "r", encoding="utf-8") as file:  # Відкриваємо файл у режимі читання
#             for line in file:
#                 line = line.strip()  # Видаляємо пробіли та символи нового рядка
#                 if not line:  # Якщо рядок порожній, пропускаємо його
#                     continue

#                 parts = line.split(",")  # Розділяємо рядок за комами

#                 # Перевіряємо, чи є всі необхідні частини (id, ім'я, вік)
#                 if len(parts) != 3:
#                     print(f"Неправильний формат рядка: {line}")
#                     continue

#                 cat_id, name, age = parts  # Розпаковуємо значення

#                 # Створюємо словник для кота
#                 cat_info = {
#                     "id": cat_id,
#                     "name": name,
#                     "age": age
#                 }

#                 cats.append(cat_info)  # Додаємо словник до списку

#     except FileNotFoundError:
#         print(f"Помилка: Файл за шляхом '{path}' не знайдено.")
#     except Exception as e:
#         print(f"Виникла помилка: {e}")

#     return cats

# cats_info = get_cats_info("cats.txt")  

# print("Інформація про котів:")
# for cat in cats_info:
#     print(f"ID: {cat['id']}, Name: {cat['name']}, Age: {cat['age']}")

# Завдання 3