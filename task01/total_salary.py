import os

def data_salary(o):
    return (o['total'], ((o['total'] // o['length']) if o['length'] > 0 else o['total']))

def total_salary(file_path):
    data = { 'total': 0, 'length': 0 }

    if not os.path.exists(file_path):
        print(f"{file_path} такого файлу не існує")
        return data_salary(data)

    if os.path.isdir(file_path):
        print(f"{file_path} є директорією")
        return data_salary(data)

    with open(file_path, 'r', encoding='utf-8') as fi:
        for line in fi:
            _, salary = line.strip().split(',')
            try:
                data['total'] = data['total'] + int(salary)
                data['length'] = data['length'] + 1
            except:
                print(f"Рядок {data['length'] + 1} має проблеми зі значенням суми, ігноруємо ці дані")

    return data_salary(data)

def main():
    file_path = input(f"Введіть шлях до файлу: ")
    total, average = total_salary(file_path)
    print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")

if __name__ == "__main__":
    main()
