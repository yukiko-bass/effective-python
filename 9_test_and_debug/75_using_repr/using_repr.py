print("foo bar")

print("-----")

# 以下、上記とすべて同じ
my_value = "foo bar"
print(str(my_value))
print("%s" % my_value)
print(f"{my_value}")
print(format(my_value))
print(my_value.__format__("s"))
print(my_value.__str__())

print("-----")

# 以下は同じに見えるので人間には区別がつかない
print(5)
print("5")

int_value = 5
str_value = "5"
print(f"{int_value} == {str_value} ?")

print("-----")

# repr を使ってより正式で理解可能な文字列表現を出力する
a = "\x07"
print(repr(a))

print("-----")

b = eval(repr(a))
assert a == b

print("-----")

print(repr(5))
print(repr("5"))

print("-----")

# repr を使った場合と同じ書き方（"%r" % ）
print("%r" % 5)
print("%r" % "5")

int_value = 5
str_value = "5"
# repr を使った場合と同じ書き方（!r）
print(f"{int_value!r} != {str_value!r} ?")

print("-----")


class OpaqueClass:
    def __init__(self, x, y):
        self.x = x
        self.y = y


obj = OpaqueClass(1, "foo")
print(obj)  # あんまり役に立たない

print("-----")


class BetterClass:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self) -> str:
        return f"BetterClass({self.x!r}, {self.y!r})"


obj = BetterClass(1, "foo")
print(obj)  # 今度は役に立つ

print("-----")
# クラスを修正できないとき

obj = OpaqueClass(4, "baz")
print(obj.__dict__)
