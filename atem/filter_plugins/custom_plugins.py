class FilterModule(object):
    ''' Custom filters are loaded by FilterModule objects '''

    def filters(self):
        ''' FilterModule objects return a dict mapping filter names to
            filter functions. '''
        return {
            'generate_answer': self.generate_answer,
        }

    def generate_answer(self, value):
        return '2'
