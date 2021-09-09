import unittest

from src.models.users import get_users


class TestModelUsers(unittest.TestCase):
    def test_get_users(self):
        self.assertEqual(get_users(), [])
