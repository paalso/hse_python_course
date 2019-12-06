# https://www.coursera.org/learn/python-osnovy-programmirovaniya/programming/Hs8PB/grazhdanskaia-oborona

# Гражданская оборона

# Штаб гражданской обороны Тридесятой области решил обновить план спасения на
# случай ядерной атаки. Известно, что все n селений области находятся
# вдоль одной прямой дороги. Вдоль дороги также расположены m бомбоубежищ, в
# которых жители селений могут укрыться на случай ядерной атаки.
# Чтобы спасение в случае ядерной тревоги проходило как можно эффективнее,
# необходимо для каждого селения определить ближайшее к нему бомбоубежище.
# Выведите n чисел - для каждого селения выведите номер ближайшего к нему
# бомбоубежища. Бомбоубежища пронумерованы от 1 до m в том порядке, в котором
# они заданы во входных данных.


def find_nearest_shelter_num(town, shelters, last_found_shelter_num=0):
    """ Заданы:
        - номер города
        - отсортированный список убежищ [(координата, номер в исх. списке)]
        - номер последнего найденного убежища
        Результат: номер следующего убежица для города town
    """
    total_shelters = len(shelters)

    nearest_shelter_num = last_found_shelter_num
    i = last_found_shelter_num + 1
    min_dist = abs(town[0] - shelters[last_found_shelter_num][0])

    while i < total_shelters:
        dist = abs(town[0] - shelters[i][0])
        if dist < min_dist:
            min_dist = dist
            nearest_shelter_num = i
        else:
            nearest_shelter_num = i - 1
            break
        i += 1

    return nearest_shelter_num


total_towns = int(input())
towns = list(map(int, input().split()))
total_shelters = int(input())
shelters = list(map(int, input().split()))


def car(pair):
    return pair[0]


ordered_towns = sorted([(towns[i], i) for i in range(total_towns)], key=car)

ordered_shelters = [(shelters[i], i) for i in range(total_shelters)]
ordered_shelters.sort(key=car)

optimal_shelters = [0 for i in range(total_towns)]

nearest = 0
for town in ordered_towns:
    nearest = find_nearest_shelter_num(town, ordered_shelters, nearest)
    optimal_shelters[town[1]] = ordered_shelters[nearest][1] + 1

print(*optimal_shelters)
