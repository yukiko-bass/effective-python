from collections import defaultdict


class BetterCountMissing:
    def __init__(self):
        self.added = 0

    # 特殊メソッド
    def __call__(self):
        self.added += 1
        return 0


counter = BetterCountMissing()
assert counter() == 0
assert callable(counter)

current = {"green": 12, "blue": 3}
increments = [
    ("red", 5),
    ("blue", 17),
    ("orange", 9),
]

counter = BetterCountMissing()
result = defaultdict(counter, current)  # __call__ を信頼する
for key, amount in increments:
    result[key] += amount

assert counter.added == 2
