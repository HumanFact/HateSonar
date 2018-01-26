import unittest

from hatesonar.api import Sonar


class TestAPI(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.text = 'this is test text.'

    def test_ping(self):
        sonar = Sonar()
        res = sonar.ping(self.text)
        self.assertIn('text', res)
        self.assertIn('top_class', res)
        self.assertIn('classes', res)
        self.assertIsInstance(res['text'], str)
        self.assertIsInstance(res['top_class'], str)
        self.assertIsInstance(res['classes'], list)
        for d in res['classes']:
            self.assertIn('class_name', d)
            self.assertIn('confidence', d)
            self.assertIsInstance(d['class_name'], str)
            self.assertIsInstance(d['confidence'], float)
