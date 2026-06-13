"""
Модуль ring.py
Реализация динамической структуры данных: циклического двусвязного списка.
"""

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class NumericRing:
    """Числовое кольцо на основе циклического двусвязного списка."""

    def __init__(self, digits_str=""):
        self.head = None
        self.size = 0
        if digits_str:
            self.build_from_string(digits_str)

    def build_from_string(self, digits_str):
        for char in digits_str:
            self.add_digit(char)

    def add_digit(self, char):
        new_node = Node(char)
        if not self.head:
            self.head = new_node
            new_node.next = new_node.prev = new_node
        else:
            # Перенастройка 4 ссылок для вставки узла в конец циклического списка
            tail = self.head.prev
            tail.next = new_node
            new_node.prev = tail
            new_node.next = self.head
            self.head.prev = new_node
        self.size += 1

    def to_string(self):
        if not self.head:
            return ""
        result = []
        curr = self.head
        for _ in range(self.size):
            result.append(curr.value)
            curr = curr.next
        return "".join(result)

    def find_solution(self):
        """Поиск тождества A+B=C.
        Алгоритм: строка 'вращается' (разрывается в точке i), превращая кольцо в линейную
        строку. Границы циклов гарантируют, что длины A, B и C будут >= 1.
        """
        if self.size < 3:
            return "No"

        base_string = self.to_string()

        for i in range(self.size):
            current_str = base_string[i:] + base_string[:i]

            for len_a in range(1, self.size - 1):
                for len_b in range(1, self.size - len_a):
                    a = current_str[:len_a]
                    b = current_str[len_a: len_a + len_b]
                    c = current_str[len_a + len_b:]

                    # Числа длиннее 1 цифры не могут начинаться с '0'
                    if (len(a) > 1 and a[0] == '0') or \
                            (len(b) > 1 and b[0] == '0') or \
                            (len(c) > 1 and c[0] == '0'):
                        continue

                    if int(a) + int(b) == int(c):
                        return f"{a}+{b}={c}"

        return "No"