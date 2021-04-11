def bubble_sort(nums):
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(nums[1]) - 1):
            if abs(nums[1][i][0]) > abs(nums[1][i + 1][0]):
                nums[1][i], nums[1][i + 1] = nums[1][i + 1], nums[1][i]
                swapped = True
            elif abs((nums[1][i][0])) == abs(nums[1][i + 1][0]):
                if abs(nums[1][i][1]) > abs(nums[1][i + 1][1]):
                    nums[1][i], nums[1][i + 1] = nums[1][i + 1], nums[1][i]
                    swapped = True


def inverted_bubble_sort(nums):  # сортировка для области где x, y < 0
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(nums[1]) - 1):
            if abs(nums[1][i][0]) < abs(nums[1][i + 1][0]):
                nums[1][i], nums[1][i + 1] = nums[1][i + 1], nums[1][i]
                swapped = True
            elif abs((nums[1][i][0])) == abs(nums[1][i + 1][0]):
                if abs(nums[1][i][1]) > abs(nums[1][i + 1][1]):
                    nums[1][i], nums[1][i + 1] = nums[1][i + 1], nums[1][i]
                    swapped = True


from math import sqrt


def sr_val(nums):
    summ = 0
    minn = 999
    maxx = -999
    for i in nums:
        summ += sqrt(i[0]**2 + i[1]**2)
        minn = min(sqrt(i[0]**2 + i[1]**2), minn)
        maxx = max(sqrt(i[0]**2 + i[1]**2), maxx)
    return [summ / len(nums), minn, maxx]


from array import array


def get_sorted_array():
    # points - генерация точек в системе координат OxY points{1, 2, 3, 4} => области на прямой
    points = ("i", [])
    points1 = ("i", [])
    points2 = ("i", [])
    points3 = ("i", [])
    points4 = ("i", [])
    length = 5  # кол-во точек

    for i in range(length):
        points[1].append([])
    from random import randint
    for i in range(length):
        points[1][i].append(randint(-100, 100))
        points[1][i].append(randint(-100, 100))

    p1 = p2 = p3 = p4 = 0
    for i in range(length):  # первая сортировка по областям
        if (points[1][i][0] >= 0 and points[1][i][1] >= 0):
            points1[1].append([])
            points1[1][p1].append(points[1][i][0])
            points1[1][p1].append(points[1][i][1])
            p1 += 1
        if (points[1][i][0] < 0 and points[1][i][1] >= 0):
            points2[1].append([])
            points2[1][p2].append(points[1][i][0])
            points2[1][p2].append(points[1][i][1])
            p2 += 1
        if (points[1][i][0] < 0 and points[1][i][1] <= 0):
            points3[1].append([])
            points3[1][p3].append(points[1][i][0])
            points3[1][p3].append(points[1][i][1])
            p3 += 1
        if (points[1][i][0] >= 0 and points[1][i][1] <= 0):
            points4[1].append([])
            points4[1][p4].append(points[1][i][0])
            points4[1][p4].append(points[1][i][1])
            p4 += 1
        bubble_sort(points1)
        bubble_sort(points2)
        inverted_bubble_sort(points3)
        bubble_sort(points4)
        output_points = points1[1] + points2[1] + points3[1] + points4[1]
    return output_points


# задание 2
# 1 вариант решения через регулярку
import re


def regular_solution(find_for_auto_sign):
    result = []
    for i in find_for_auto_sign:
        result += re.findall(
            r'^[ABKMTXOАВЕКМНОРСТУХ]\d{3}[ABKMTXOАВЕКМНОРСТУХ]{2}\d{2,3}', i)
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
    task = sr_val(output)
    print("задание 1", end="\n")
    print("среднее значение до точек: ", round(task[0], 3))
    print("макс значение до точек: ", round(task[2], 3))
    print("минимальное значение до точек: ", round(task[1], 3))
    print("задание 2", end="\n")
    #задание 2
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