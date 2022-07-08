import datetime


def get_animals(database, species):
    name = ""
    last_mealtime = datetime.datetime.now()
    return ((name, last_mealtime),)


def get_food_period(database, species):
    # データベースクエリ
    # ・・・・
    # 時間の差分を返す
    return datetime.timedelta(hours=1)


def feed_animal(database, name, when):
    # データベースに書き出し
    pass


# これだとdaetme.utcnow をモック化できないのでリファクタリングする
def do_rounds(database, species):
    now = datetime.datetime.now()
    feeding_timedelta = get_food_period(database, species)
    animals = get_animals(database, species)
    fed = 0

    for name, last_mealtime in animals:
        if (now - last_mealtime) > feeding_timedelta:
            feed_animal(database, name, now)
            fed += 1

    return fed


# 解決策1：すべてをキーワード専用引数で与える
def do_rounds2(
    database,
    species,
    *,
    now_func=datetime.datetime.now,
    food_func=get_food_period,
    animals_func=get_animals,
    feed_func=feed_animal
):
    now = now_func()
    feeding_timedelta = food_func(database, species)
    animals = animals_func(database, species)
    fed = 0

    for name, last_mealtime in animals:
        if (now - last_mealtime) > feeding_timedelta:
            feed_animal(database, name, now)
            fed += 1

    return fed


# モックにするために外に出す
def get_do_rounds_time():
    return datetime.datetime.utcnow()


def do_rounds3(database, species):
    now = get_do_rounds_time()
    return now


# datetime.utcnow　mock にキーワード専用引数を使う
def do_rounds4(database, species, *, now=datetime.datetime.now):
    now = now()
    feeding_timedelta = get_food_period(database, species)
    animals = get_animals(database, species)
    fed = 0

    for name, last_mealtime in animals:
        if (now - last_mealtime) > feeding_timedelta:
            feed_animal(database, name, now)
            fed += 1

    return fed
