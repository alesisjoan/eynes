import unittest
from random import randint
from simple import Simple
from simple import MAX_LIST_LENGTH, MAX_AGE, MIN_AGE


class TestSimple(unittest.TestCase):

    def _get_random_obj(self, data):
        return data[randint(0, (MAX_LIST_LENGTH - 1))]

    def test_seed(self):
        """
        Test can generate a list of ten dicts, containing id and age (1 to 100)
        """
        data = Simple().seed_list()
        self.assertEqual(len(data), MAX_LIST_LENGTH)

        obj1 = self._get_random_obj(data)
        self.assertGreaterEqual(obj1['age'], MIN_AGE)

        obj2 = self._get_random_obj(data)
        self.assertLessEqual(obj2['age'], MAX_AGE)

        obj3 = self._get_random_obj(data)
        self.assertIsNotNone(obj3['id'])

        # negative testing
        obj_4 = self._get_random_obj(data)
        self.assertFalse(obj_4['age'] > MAX_AGE)

        obj_5 = self._get_random_obj(data)
        self.assertFalse(obj_5['age'] < 0)

    def test_sort(self):
        """
        Test dicts are sorted by age, oldest is first
        """
        data = Simple().seed_list()
        data = Simple().sort(data)
        first_obj = data[0]
        middle_obj = self._get_random_obj(data)
        last_obj = data[-1]
        greater_ages = map(lambda o: o['age'], [first_obj, middle_obj])
        # make sure first object is the lowest age
        self.assertTrue(all([a >= last_obj['age'] for a in greater_ages]))
        lower_ages = map(lambda o: o['age'], [last_obj, middle_obj])
        # make sure last object is the greatest age
        self.assertTrue(all([a <= first_obj['age'] for a in lower_ages]))

    def main(self):
        self.test_seed()
        self.test_sort()


if __name__ == '__main__':
    unittest.main()
