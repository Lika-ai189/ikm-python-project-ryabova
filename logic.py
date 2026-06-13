"""
Модуль logic.py - логика: валидация, работа с файлами и запуск алгоритма.
"""

from ring import NumericRing
from exceptions import (
    EmptyInputError,
    RingValidationError,
    TooShortRingError,
    TooLongRingError,
    FileProcessingError
)

class RingLogic:
    """Класс, который отвечает за валидацию данных, чтение/запись
    файлов и запуск алгоритма поиска решения.
    """

    def read_file(self, input_path):
        try:
            with open(input_path, 'r', encoding='utf-8') as file:
                return file.readline().strip()
        except FileNotFoundError:
            raise FileProcessingError(f"Файл '{input_path}' не найден.")
        except PermissionError:
            raise FileProcessingError(f"Нет доступа к файлу '{input_path}'.")
        except Exception as error:
            raise FileProcessingError(f"Ошибка чтения: {error}")

    def validate_data(self, data):
        if not data:
            raise EmptyInputError("Ввод не может быть пустым.")
        if not data.isdigit():
            raise RingValidationError("Ввод должен содержать только цифры.")
        if len(data) < 3:
            raise TooShortRingError("Кольцо должно содержать минимум 3 цифры.")
        if len(data) > 1000:
            raise TooLongRingError("Кольцо не должно содержать более 1000 цифр.")

    def write_file(self, output_path, result):
        try:
            with open(output_path, 'w', encoding='utf-8') as file:
                file.write(result + '\n')
        except PermissionError:
            raise FileProcessingError(f"Нет доступа для записи в '{output_path}'.")
        except Exception as error:
            raise FileProcessingError(f"Ошибка записи: {error}")

    def solve_from_file(self, input_path, output_path):
        data = self.read_file(input_path)

        # Валидация по правилам задачи
        self.validate_data(data)

        # Инициализация структуры и запуск алгоритма
        ring = NumericRing(data)
        result = ring.find_solution()

        self.write_file(output_path, result)

        return result

    def solve_from_string(self, data):
        """Обработка ручного ввода: валидация и запуск алгоритма."""
        clean_data = data.strip()
        self.validate_data(clean_data)

        ring = NumericRing(clean_data)
        return ring.find_solution()