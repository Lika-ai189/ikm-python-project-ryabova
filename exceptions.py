"""
Модуль exceptions.py - модуль с собственными классами ошибок (исключений) для программы.
"""

class RingError(Exception):
    """Базовое исключение для всех ошибок модуля числового кольца."""
    pass

class EmptyInputError(RingError):
    """Исключение при пустом вводе."""
    pass

class RingValidationError(RingError):
    """Исключение при некорректных входных данных (не цифры)."""
    pass

class TooShortRingError(RingError):
    """Исключение при кольце меньше 3 цифр."""
    pass

class FileProcessingError(RingError):
    """Исключение при ошибках чтения или записи файлов."""
    pass

class TooLongRingError(RingError):
    """Исключение при кольце более, чем 1000 цифр."""
    pass