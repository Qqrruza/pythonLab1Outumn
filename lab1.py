# лаба 1
# 1) флаг франции
# 2) сделать узор шахматный
# 3) сгененрить график функции пораболы
# 4) вывести диаграмму процентного соотношения количества чисел больше и меньше нуля
#
# доп. задание: реализовать анимацию из 2-3 кадров
import os
import time

def clear_console():
    """Очистка консоли"""
    os.system('cls' if os.name == 'nt' else 'clear')

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

def analyze_sequence():
    file = open('C:\\Users\\Анна\\Desktop\\python project\\sequence.txt')
    
    numbers = []
    less_than_zero = 0
    greater_than_zero = 0
    
    for line in file:
        line = line.strip()
        if line != "":
            num = float(line)
            numbers.append(num)
            
            if num < 0:
                less_than_zero += 1
            elif num > 0:
                greater_than_zero += 1
    
    file.close()
    
    total = len(numbers)
    
    # Результаты
    print(f"\nВсего чисел: {total}")
    print(f"Меньше 0: {less_than_zero}")
    print(f"Больше 0: {greater_than_zero}")
    
    # Цветные блоки для диаграммы
    red = "\u001b[41m \u001b[0m"
    
    # Диаграмма
    print("\nДИАГРАММА:")
    print("Меньше 0: " + red * less_than_zero  + f" ({less_than_zero})")
    print("Больше 0: " + red * greater_than_zero + f" ({greater_than_zero})")

def rainbow_pixels():
    rainbow = [
        "\u001b[41m \u001b[0m",  # красный
        "\u001b[43m \u001b[0m",  # желтый
        "\u001b[42m \u001b[0m",  # зеленый
        "\u001b[46m \u001b[0m",  # голубой
        "\u001b[44m \u001b[0m",  # синий
        "\u001b[45m \u001b[0m"   # фиолетовый
        ]
    
    for frame in range(20):
        os.system("cls" if os.name == 'nt' else "clear")
        
        for i in range(6):
            line = ""
            for j in range(12):
                color_idx = (frame + i + j) % len(rainbow)
                line += rainbow[color_idx]
            print("   " + line)
        
        
        time.sleep(0.1)


if __name__ == "__main__":
    paint_france(7, 20)
    print("\n\n")
    print_chess(11)
    print_function_graph()
    analyze_sequence()
    time.sleep(10)
    rainbow_pixels()
    
