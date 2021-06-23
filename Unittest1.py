import unittest
import random
import dump_all_functions as functions

class Main(unittest.TestCase):


    def if_more(self):
        x, y = int(input())
        z = functions.more(x, y)
        self.assertGreater(z, x)


    def if_less(self):
        rank = 6
        number = functions.less()
        self.assertLess(number, rank)


    def if_consonant(self):
        consonants = ['clean_prima', 'clean_octava', 'clean_quarta', 'clean_quinta', 'big_tertia', 'small_tertia', 'big_sexta', 'small_sexta']
        intervals = consonants
        interval_1 = random.choice(intervals)
        interval_2 = functions.test_in()
        self.assertIN(interval_1, consonants)
        self.assertNotIn(interval_2, consonants)


    def if_truth(self):
        x = 'FDSDWER'
        y = functions.truth(x)
        self.assertTrue(y.islower())
        self.assertFalse(x.islower())


    def if_equal(self):
        lords = {'Svyatoslav', 'Olgerd', 'Konstantin', 'Nikolay', 'Ingvar'}
        rurics = functions.equal()
        self.assertEqual(lords, rurics)


if __name__ == '__main__':
    unittest.main()
