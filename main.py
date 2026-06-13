"""
Модуль main.py - точка входа в приложение. Инициализация и запуск..
"""
from logic import RingLogic
from interface import UserInterface

def main():
    logic = RingLogic()
    app = UserInterface(logic)
    app.run()

if __name__ == "__main__":
    main()