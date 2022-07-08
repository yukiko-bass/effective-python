import contextlib
from datetime import datetime, timedelta
import io
from unittest import TestCase
from unittest.mock import patch
from zoo_database import ZooDatabase, do_round

DATABASE = None


def get_database():
    global DATABASE
    if DATABASE is None:
        DATABASE = ZooDatabase()
    return DATABASE


def main(argv):
    database = get_database()
    species = argv[1]
    count = do_round(database, species)
    print(f"Fed {count} {species}(s)")
    return 0


class TestZooDatabase(TestCase):
    def test(self):
        with patch("__main__.DATABASE", spec=ZooDatabase):
            now = datetime.now()

            DATABASE.get_food_period.return_value = timedelta(hours=3)
            DATABASE.get_animals.return_value = [
                ("Spot", now - timedelta(minutes=4.5)),
                ("Fluffy", now - timedelta(minutes=3.25)),
                ("Jojo", now - timedelta(minutes=3)),
            ]

            fake_stdout = io.StringIO()
            with contextlib.redirect_stdout(fake_stdout):
                main(["program name", "Meerkat"])

            found = fake_stdout.getvalue()
            expected = "Fed 2 Meerkat(s)\n"

            self.assertEqual(found, expected)
