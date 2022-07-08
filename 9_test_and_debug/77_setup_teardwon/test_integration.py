# モジュール内の全TestCaseクラスの初期化より前に走る
from unittest import TestCase, main


def setUpModule():
    print("* Module setup")


# モジュール内の全TestCaseクラスの実行が終わったあとに走る
def tearDownModule():
    print("* Module clean-up")


class TestIntegration(TestCase):
    def setUp(self):
        print("* Test1 setup")

    def tearDown(self):
        print("* Test1 clean-up")

    def test_end_to_end1(self):
        print("* Test1-1")

    def test_end_to_end2(self):
        print("* Test1-2")


class TestIntegration2(TestCase):
    def setUp(self):
        print("* Test2 setup")

    def tearDown(self):
        print("* Test2 clean-up")

    def test_start_to_end1(self):
        print("* Test2-1")

    def test_start_to_end2(self):
        print("* Test2-2")


if __name__ == "__main__":
    main()

"""
実行順
* Module setup
* Test1 setup
* Test1-1
* Test1 clean-up
.* Test1 setup
* Test1-2
* Test1 clean-up
.* Test2 setup
* Test2-1
* Test2 clean-up
.* Test2 setup
* Test2-2
* Test2 clean-up
.* Module clean-up
"""
