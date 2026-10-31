"""
Вариант 3  Страниц за день
Функция: pages_per_day(pages, days). Число страниц разделите на число дней. Пример: pages_per_day(84, 7) → 12.0.
Слова для сортировки: ["том", "книга", "энциклопедия"]
"""


def pages_per_day(pages, days):
    if days == 0:
        return "На ноль делить нельзя"
    return pages / days

assert pages_per_day(84, 7) == 12.0
assert pages_per_day(34, 0) == "На ноль делить нельзя"
assert pages_per_day(128, 16) == 8.0

words = ["том", "книга", "энциклопедия"]
sortedwords = sorted(words, key=lambda word: len(word))
print(sortedwords)