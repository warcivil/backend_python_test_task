import re
from math import sqrt

# медленная сортировка, но для точек от 1 до 256 пойдеи вполне
def bubble_sort(nums):
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(nums) - 1):
            if abs(nums[i][0]) > abs(nums[i + 1][0]):
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                swapped = True
            elif abs((nums[i][0])) == abs(nums[i + 1][0]):
                if abs(nums[i][1]) > abs(nums[i + 1][1]):
                    nums[i], nums[i + 1] = nums[i + 1], nums[i]
                    swapped = True


def inverted_bubble_sort(nums):  # сортировка для области где x, y < 0
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(nums[1]) - 1):
            if abs(nums[i][0]) < abs(nums[i + 1][0]):
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                swapped = True
            elif abs((nums[i][0])) == abs(nums[i + 1][0]):
                if abs(nums[i][1]) > abs(nums[i + 1][1]):
                    nums[i], nums[i + 1] = nums[i + 1], nums[i]
                    swapped = True


def val(nums):  # возвращает значения[cр. значение, мин, макс]
    summ = 0
    minn = 999
    maxx = -999
    for i in nums:
        summ += sqrt(i[0]**2 + i[1]**2)
        minn = min(sqrt(i[0]**2 + i[1]**2), minn)
        maxx = max(sqrt(i[0]**2 + i[1]**2), maxx)
    return [summ / len(nums), minn, maxx]


def get_sorted_array():
    # points - генерация точек в системе координат OxY points{1, 2, 3, 4} => области на прямой
    points = []
    length = 10  # кол-во точек

    for i in range(length):
        points.append([])
    from random import randint
    for i in range(length):
        points[i].append(randint(-100, 100))
        points[i].append(randint(-100, 100))

    PO = [[], [], [], []]  # разделим на 4 части нашу область
    p = [0, 0, 0, 0]
    for i in range(length):  # первая сортировка по областям
        x = points[i][0]  # наш x
        y = points[i][1]  # наш y
        coordinates_part = ((x < 0) + (y < 0) + 2*(x >= 0)*(y < 0)) # в какой области находится наша очередная точка
        PO[coordinates_part].append([])
        PO[coordinates_part][p[coordinates_part]].append(x)
        PO[coordinates_part][p[coordinates_part]].append(y)
        p[coordinates_part] += 1
    for i in PO:
        if(i != PO[2] and i != []):
            bubble_sort(i)
    if(len(PO[2]) > 1):
        print(PO[2])
        inverted_bubble_sort(PO[2])

    output_points = PO[0] + PO[1] + PO[2] + PO[3]
    return output_points


# задание 2
# 1 вариант решения через регулярку
def regular_solution(find_for_auto_sign):
    result = []
    regular_pattern = r'^[ABKMTXOАВЕКМНОРСТУХ]\d{3}[ABKMTXOАВЕКМНОРСТУХ]{2}\d{2,3}'
    for i in find_for_auto_sign:
        result += re.findall(regular_pattern, i)
    return result


# 2 вариант решения простой анализатор
def get_of_valid_sign(input_array):
    output_array = []
    pattern = "ABKMTXOАВЕКМНОРСТУХ"
    for input_sign in input_array:
        if (len(input_sign) == 8):
            pattern_matching = input_sign[0] in pattern and input_sign[
                1].isdigit() and input_sign[2].isdigit() and input_sign[
                    3].isdigit() and input_sign[4] in pattern and input_sign[
                        5] in pattern and input_sign[6].isdigit(
            ) and input_sign[7].isdigit()
            if pattern_matching:
                output_array.append(input_sign)
        elif (len(input_sign) == 9):
            pattern_matching = input_sign[0] in pattern and input_sign[
                1].isdigit() and input_sign[2].isdigit(
            ) and input_sign[3].isdigit(
            ) and input_sign[4] in pattern and input_sign[
                    5] in pattern and input_sign[6].isdigit(
            ) and input_sign[7].isdigit() and input_sign[8].isdigit()
            if pattern_matching:
                output_array.append(input_sign)
    return output_array


def main():
    # задание 1
    output = get_sorted_array()
    print(output)
    task = val(output)
    print("задание 1", end="\n")
    print("среднее значение до точек: ", round(task[0], 3))
    print("макс значение до точек: ", round(task[2], 3))
    print("минимальное значение до точек: ", round(task[1], 3))
    print("задание 2", end="\n")
    # задание 2
    find_for_auto_sign = [
        "AASCB123KK12", "BB1234B1", "А123АА11", "А222АА123", "A12AA123",
        "A123CC1234", "AA123A12", "АА12322"
    ]
    # решение 1
    print("регулярное выражение: ",
          regular_solution(find_for_auto_sign),
          end="\n")
    # решение 2
    print("проброс через булево условие: ",
          get_of_valid_sign(find_for_auto_sign))


if __name__ == "__main__":
    main()
