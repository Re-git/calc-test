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
        self.assertEqual(calc.numericSystem, NumericSystem.dec)

    def test_initial_binary_value(self):
        calc = Calculator()
        self.assertEqual(calc.binaryValue, '0' * 64)


class Binary_input_tests(unittest.TestCase):

    def test1_when_input_1(self):
        calc = Calculator()
        calc.numericSystem = NumericSystem.bin

        calc.input('1')
        self.assertEqual(calc.value, '1')
        self.assertEqual(calc.operation, '')

    def test2_when_input_0(self):
        calc = Calculator()
        calc.numericSystem = NumericSystem.bin

        calc.input('0')
        self.assertEqual(calc.value, '0')
        self.assertEqual(calc.operation, '')

    def test2_when_input_other_numbers(self):
        calc = Calculator()
        calc.numericSystem = NumericSystem.bin

        for number in ["23456789"]:
            calc.input(number)
            self.assertEqual(calc.value, '0')
            self.assertEqual(calc.operation, '')

    def test2_when_input_other_characters(self):
        calc = Calculator()
        calc.numericSystem = NumericSystem.bin

        for letter in ["abcdefghijklmnoprstquvwzABCDEFGHIJKLMNOPRSTQUVWZ"]:
            calc.input(letter)
            self.assertEqual(calc.value, '0')
            self.assertEqual(calc.operation, '')

    def test_when_input_percent(self):
        calc = Calculator()
        calc.numericSystem = NumericSystem.bin

        calc.input('%')
        self.assertEqual(calc.value, '0')
        self.assertEqual(calc.operation, '')

    def test_when_input_plus_sign(self):
        calc = Calculator()
        calc.numericSystem = NumericSystem.bin
        calc.input('+')
        self.assertEqual(calc.operation, '+')
        self.assertEqual(calc.value, '0')

    def test_when_input_minus_sign(self):
        calc = Calculator()
        calc.numericSystem = NumericSystem.bin
        calc.input('-')
        self.assertEqual(calc.operation, '-')
        self.assertEqual(calc.value, '0')

    def test_when_input_slash_sign(self):
        calc = Calculator()
        calc.numericSystem = NumericSystem.bin
        calc.input('/')
        self.assertEqual(calc.operation, '/')
        self.assertEqual(calc.value, '0')

    def test_when_input_start_sign(self):
        calc = Calculator()
        calc.numericSystem = NumericSystem.bin
        calc.input('*')
        self.assertEqual(calc.operation, '*')
        self.assertEqual(calc.value, '0')

    def test_when_input_exclamation_sign(self):
        calc = Calculator()
        calc.numericSystem = NumericSystem.bin
        calc.input('!')
        self.assertEqual(calc.operation, '!')
        self.assertEqual(calc.value, '0')

    def test_when_input_equal_sign(self):
        calc = Calculator()
        calc.numericSystem = NumericSystem.bin
        calc.input('=')
        self.assertEqual(calc.operation, '=')
        self.assertEqual(calc.value, '0')

    def test_when_input_open_paren_sign(self):
        calc = Calculator()
        calc.numericSystem = NumericSystem.bin
        calc.input('(')
        self.assertEqual(calc.operation, '(')
        self.assertEqual(calc.value, '0')

    def test_when_input_close_paren_sign(self):
        calc = Calculator()
        calc.numericSystem = NumericSystem.bin
        calc.input(')')
        self.assertEqual(calc.operation, ')')
        self.assertEqual(calc.value, '0')

    def test_for_other_signs(self):
        calc = Calculator()
        calc.numericSystem = NumericSystem.bin

        for i in range(12, 256):
            if chr(i) in "01+-*/=!()":
                continue
            else:
                # reset class to default value
                calc.value = '0'
                calc.operation = ''
                # input char
                calc.input(chr(i))
                self.assertEqual(calc.operation, '')
                self.assertEqual(calc.value, '0')


class Oct_input_tests(unittest.TestCase):

    def test_when_input_accepted_numeric_values(self):
        calc = Calculator()
        calc.numericSystem = NumericSystem.oct
        for i in "12345670":
            calc.value = '0'
            calc.operation = ''

            calc.input(i)
            self.assertEqual(calc.value, i)
            self.assertEqual(calc.operation, '')

    def test_when_input_accepted_signs(self):
        calc = Calculator()
        calc.numericSystem = NumericSystem.oct
        for i in "+-*/=!()":
            calc.value = '0'
            calc.operation = ''

            calc.input(i)
            self.assertEqual(calc.value, '0')
            self.assertEqual(calc.operation, i)

    def test_for_other_signs(self):
        calc = Calculator()
        calc.numericSystem = NumericSystem.oct

        for i in range(12, 256):
            if chr(i) in "01234567+-*/=!()":
                continue
            else:
                # reset class to default value
                calc.value = '0'
                calc.operation = ''
                # input char
                calc.input(chr(i))
                self.assertEqual(calc.operation, '')
                self.assertEqual(calc.value, '0')


class Dec_input_tests(unittest.TestCase):

    def test_when_input_accepted_numeric_values(self):
        calc = Calculator()
        calc.numericSystem = NumericSystem.dec
        for i in "1234567890":
            calc.value = '0'
            calc.operation = ''

            calc.input(i)
            self.assertEqual(calc.value, i)
            self.assertEqual(calc.operation, '')

    def test_when_input_accepted_signs(self):
        calc = Calculator()
        calc.numericSystem = NumericSystem.dec
        for i in "+-*/=!()":
            calc.value = '0'
            calc.operation = ''

            calc.input(i)
            self.assertEqual(calc.value, '0')
            self.assertEqual(calc.operation, i)

    def test_for_other_signs(self):
        calc = Calculator()
        calc.numericSystem = NumericSystem.dec

        for i in range(12, 256):
            if chr(i) in "01234567890+-*/=!()":
                continue
            else:
                # reset class to default value
                calc.value = '0'
                calc.operation = ''
                # input char
                calc.input(chr(i))
                self.assertEqual(calc.operation, '')
                self.assertEqual(calc.value, '0')


class hex_input_tests(unittest.TestCase):

    def test_when_input_accepted_numeric_values(self):
        calc = Calculator()
        calc.numericSystem = NumericSystem.hex
        for i in "1234567890ABCDEF":
            calc.value = '0'
            calc.operation = ''

            calc.input(i)
            self.assertEqual(calc.value, i)
            self.assertEqual(calc.operation, '')

    def test_when_input_accepted_signs(self):
        calc = Calculator()
        calc.numericSystem = NumericSystem.hex
        for i in "+-*/=!()":
            calc.value = '0'
            calc.operation = ''

            calc.input(i)
            self.assertEqual(calc.value, '0')
            self.assertEqual(calc.operation, i)

    def test_for_other_signs(self):
        calc = Calculator()
        calc.numericSystem = NumericSystem.hex

        for i in range(12, 256):
            if chr(i) in "01234567890ABCDEF+-*/=!()":
                continue
            else:
                # reset class to default value
                calc.value = '0'
                calc.operation = ''
                # input char
                calc.input(chr(i))
                self.assertEqual(calc.operation, '')
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
            calc.value, '1101')


unittest.main()
