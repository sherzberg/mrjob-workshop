from mrjob.job import MRJob


class WordCount(MRJob):

    def mapper(self, _, line):
        yield "words", len(line.split())

    def reducer(self, key, values):
        yield key, sum(values)


if __name__ == '__main__':
    WordCount.run()
