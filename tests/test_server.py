import unittest
import uuid

from src.entities.jobs import Job
from src.entities.servers import Server
from src.entities.tasks import Task
from src.entities.users import User


class TestServer(unittest.TestCase):
    server = None
    def setUp(self):
        self.server = Server(1,3)

    def tearDown(self):
        self.server = None

    def test_get_id(self):
        current = self.server.get_id()
        expected = 1
        self.assertEqual(current,expected)

    def test_can_add_job_with_default_value(self):
        current = self.server.can_add_job()
        expected = True
        self.assertEqual(current,expected)

    def test_can_add_job_has_spaces_for_new_jobs(self):
        for number in range(2):
            job = Job(User(),Task(2))
            self.server.add_job(job)
        current = self.server.can_add_job()
        expected = True
        self.assertEqual(current, expected)

    def test_can_add_job_has_no_spaces_for_new_jobs(self):
        for number in range(3):
            job = Job(User(),Task(2))
            self.server.add_job(job)
        current = self.server.can_add_job()
        expected = False
        self.assertEqual(current, expected)

    def test_add_job_when_has_spaces_for_new_jobs(self):
        for number in range(2):
            job = Job(User(),Task(2))
            self.server.add_job(job)
        current = len(self.server.get_running_jobs())
        expected = 2
        self.assertEqual(current, expected)

    def test_add_job_when_has_no_spaces_for_new_jobs(self):
        for number in range(3):
            job = Job(User(),Task(2))
            self.server.add_job(job)
        current = len(self.server.get_running_jobs())
        expected = 3
        self.assertEqual(current, expected)

    def test_get_running_jobs_when_add_one_job(self):
        job = Job(User(), Task(2))
        self.server.add_job(job)
        current = len(self.server.get_running_jobs())
        expected = 1
        self.assertEqual(current, expected)

    def test_get_uptime(self):
        current = self.server.get_uptime()
        expected = 1
        self.assertEqual(current,expected)

    def test_update_uptime(self):
        self.server.update_uptime()
        current = self.server.get_uptime()
        expected = 2
        self.assertEqual(current,expected)

    def test_update_tasks_remove_finished(self):
        for number in range(2):
            job = Job(User(), Task(number + 1))
            self.server.add_job(job)
        self.server.update_tasks_remove_finished()
        current = len(self.server.get_running_jobs())
        expected = 1
        self.assertEqual(current,expected)




if __name__ == '__name__':
    unittest.main()
