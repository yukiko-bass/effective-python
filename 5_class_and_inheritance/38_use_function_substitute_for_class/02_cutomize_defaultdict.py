from collections import defaultdict


def log_missing():
    print("Key added")
    return 0


def increment_with_report(current, increments):
    added_count = 0

    def missing():
        nonlocal added_count
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
result = defaultdict(log_missing, current)
print("Before:", dict(result))
for key, amout in increments:
    result[key] += amout
print("After: ", dict(result))
