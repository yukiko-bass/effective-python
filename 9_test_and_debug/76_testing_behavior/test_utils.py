from unittest import TestCase, main
from utils import to_str


class TestUtils(TestCase):
    def test_to_str_bytes(self):
        self.assertEqual("hello", to_str("hello"))

    def test_to_str_str(self):
        self.assertNotEqual("incorrect", to_str("hello"))

    def test_to_str_bad(self):
        self.assertRaises(TypeError, to_str("hello"))


if __name__ == "__main__":
    main()
