from random import randint
import uuid
import operator

MAX_LIST_LENGTH = 10
MAX_AGE = 100
MIN_AGE = 1


class Simple(object):

    def _generateId(self):
        return str(uuid.uuid1())

    def _seed_one(self):
        return {
            'id': self._generateId(),
            'age': randint(MIN_AGE, MAX_AGE)
        }

    def seed_list(self):
        data = []
        for x in range(0, MAX_LIST_LENGTH):
            data.append(self._seed_one())
        return data

    def sort(self, data, key='age', reverse=True):
        sorted_data = sorted(data, key=operator.itemgetter(key),
                             reverse=reverse)
        print('First: %i' % sorted_data[0]['age'])
        print('Last: %i' % sorted_data[-1]['age'])
        return sorted_data


if __name__ == '__main__':
    data = Simple().seed_list()
    print(data)
