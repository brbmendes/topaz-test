import unittest
import uuid

from src.entities.tasks import Task


class TestTask(unittest.TestCase):
    task = None
    def setUp(self):
        self.task = Task(2)

    def tearDown(self):
        self.task = None

    def test_get_id(self):
        current = type(self.task.get_id())
        expected = type(uuid.uuid4())
        self.assertEqual(current,expected)

    def test_get_ticks(self):
        current = self.task.get_ticks()
        expected = 2
        self.assertEqual(current,expected)

    def test_decrement_ticks(self):
        self.task.decrement_ticks()
        current = self.task.get_ticks()
        expected = 1
        self.assertEqual(current,expected)

if __name__ == '__name__':
    unittest.main()
