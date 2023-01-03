#!/bin/usr/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    def test_argument_1(self):
        with self.assertRaises(KeyError):
            max_integer({1: 'a', 2: 'b'})

    def test_argument_2(self):
        with self.assertRaises(KeyError):
            max_integer({0: 'a', 2: 'b'})

    def test_argument_3(self):
        with self.assertRaises(TypeError):
            max_integer(True)

    def test_none(self):
        self.assertIsNone(max_integer())

    def test_one_element(self):
        self.assertEqual(max_integer([1]), 1)

    def test_with_negatives(self):
        self.assertEqual(max_integer([-1, 0, -5]), 0)

    def test_with_string(self):
        self.assertEqual(max_integer('bcdab'), 'd')

    def test_with_positives(self):
        self.assertEqual(max_integer([8, 10, 5, 1]), 10)

    def test_with_mixed(self):
        with self.assertRaises(TypeError):
            max_integer([8, '10', 5, 1])
