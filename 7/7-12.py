# https://www.coursera.org/learn/python-osnovy-programmirovaniya/programming/iw02h/tieliefonnyie-nomiera

# Телефонные номера

# Телефонные номера в адресной книге мобильного телефона имеют один из
# следующих форматов:
# +7<код><номер>
# 8<код><номер>
# <номер>
# где <номер> — это семь цифр, а <код> — это три цифры или три цифры в круглых
# скобках. Если код не указан, то считается, что он равен 495. Кроме того, в
# записи телефонного номера может стоять знак “-” между любыми двумя цифрами
# (см. пример). На данный момент в адресной книге телефона Васи записано всего
# три телефонных номера, и он хочет записать туда еще один. Но он не может
# понять, не записан ли уже такой номер в телефонной книге. Помогите ему! Два
# телефонных номера совпадают, если у них равны коды и равны номера. Например,
# +7(916)0123456 и 89160123456 — это один и тот же номер.


def process_phone(text):
    DEFAULT_CODE = '495'
    symbols_to_del = ('-', '(', ')')
    for symbol in symbols_to_del:
        text = text.replace(symbol, '')

    if text[:2] == '+7':
        phone_number = text[2:5], text[5:]
    elif text[0] == '8':
        phone_number = text[1:4], text[4:]
    else:
        phone_number = DEFAULT_CODE, text
    return phone_number


phones_list = []
with open('input.txt') as finput:
    for line in finput:
        phones_list.append(process_phone(line.rstrip()))

phone_to_check = phones_list[0]
for i in range(1, len(phones_list)):
    print('YES' if phones_list[i] == phone_to_check else 'NO')
