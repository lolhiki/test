import time
import random

class LoopsPractice:
    """
    Класс для практики работы с циклами в Python.
    """

    @staticmethod
    def task_1_numbers():
        """
        Задание 1
        """
        numbers = list(range(1, 8))
        for n in numbers:
            print(n)
            if n == 5:
                break

    @staticmethod
    def task_2_strings():
        """
        Задание 2 
        """
        words = [f"str{i}" for i in range(10)]
        for word in words:
            print(word)

    @staticmethod
    def task_3_wing_load():
        """
        Задание 3
        """
        i = 0
        while i < 10:
            load = random.randint(0, 100)
            if load > 85:
                print(f"Крылышки в опасности! Нагрузка — {load}%")
            time.sleep(0.2)
            i += 1


# Демонстрация работы всех задач
if __name__ == "__main__":
    print("=== Задача 1: Список чисел с прерыванием ===")
    LoopsPractice.task_1_numbers()
    
    print("\n=== Задача 2: Список строк ===")
    LoopsPractice.task_2_strings()
    
    print("\n=== Задача 3: Мониторинг нагрузки на крылышки ===")
    LoopsPractice.task_3_wing_load()
