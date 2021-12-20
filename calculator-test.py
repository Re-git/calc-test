import unittest
from calculator import *


class Initial_tests(unittest.TestCase):

    def test_class_initialization(self):
        calc = Calculator()
        self.assertIsInstance(calc, Calculator)

    def test_initial_value(self):
        calc = Calculator()
        self.assertEqual(calc.value, '0')

    def test_initial_datatype(self):
        calc = Calculator()
        self.assertEqual(calc.dataType, Datatype.qword)

    def test_initial_numeric_system(self):
        calc = Calculator()
        self.assertEqual(calc.numericSystem, NumericSystem.bin)

    def test_initial_binary_value(self):
        calc = Calculator()
        self.assertEqual(calc.binaryValue, '0' * 64)

    def test_initial_hex_value(self):
        calc = Calculator()
        self.assertEqual(calc.hexValue, '0')

    def test_initial_oct_value(self):
        calc = Calculator()
        self.assertEqual(calc.octValue, '0')


class Binary_input_tests(unittest.TestCase):

    def test1_when_input_1(self):
        calc = Calculator()
        calc.input('1')
        self.assertEqual(calc.value, '1')

    def test2_when_input_0(self):
        calc = Calculator()
        calc.input('0')
        self.assertEqual(calc.value, '0')

    def test2_when_input_other_numbers(self):
        calc = Calculator()
        for number in ["234567890"]:
            calc.input(number)
            self.assertEqual(calc.value, '0')

    def test2_when_input_other_characters(self):
        calc = Calculator()
        for letter in ["abcdefghijklmnoprstquvwzABCDEFGHIJKLMNOPRSTQUVWZ"]:
            calc.input(letter)
            self.assertEqual(calc.value, '0')


class Casting_tests(unittest.TestCase):

    def test_cast_bin_to_dec(self):
        # GIVEN
        calc = Calculator()
        calc.numericSystem = NumericSystem.bin
        calc.value = '1101'
        # WHEN
        calc.numericSystem = NumericSystem.dec
        # THEN
        self.assertEqual(calc.value, '13')

    def test_cast_bin_to_oct(self):
        # GIVEN
        calc = Calculator()
        calc.numericSystem = NumericSystem.bin
        calc.value = '1101'
        # WHEN
        calc.numericSystem = NumericSystem.oct
        # THEN
        self.assertEqual(calc.value, '15')

    def test_cast_bin_to_hex(self):
        # GIVEN
        calc = Calculator()
        calc.numericSystem = NumericSystem.bin
        calc.value = '1101'
        # WHEN
        calc.numericSystem = NumericSystem.hex
        # THEN
        self.assertEqual(calc.value, 'D')

    def test_cast_hex_to_bin(self):
        # GIVEN
        calc = Calculator()
        calc.numericSystem = NumericSystem.hex
        calc.value = 'D'
        # WHEN
        calc.numericSystem = NumericSystem.bin
        # THEN
        self.assertEqual(
            calc.value, '0000000000000000000000000000000000000000000000000000000000001101')


unittest.main()
