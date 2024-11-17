def find_min_substring_length_simple(s, c):
    # Проверки
    if not (1 <= len(s) <= 100):
        return 0
        # raise ValueError("Длина строки s должна быть от 1 до 100 символов.")
    if not (1 <= len(c) <= 26):
        return 0
        # raise ValueError("Длина строки c должна быть от 1 до 26 символов.")
    if not s.islower() or not c.islower():
        return 0
        # raise ValueError("Все символы в строках s и c должны быть строчными английскими буквами.")
    if len(set(c)) != len(c):
        return 0
        # raise ValueError("Все символы в строке c должны быть уникальными.")
    if not set(c).issubset(set(s)):
        return 0  # Если хотя бы один символ из c отсутствует в s, подстрока невозможна.

    # Основная логика
    c_set = set(c)
    min_length = float('inf')  # Для хранения минимальной длины

    # Перебираем все возможные подстроки
    for i in range(len(s)):
        for j in range(i, len(s)):
            # Подстрока от i до j
            substring = s[i:j+1]
            # Проверяем, содержит ли подстрока все символы из C
            if c_set.issubset(set(substring)):
                # Если содержит, обновляем минимальную длину
                min_length = min(min_length, j - i + 1)

    # Если не нашли подходящей подстроки, возвращаем 0
    return min_length if min_length != float('inf') else 0

# Ввод
# s = input()
# c = input()

# try:
#     # Вывод
#     print(find_min_substring_length_simple(s, c))
# except ValueError as e:
#     print(f"Ошибка ввода: {e}")



def run_tests():
    test_cases = [
        ("a", "a", 1),
        ("a", "b", 0),
        ("abcdefghij"*10, "fj", 5),
        ("abc", "d", 0),
        ("abc", "abcd", 0),
        ("aaabbbccc", "abc", 3),
        ("aaabbbccc", "aab", 2),
        ("abcdef", "f", 1),
        ("abcdef", "abc", 3),
        ("a...b...c", "abc", 9),
        ("a", "a", 1),
        ("aaaaa", "a", 1),
        ("abcdefghijklmnopqrstuvwxyz", "xyz", 3),
        ("abcdefghijklmnopqrstuvwxyz", "yxz", 3),
    ]

    for idx, (s, c, expected) in enumerate(test_cases, 1):
        result = find_min_substring_length_simple(s, c)
        if result == expected:
            print(f"Test {idx}: Passed")
        else:
            print(f"Test {idx}: Failed (s={s}, c={c}, expected={expected}, got={result})")

# Запуск тестов
run_tests()
