base_rate = 15
backpack_size = 8

stuffdict = {
    "rifle": ("r", 3, 25),
    "pistol": ("p", 2, 15),
    "ammo": ("a", 2, 15),
    "medkit": ("m", 2, 20),
    "inhaler": ("i", 1, 5),
    "knife": ("k", 1, 15),
    "axe": ("x", 3, 20),
    "talisman": ("t", 1, 25),
    "flask": ("f", 1, 15),
    "antidot": ("d", 1, 10),
    "supplies": ("s", 2, 20),
    "crossbow": ("c", 2, 20),
}


def get_symbol_size_points(stuffdict):
    symbol = [stuffdict[item][0] for item in stuffdict]
    size = [stuffdict[item][1] for item in stuffdict]
    points = [stuffdict[item][2] for item in stuffdict]
    return symbol, size, points


def get_memtable(stuffdict, capacity=backpack_size):
    symbol, size, points = get_symbol_size_points(stuffdict)
    n = len(points)

    total_all_points = sum(points)
    adjusted_points = [2 * points[i] for i in range(n)]

    V = [[0 for a in range(capacity + 1)] for i in range(n + 1)]

    for i in range(n + 1):
        for a in range(capacity + 1):
            if i == 0 or a == 0:
                V[i][a] = 0
            elif size[i - 1] <= a:
                V[i][a] = max(
                    adjusted_points[i - 1] + V[i - 1][a - size[i - 1]], V[i - 1][a]
                )
            else:
                V[i][a] = V[i - 1][a]
    return V, symbol, size, points, total_all_points


def get_selected_items_list(stuffdict, capacity=backpack_size):
    V, symbol, size, points, total_all_points = get_memtable(stuffdict, capacity)
    n = len(points)
    res = V[n][capacity]
    a = capacity
    items_list = []

    for i in range(n, 0, -1):
        if res <= 0:
            break
        if res == V[i - 1][a]:
            continue
        else:
            item_key = list(stuffdict.keys())[i - 1]
            items_list.append(item_key)
            res -= 2 * points[i - 1]
            a -= size[i - 1]

    return items_list, total_all_points


def create_backpack_layout(selected_items, stuffdict):
    backpack = []
    current_row = []
    current_space = 0

    for item in selected_items:
        symbol = stuffdict[item][0]
        item_size = stuffdict[item][1]
        for _ in range(item_size):
            if current_space >= 4:
                backpack.append(current_row)
                current_row = []
                current_space = 0
            current_row.append(symbol)
            current_space += 1

    if current_row:
        while len(current_row) < 4:
            current_row.append(" ")
        backpack.append(current_row)

    return backpack


def find_all_combinations(stuffdict, capacity):
    items = list(stuffdict.keys())
    n = len(items)
    
    dp = [[] for _ in range(capacity + 1)]
    
    for i in range(n):
        item = items[i]
        item_size = stuffdict[item][1]
        
        for a in range(capacity, item_size - 1, -1):
            for combo in dp[a - item_size]:
                new_combo = combo + [item]
                if sum(stuffdict[item][1] for item in new_combo) <= capacity:
                    if new_combo not in dp[a]:
                        dp[a].append(new_combo)
    
    all_combinations = []
    for a in range(capacity + 1):
        all_combinations.extend(dp[a])
    
    return all_combinations


def solve_tom_problem(capacity=8, find_all_combinations_b=False):
    
    if find_all_combinations_b:
        total_all_points = sum(stuffdict[item][2] for item in stuffdict)
        positive_combinations = []

        # Используем динамическое программирование вместо рекурсии
        all_combinations = find_all_combinations(stuffdict, capacity)
        
        for combo in all_combinations:
            total_size = sum(stuffdict[item][1] for item in combo)
            points_selected = sum(stuffdict[item][2] for item in combo)
            final_score = (
                base_rate + points_selected - (total_all_points - points_selected)
            )

            if final_score > 0:
                backpack = create_backpack_layout(combo, stuffdict)
                positive_combinations.append((combo, final_score, total_size, backpack))

        positive_combinations.sort(key=lambda x: x[1], reverse=True)

        print(f"Найдено комбинаций: {len(positive_combinations)}\n")

        for i, (combo, score, size, backpack) in enumerate(positive_combinations, 1):
            print(f"{i}. Очки: {score}, Ячейки: {size}/{capacity}")
            print("   Расположение:")
            for row in backpack:
                print("   [" + "],[".join(row) + "]")
            print()

        return positive_combinations
    
    else:
        selected_items, total_all_points = get_selected_items_list(stuffdict, capacity)

        backpack_layout = create_backpack_layout(selected_items, stuffdict)

        total_points = base_rate
        total_size = 0

        points_from_selected = 0
        for item in selected_items:
            points_from_selected += stuffdict[item][2]
            total_size += stuffdict[item][1]

        points_from_not_selected = total_all_points - points_from_selected
        total_points = base_rate + points_from_selected - points_from_not_selected

        print(f"\nПараметры:")
        print(f"- Размер рюкзака: {capacity} ячеек")
        print(f"- Стартовые очки: {base_rate}")

        print(f"\nРасположение в рюкзаке:")
        for row in backpack_layout:
            print("[" + "],[".join(row) + "]")

        print(f"\nИтоговые очки выживания: {total_points}")
        
        if total_points <= 0:
            print(f"\nНет комбинаций с положительным счётом => нет решений")

        return selected_items, backpack_layout, total_points


if __name__ == "__main__":
    print(f"\nЛучшее решение для 8 ячеек")
    solve_tom_problem(capacity=8, find_all_combinations_b=False)

    print(f"\nРешение для 7 ячеек")
    solve_tom_problem(capacity=7, find_all_combinations_b=False)
    
    print(f"\nВсе комбинации для 8 ячеек")
    solve_tom_problem(capacity=8, find_all_combinations_b=True)