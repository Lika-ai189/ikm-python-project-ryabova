"""
Модуль interface.py - пользовательский консольный интерфейс с циклическим меню..
"""

from logic import RingLogic
from exceptions import (
    RingError,
    FileProcessingError,
    EmptyInputError,
    RingValidationError,
    TooShortRingError,
    TooLongRingError
)

# Группировка исключений валидации для компактной и чистой обработки
VALIDATION_ERRORS = (EmptyInputError, RingValidationError, TooShortRingError, TooLongRingError)


class UserInterface:
    def __init__(self, logic):
        self.logic = logic
        self.is_running = True

    def display_menu(self):
        print("\n" + "=" * 40)
        print(" ПРОГРАММА 'ЧИСЛОВОЕ КОЛЬЦО'")
        print("=" * 40)
        print("1. Решить задачу из файла")
        print("2. Решить задачу с ручным вводом")
        print("3. Выход")
        print("=" * 40)

    def get_valid_choice(self):
        while True:
            choice = input("Выберите пункт (1-3): ").strip()
            if choice in ['1', '2', '3']:
                return choice
            print("Ошибка: введите 1, 2 или 3.")

    def handle_file_mode(self):
        while True:
            inp = input("Входной файл (например, input.txt): ").strip()
            if not inp:
                print("Имя входного файла не может быть пустым.\n")
                continue

            try:
                with open(inp, 'r', encoding='utf-8') as f:
                    pass
            except FileNotFoundError:
                print(f"Ошибка: Файл '{inp}' не найден. Проверьте имя и расширение.\n")
                continue
            except PermissionError:
                print(f"Ошибка: Нет доступа к чтению файла '{inp}'.\n")
                continue
            except Exception as e:
                print(f"Ошибка чтения файла: {e}\n")
                continue

            while True:
                out = input("Выходной файл (например, output.txt): ").strip()
                if not out:
                    print("Имя выходного файла не может быть пустым.\n")
                    continue

                try:
                    result = self.logic.solve_from_file(inp, out)
                    print(f"\nРешение {'найдено' if result != 'No' else 'не найдено'}.")
                    print(f"Результат: {result}")
                    print(f"Результат успешно записан в файл '{out}'")
                    return

                except VALIDATION_ERRORS as e:
                    print(f"\nОшибка в содержимом файла '{inp}': {e}")
                    print("Пожалуйста, выберите другой входной файл.\n")
                    break
                except PermissionError:
                    print(f"Ошибка: Нет доступа для записи в '{out}'. Попробуйте указать другое имя.\n")
                except FileProcessingError as e:
                    print(f"Ошибка записи в файл: {e}. Попробуйте указать другое имя.\n")
                except Exception as e:
                    print(f"\nСистемная ошибка: {e}")
                    return

    def handle_manual_mode(self):
        while True:
            data = input("Строка цифр кольца: ").strip()
            try:
                result = self.logic.solve_from_string(data)
                print(f"\nРешение {'найдено' if result != 'No' else 'не найдено'}.")
                print(f"Результат: {result}")
                break
            except VALIDATION_ERRORS as e:
                print(f"\nОшибка: {e}")
                print("Попробуйте ввести снова.\n")
            except RingError as e:
                print(f"\nОшибка: {e}")
                break
            except Exception as e:
                print(f"\nСистемная ошибка: {e}")
                break

    def run(self):
        print("Добро пожаловать!")
        while self.is_running:
            self.display_menu()
            choice = self.get_valid_choice()
            if choice == '1':
                self.handle_file_mode()
            elif choice == '2':
                self.handle_manual_mode()
            elif choice == '3':
                self.is_running = False

            if self.is_running:
                input("\nНажмите Enter для продолжения...")