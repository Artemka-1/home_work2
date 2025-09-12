def get_cats_info(path):
    try:
        with open(path, "r", encoding="cp1251") as cats:
            info = []
            for line in cats:
                parts = line.strip().split(",")
                cat = {"id": parts[0], "name": parts[1], "age": parts[2]}
                info.append(cat)
        return info
    except FileNotFoundError:
        print("Файл не найден.")
        return []
    

cats_info = get_cats_info("C:/Users/PC/Desktop/моё/домашечка 2.txt")
print(cats_info)