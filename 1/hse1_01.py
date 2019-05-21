# https://www.coursera.org/learn/python-osnovy-programmirovaniya/programming/wtrK6/hello-username

# Hello, %username!
# Напишите программу, которая приветствует пользователя, выводя слово Hello, 
# введенное имя и знаки препинания по образцу (см. пример входных и выходных данных). 
# Программа должна считывать в строковую переменную значение и писать соответствующее приветствие

name = input()
print("Hello, ", name, "!", sep='')
