import unittest
import uuid

from src.entities.jobs import Job
from src.entities.users import User
from src.entities.tasks import Task


class TestJob(unittest.TestCase):
    job = None
    def setUp(self):
        user = User()
        task = Task(2)
        self.job = Job(user,task)

    def tearDown(self):
        self.job = None

    def test_get_id(self):
        current = type(self.job.get_id())
        expected = type(uuid.uuid4())
        self.assertEqual(current,expected)

    def test_get_user(self):
        current = type(self.job.get_user())
        expected = type(User())
        self.assertEqual(current,expected)

    def test_get_task(self):
        current = type(self.job.get_task())
        expected = type(Task(2))
        self.assertEqual(current,expected)

if __name__ == '__name__':
    unittest.main()
