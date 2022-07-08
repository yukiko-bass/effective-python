from datetime import datetime, timedelta
from unittest import TestCase
from unittest.mock import DEFAULT, Mock, call, patch

from animal import (
    do_rounds2,
    do_rounds4,
    feed_animal,
    get_animals,
    get_do_rounds_time,
    get_food_period,
)


class TestAnimal(TestCase):
    def test_do_rounds2(self):
        now_func = Mock(spec=datetime.now)
        now_func.return_value = datetime(2022, 7, 8, 15, 45)

        food_func = Mock(spec=get_food_period)
        food_func.return_value = timedelta(hours=3)

        animals_func = Mock(spec=get_animals)
        animals_func.return_value = [
            ("Spot", datetime(2022, 7, 8, 11, 15)),
            ("Fluffy", datetime(2022, 7, 8, 12, 30)),
            ("Jojo", datetime(2022, 7, 8, 12, 45)),
        ]

        feed_func = Mock(spec=feed_animal)

        database = Mock()

        result = do_rounds2(
            database,
            "Meerkat",
            now_func=now_func,
            food_func=food_func,
            animals_func=animals_func,
            feed_func=feed_func,
        )

        assert result == 2

        # 呼び出しの検証
        food_func.assert_called_once_with(database, "Meerkat")
        animals_func.assert_called_once_with(database, "Meerkat")

        feed_func.assert_has_calls(
            [
                call(database, "Spot", now_func.return_value),
                call(database, "Fluffy", now_func.return_value),
            ],
            any_order=True,
        )


# dbアクセス関数とかを一時的に再割付けするのに便利なpatch
class TestUsingPatch(TestCase):
    print("Outside patch:", get_animals)

    with patch("__main__.get_animals"):
        print("Inside patch: ", get_animals)

    print("Outside again:", get_animals)

    fake_now = datetime(2022, 7, 8, 11, 15)

    # cannot set 'now' attribute of immutable type 'datetime.datetime'
    # with patch("datetime.datetime.now"):
    #     datetime.now.return_value = fake_now

    # 解決策
    with patch("__main__.get_do_rounds_time"):
        get_do_rounds_time.return_value = fake_now


class TestMultipleMock(TestCase):
    def test_do_rounds(self):
        with patch.multiple(
            "__main__",
            autospec=True,
            get_food_period=DEFAULT,
            get_animals=DEFAULT,
            feed_animal=DEFAULT,
        ):
            database = Mock()
            now_func = Mock(spec=datetime.now)
            now_func.return_value = datetime(2022, 7, 8, 11, 15)
            get_food_period.return_value = timedelta(hours=3)
            get_animals.return_value = [
                ("Spot", datetime(2022, 7, 8, 11, 15)),
                ("Fluffy", datetime(2022, 7, 8, 12, 30)),
                ("Jojo", datetime(2022, 7, 8, 12, 45)),
            ]
        result = do_rounds4(database, "Meerkat", now=now_func)
        assert result == 2

        food_func.assert_called_one_with(database, "Meerkat")
        animals_func.assert_called_one_with(database, "Meerkat")
        feed_func.assert_has_calls(
            [
                call(database, "Spot", now_func.return_value),
                call(database, "Fluffy", now_func.return_value),
            ],
            any_order=True,
        )
