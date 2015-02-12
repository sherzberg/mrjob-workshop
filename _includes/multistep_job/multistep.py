from mrjob.job import MRJob


class MultistepJob(MRJob):

    def mapper(self, _, value):
        count, animal = value.split()

        yield animal, int(count)

    def reducer(self, animal, count):
        yield None, (sum(count), animal)

    def reducer_max(self, _, values):
        yield max(values)

    def steps(self):
        return [
            self.mr(mapper_pre_filter='grep at',
                    mapper=self.mapper,
                    reducer=self.reducer
                    ),
            self.mr(reducer=self.reducer_max)
        ]

if __name__ == '__main__':
    MultistepJob.run()
