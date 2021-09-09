import unittest
from src.models.test import soma


class TestSoma(unittest.TestCase):
    def test_retorna_soma_10_10(self):
        self.assertEqual(soma(10, 10), 20)
