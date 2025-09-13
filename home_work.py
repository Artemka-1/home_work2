def total_salary(path):
    total = 0
    count = 0
    try:
        with open(path, "r", encoding="utf-8") as f:
            for line in f:
                parts = line.strip().split(",")
                if len(parts) == 2:
                    try:
                        salary = float(parts[1])
                        total += salary
                        count += 1
                    except ValueError:
                        pass
        if count == 0:
            return 0, 0
        average = total / count
        return total, average
    except FileNotFoundError:
        print("Файл не найден по указанному пути.")
        return 0, 0

path = r"C:\Users\PC\Desktop\my1\home_work.txt"

total, average = total_salary(path)
print(f"Сумма зарплат: {total}")
print(f"Средняя зарплата: {average}")
