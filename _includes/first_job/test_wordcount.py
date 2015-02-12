import unittest

from wordcount import WordCount


class TestWordCount(unittest.TestCase):

    def setUp(self):
        self.job = WordCount()

    def test_word_count_mapper(self):
        line = 'oh hi pyowa!'

        self.assertEqual(self.job.mapper(None, line).next(), ('words', 3))


if __name__ == '__main__':
    unittest.main()
