# https://www.coursera.org/learn/python-osnovy-programmirovaniya/programming/30kXq/slieduiushchieie-i-priedydushchieie

# Задание по программированию: Следующее и предыдущее

# Напишите программу, которая считывает целое число и выводит текст, аналогичный приведенному 
# в примере (важно в точности соблюдать вывод программы: обратите внимание на пробелы и на точки). 
# Нельзя пользоваться конкатенацией строк, используйте print с несколькими параметрами.

n = int(input())

prev_text = 'The previous number for the number '
next_text = 'The next number for the number '

print(next_text, n, ' is ', n + 1, '.', sep='')
print(prev_text, n, ' is ', n - 1, '.', sep='')

