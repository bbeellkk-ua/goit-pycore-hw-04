from os.path import exists, isdir
from pathlib import Path
from colorama import Fore, Style

def path_tree(path, level = 0, prefix = ''):
    pt = path

    p = Path(path)

    if prefix:
        pt = path.removeprefix(prefix + '/')

    if level:
        color = Fore.BLUE if p.is_dir() else Fore.LIGHTGREEN_EX
        print(f"{' '*(level - 1)*4}{color}{pt}{Style.RESET_ALL}")

    if p.is_dir():
        for i in p.iterdir():
            path_tree(path + '/' + i.name, level + 1, path)

def dir(dir_path):
    d = Path(dir_path)
    if not d.exists() or not d.is_dir():
        print(f"Не правильний шлях до директорії")
        return
    path_tree(dir_path)

def main():
    dir_path = input(f"Введіть шлях до директорії: ")
    dir(dir_path)

if __name__ == "__main__":
    main()
