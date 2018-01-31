
if__name__='__main__'
unitest='main'
from task1 import re_text
from task1 import getIndex
from task1 import multi
from task1 import calc_area
from task1 import diction


import unittest

class TestAssignmentOne(unittest.TestCase):

    def test_re_text(self):
        self.assertEqual(re_text('mobile'), 'mbl')
  
    def test_getIndex(self):
        self.assertEqual(getIndex('This is javaScript','i'), [2,5,15])
    
    def test_multi(self):
        self.assertEqual(multi(3), [[1],[2,4],[3,6,9]])

    
    def test_calc_area(self):
        self.assertEqual(calc_area("s",5), 25 )
   
    def test_diction(self):
        #l1 =['marwa','lamiaa','Mohamed']
        #d1={'l': ['lamiaa'], 'M': ['Mohamed'], 'm': ['marwa']}
        self.assertEqual(diction(['marwa','lamiaa','Mohamed']), {'l': ['lamiaa'], 'M': ['Mohamed'], 'm': ['marwa']})

if __name__ == '__main__':
    unittest.main()