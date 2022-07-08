from unittest import TestCase, main
from utils import to_str


class TestDataDriven(TestCase):
    def test_good(self):
        good_cases = [
            (b"my bytes", "my bytes"),
            ("no error", b"no error"),  # これは失敗する
            ("other str", "other str"),
        ]
        for value, expected in good_cases:
            # subTest により、失敗したところで止まらず、後続もテストしてくれる
            with self.subTest(value):
                self.assertEqual(expected, to_str(value))

    def test_bad(self):
        bad_cases = [
            (object(), TypeError),
            (b"\xfa\xfa", UnicodeDecodeError),
        ]
        for value, exception in bad_cases:
            with self.subTest(value):
                with self.assertRaises(exception):
                    to_str(value)


if __name__ == "__main__":
    main()
