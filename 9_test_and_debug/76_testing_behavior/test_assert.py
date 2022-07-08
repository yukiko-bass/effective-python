from unittest import TestCase, main


class TestAssert(TestCase):
    # こっちのほうが詳細を出力してくれる
    def test_assert_helper(self):
        expected = 12
        found = 2 * 5
        self.assertEqual(expected, found)

    def test_assert_statement(self):
        expected = 12
        found = 2 * 5
        assert expected == found


if __name__ == "__main__":
    main()
