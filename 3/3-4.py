# https://www.coursera.org/learn/python-osnovy-programmirovaniya/programming/DalOx/tsiena-tovara/submission

# Цена товара
# Цена товара обозначена в рублях с точностью до копеек, то есть 
# действительным числом с двумя цифрами после десятичной точки. 
# Запишите в две целочисленные переменные стоимость товара в виде 
# целого числа рублей и целого числа копеек и выведите их на экран. 
# При решении этой задачи нельзя пользоваться условными инструкциями 
# и циклами.

price = float(input())

price_rub = int(price)

s = "%.2f" % price
price_cop = int(s[len(s)-2:len(s)])

print(price_rub, price_cop)
