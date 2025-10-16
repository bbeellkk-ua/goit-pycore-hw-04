import os

def get_cats_info(file_path):
    cats = []

    if not os.path.exists(file_path):
        print(f"{file_path} такого файлу не існує")
        return cats

    if os.path.isdir(file_path):
        print(f"{file_path} є директорією")
        return cats

    with open(file_path, 'r', encoding='utf-8') as fi:
        for line in fi:
            uuid, name, age = line.strip().split(',')
            cats.append({'id': uuid, 'name': name, 'age': age})

    return cats

def main():
    file_path = input(f"Введіть шлях до файлу: ")
    cats = get_cats_info(file_path)
    print(cats)

if __name__ == "__main__":
    main()
