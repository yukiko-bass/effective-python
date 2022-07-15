from collections import defaultdict


def increment_with_report(current, increments):
    added_count = 0

    def missing():
        nonlocal added_count  # ステートフルクロージャ
        added_count += 1
        return 0

    result = defaultdict(missing, current)
    for key, amount in increments:
        result[key] += amount

    return result, added_count


current = {"green": 12, "blue": 3}
increments = [
    ("red", 5),
    ("blue", 17),
    ("orange", 9),
]
result, count = increment_with_report(current, increments)
print(result)
print(count)
assert count == 2
