from pathlib import Path
from tempfile import TemporaryDirectory
from unittest import TestCase, main


class TestEnviroment(TestCase):
    def setUp(self):
        self.test_dir = TemporaryDirectory()
        self.test_path = Path(self.test_dir.name)

    def tearDown(self):
        self.test_dir.cleanup()

    def test_modify_file(self):
        with open(self.test_path / "data.bin", "w") as f:
            f.write("hello")


if __name__ == "__main__":
    main()
