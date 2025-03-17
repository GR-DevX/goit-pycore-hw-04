import subprocess
import sys
from pathlib import Path
from colorama import init, Fore, Style

VENV_DIR = Path("venv")

# Створення віртуального оточення
if not VENV_DIR.exists():
    subprocess.check_call([sys.executable, "-m", "venv", str(VENV_DIR)])
    print("Віртуальне оточення створене.")

# Визначення pip команд
if sys.platform == "win32":
    PIP_CMD = VENV_DIR / "Scripts" / "pip"
else:
    PIP_CMD = VENV_DIR / "bin" / "pip"

# Установка colorama
try:
    subprocess.check_call([str(PIP_CMD), "install", "colorama"])
    print("Бібліотека 'colorama' встановлена.")
except subprocess.CalledProcessError as e:
    print(f"Помилка при встановленні colorama: {e}")
    sys.exit(1)

# Імпорт colorama після установки
from colorama import init, Fore, Style

# Обробка аргументів командного рядка
init(autoreset=True)
print(f"{Fore.GREEN}Colorama активована і готова до використання!")

def get_directory_path():
    if len(sys.argv) != 2:
        print(f"{Fore.RED}Помилка: Потрібно передати шлях до директорії як аргумент.")
        sys.exit(1)
    
    directory = Path(sys.argv[1])
    
    if not directory.exists():
        print(f"{Fore.RED}Помилка: Шлях не існує.")
        sys.exit(1)
    
    if not directory.is_dir():
        print(f"{Fore.RED}Помилка: Вказаний шлях не є директорією.")
        sys.exit(1)
    
    return directory

# Рекурсивний обхід директорії
def print_directory_structure(directory: Path, indent: str = ""):
    for item in directory.iterdir():
        if item.is_dir():
            print(f"{indent}{Fore.BLUE}{item.name}/")
            print_directory_structure(item, indent + "    ")  # Рекурсивний виклик для піддиректорій
        else:
            print(f"{indent}{Fore.GREEN}{item.name}")

# Основний блок виконання скрипта
def main():
    directory = get_directory_path()
    print(f"{Fore.YELLOW}Структура директорії: {directory}")
    print_directory_structure(directory)

if __name__ == "__main__":
    main()
