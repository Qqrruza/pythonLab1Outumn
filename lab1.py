# лаба 1
# 1) флаг франции
# 2) сделать узор шахматный
# 3) сгененрить график функции пораболы
# 4) вывести диаграмму процентного соотношения количества чисел больше и меньше нуля
#
# доп. задание: реализовать анимацию из 2-3 кадров


def paint_france(hight, width_column):
    blue = f"\u001b[44m \u001b[0m"
    white = f"\u001b[47m \u001b[0m"
    red = f"\u001b[41m \u001b[0m"
    for line in range(hight):
        print(blue * width_column + white * width_column + red * width_column, sep="")


def print_chess(square_size):
    black = f"\u001b[40m \u001b[0m"
    white = f"\u001b[47m \u001b[0m"
    for line1 in range(square_size // 2):
        print(black * square_size + white * square_size + black * square_size)
    for line2 in range(square_size // 2):
        print(white * square_size + black * square_size + white * square_size)
    for line3 in range(square_size // 2):
        print(black * square_size + white * square_size + black * square_size)


def print_function_graph():

    size = 15
    graph = [[" " for _ in range(size)] for _ in range(size)]

    for x in range(size):
        y = int(x**2 / 4)
        if y < size:
            graph[size - 1 - y][x] = "*"

    for i in range(size):
        graph[size - 1][i] = "-"
        graph[i][0] = "|"

    graph[size - 1][0] = "+"

    for row in graph:
        print("".join(row))


if __name__ == "__main__":
    paint_france(7, 20)
    print("\n\n")
    print_chess(11)
    print_function_graph()
