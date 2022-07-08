from datetime import datetime, timedelta
from unittest import TestCase, main
from unittest.mock import Mock, call
from zoo_database import ZooDatabase, do_round


class TestZoo(TestCase):
    def test_mock_database(self):
        database = Mock(spec=ZooDatabase)
        print(database.feed_animal)
        database.feed_animal()
        database.feed_animal.assert_any_call()

    def test_do_rounds(self):

        now_func = Mock(spec=datetime.now)
        now_func.return_value = datetime(2022, 7, 8, 15, 45)

        database = Mock(spec=ZooDatabase)
        database.get_food_period.return_value = timedelta(hours=3)
        database.get_animals.return_value = [
            ("Spot", datetime(2022, 7, 8, 11, 15)),
            ("Fluffy", datetime(2022, 7, 8, 12, 30)),
            ("Jojo", datetime(2022, 7, 8, 12, 55)),
        ]

        result = do_round(database, "Meerkat", now=now_func)
        assert result == 2

        database.get_food_period.assert_called_once_with("Meerkat")
        database.get_animals.assert_called_once_with("Meerkat")
        database.feed_animal.assert_has_calls(
            [
                call(database, "Spot", now_func.return_value),
                call(database, "Fluffy", now_func.return_value),
            ],
            any_order=True,
        )


if __name__ == "__main__":
    main()
