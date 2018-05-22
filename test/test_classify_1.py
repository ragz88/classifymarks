#!/usr/bin/env python3

import unittest

import os

import classify

this_dir = os.path.dirname(__file__)


class TestExclude(unittest.TestCase):

    def setUp(self):
        infile = open(os.path.join(this_dir,"marks.txt"))
        #infile = open("marks.txt")
        print (infile)
        self.data = classify.getData(infile)

    def test_thoseInRange1(self):
        students = classify.thoseInRange(self.data, 45, 60)        
        self.assertListEqual(students, ["student45", "student55"])

    def test_thoseInRange2(self):
        students = classify.thoseInRange(self.data, 5, 25)        
        self.assertListEqual(students, ["none"])

    def tearDown(self):
        del self.data
        

if __name__ == '__main__':


    unittest.main()
