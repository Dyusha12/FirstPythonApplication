import random

print("Hello Python from Visual Studio!")
s = "*" * 25
print(s)
print("Working on a new project")
print(s)
print("Initialization of the program...")
print("The program is ready!")
print(s)
new_string = "" #������� ������ ������
for i in range(1,11):
    if i % 2 == 0: #�������� �� ��, ��� ��� ������ �������
        while True:
            chislo = random.randint(0,8)#�������� ���������� ��������� �����
            if chislo % 2 == 0: #���� ����� ������
                new_string += str(chislo)#���������� �����
                break;
    if i % 2 != 0: #���� ������� ��������
        bukva = chr(random.randint(ord("a"),ord("z")))#���������� ��������� �����
        new_string += bukva #���������� �����
print("Your received string:",new_string)
