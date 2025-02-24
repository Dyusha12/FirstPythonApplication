import random

print("Hello Python from Visual Studio!")
s = "*" * 25
print(s)
print("Working on a new project")
print(s)
print("Initialization of the program...")
print("The program is ready!")
print(s)
new_string = "" #Создаем пустую строку
for i in range(1,11):
    if i % 2 == 0: #Проверка на то, что это четный элемент
        while True:
            chislo = random.randint(0,8)#Рандомно генерируем случайные числа
            if chislo % 2 == 0: #Если число четное
                new_string += str(chislo)#Записываем число
                break;
    if i % 2 != 0: #Если элемент нечетный
        bukva = chr(random.randint(ord("a"),ord("z")))#Генерируем случайные буквы
        new_string += bukva #Записываем букву
print("Your received string:",new_string)
