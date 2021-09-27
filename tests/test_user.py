import unittest
import uuid

from src.entities.users import User


class TestUser(unittest.TestCase):
    user = None
    def setUp(self):
        self.user = User()

    def tearDown(self):
        self.user = None

    def test_get_id(self):
        current = type(self.user.get_id())
        expected = type(uuid.uuid4())
        self.assertEqual(current,expected)

if __name__ == '__name__':
    unittest.main()
