# лаба 1
# 1) флаг франции
# 2) сделать узор шахматный
# 3) сгененрить график функции пораболы
# 4) вывести диаграмму процентного соотношения количества чисел больше и меньше нуля
#
# доп. задание: реализовать анимацию из 2-3 кадров
import os
import math
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
    """Анализ последовательности чисел из файла sequence.txt"""
    print("\n=== АНАЛИЗ ПОСЛЕДОВАТЕЛЬНОСТИ ===")
    
    # Диагностика: покажем текущую рабочую директорию
    current_dir = os.getcwd()
    print(f"Текущая папка: {current_dir}")
    
    # Покажем файлы в текущей директории
    files = os.listdir('.')
    print(f"Файлы в папке: {[f for f in files if f.endswith('.txt') or f.endswith('.py')]}")
    
    # Попробуем несколько вариантов имени файла
    possible_filenames = ['sequence.txt', 'Sequence.txt', 'SEQUENCE.txt']
    file_found = None
    
    for filename in possible_filenames:
        if os.path.exists(filename):
            file_found = filename
            break
    
    if not file_found:
        print("❌ Файл sequence.txt не найден!")
        print("Пожалуйста, убедитесь в следующем:")
        print("1. Файл находится в той же папке, что и программа")
        print("2. Имя файла точно 'sequence.txt'")
        print("3. Файл не имеет скрытого расширения (например, 'sequence.txt.txt')")
        return
    
    print(f"✅ Найден файл: {file_found}")
    
    try:
        with open(file_found, 'r', encoding='utf-8') as file:
            numbers = []
            line_count = 0
            for line in file:
                line_count += 1
                line = line.strip()
                if line:
                    try:
                        numbers.append(float(line))
                    except ValueError:
                        print(f"⚠️  Предупреждение: некорректное значение в строке {line_count}: '{line}'")
            
        if not numbers:
            print("Файл sequence.txt пуст или не содержит корректных чисел")
            return
            
        print(f"✅ Успешно загружено {len(numbers)} чисел из {line_count} строк файла")
        
    except Exception as e:
        print(f"❌ Ошибка при чтении файла: {e}")
        return
    
    # Подсчет чисел
    less_than_zero = len([x for x in numbers if x < 0])
    greater_than_zero = len([x for x in numbers if x > 0])
    equal_to_zero = len([x for x in numbers if x == 0])
    total = len(numbers)
    
    print(f"\n📊 РЕЗУЛЬТАТЫ АНАЛИЗА:")
    print(f"Всего чисел: {total}")
    print(f"Меньше 0: {less_than_zero} ({less_than_zero/total*100:.1f}%)")
    print(f"Больше 0: {greater_than_zero} ({greater_than_zero/total*100:.1f}%)")
    print(f"Равно 0: {equal_to_zero} ({equal_to_zero/total*100:.1f}%)")
    
    # Диаграмма
    print("\n📈 ДИАГРАММА:")
    max_width = 40
    
    less_width = int((less_than_zero / total) * max_width)
    greater_width = int((greater_than_zero / total) * max_width)
    zero_width = int((equal_to_zero / total) * max_width)
    
    print("Меньше 0:  " + '█' * max(1, less_width) + f" ({less_than_zero})")
    print("Больше 0: " + '█' * max(1, greater_width) + f" ({greater_than_zero})")
    print("Равно 0:   " + '█' * max(1, zero_width) + f" ({equal_to_zero})")


if __name__ == "__main__":
    paint_france(7, 20)
    print("\n\n")
    print_chess(11)
    print_function_graph()
    analyze_sequence()
