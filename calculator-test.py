import unittest
from calculator import *


class Initial_tests(unittest.TestCase):

    def test_class_initialization(self):
        calc = Calculator()
        self.assertIsInstance(calc, Calculator)

    def test_initial_value(self):
        calc = Calculator()
        self.assertEqual(calc.displayValue, '0')

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
        self.assertEqual(calc.displayValue, '1')
        self.assertEqual(calc.operation, '')

    def test2_when_input_0(self):
        calc = Calculator()
        calc.numericSystem = NumericSystem.bin

        calc.input('0')
        self.assertEqual(calc.displayValue, '0')
        self.assertEqual(calc.operation, '')

    def test2_when_input_other_numbers(self):
        calc = Calculator()
        calc.numericSystem = NumericSystem.bin

        for number in ["23456789"]:
            calc.input(number)
            self.assertEqual(calc.displayValue, '0')
            self.assertEqual(calc.operation, '')

    def test_when_input_accepted_signs(self):
        calc = Calculator()
        calc.numericSystem = NumericSystem.bin
        for i in "+-*/=!()":
            calc.value = '0'
            calc.operation = ''

            calc.input(i)
            self.assertEqual(calc.displayValue, '0')
            self.assertEqual(calc.operation, i)

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
                self.assertEqual(calc.displayValue, '0')


class Oct_input_tests(unittest.TestCase):

    def test_when_input_accepted_numeric_values(self):
        calc = Calculator()
        calc.numericSystem = NumericSystem.oct
        for i in "12345670":
            calc.value = '0'
            calc.operation = ''

            calc.input(i)
            self.assertEqual(calc.displayValue, i)
            self.assertEqual(calc.operation, '')

    def test_when_input_accepted_signs(self):
        calc = Calculator()
        calc.numericSystem = NumericSystem.oct
        for i in "+-*/=!()":
            calc.value = '0'
            calc.operation = ''

            calc.input(i)
            self.assertEqual(calc.displayValue, '0')
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
                self.assertEqual(calc.displayValue, '0')


class Dec_input_tests(unittest.TestCase):

    def test_when_input_accepted_numeric_values(self):
        calc = Calculator()
        calc.numericSystem = NumericSystem.dec
        for i in "1234567890":
            calc.value = '0'
            calc.operation = ''

            calc.input(i)
            self.assertEqual(calc.displayValue, i)
            self.assertEqual(calc.operation, '')

    def test_when_input_accepted_signs(self):
        calc = Calculator()
        calc.numericSystem = NumericSystem.dec
        for i in "+-*/=()":
            calc.value = '0'
            calc.operation = ''

            calc.input(i)
            self.assertEqual(calc.displayValue, '0')
            self.assertEqual(calc.operation, i)

    def test_when_input_change_sign(self):
        calc = Calculator()
        calc.numericSystem = NumericSystem.dec
        calc.input('1')
        calc.input('!')
        self.assertEqual(calc.displayValue, '-1')
        self.assertEqual(calc.operation, '')

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
                self.assertEqual(calc.displayValue, '0')


class hex_input_tests(unittest.TestCase):

    def test_when_input_accepted_numeric_values(self):
        calc = Calculator()
        calc.numericSystem = NumericSystem.hex
        for i in "1234567890ABCDEF":
            calc.value = '0'
            calc.operation = ''

            calc.input(i)
            self.assertEqual(calc.displayValue, i)
            self.assertEqual(calc.operation, '')

    def test_when_input_accepted_signs(self):
        calc = Calculator()
        calc.numericSystem = NumericSystem.hex
        for i in "+-*/=!()":
            calc.value = '0'
            calc.operation = ''

            calc.input(i)
            self.assertEqual(calc.displayValue, '0')
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
                self.assertEqual(calc.displayValue, '0')


class byte_dataType_tests(unittest.TestCase):
    def test_input_for_acceptable_values_range(self):
        calc = Calculator()
        calc.dataType = Datatype.byte
        calc.input('0')
        self.assertEqual(calc.displayValue, '0')

    def test2_input_for_acceptable_values_range(self):
        calc = Calculator()
        calc.dataType = Datatype.byte
        calc.input('0')
        calc.input('0')
        calc.input('0')
        self.assertEqual(calc.displayValue, '0')

    def test3_input_for_acceptable_values_range(self):
        calc = Calculator()
        calc.dataType = Datatype.byte
        calc.input('1')
        calc.input('2')
        calc.input('7')
        print(calc.displayValue)
        self.assertEqual(calc.displayValue, "127")

    def test4_input_for_acceptable_values_range(self):
        calc = Calculator()
        calc.dataType = Datatype.byte
        calc.input('1')
        calc.input('!')
        calc.input('2')
        calc.input('8')
        self.assertEqual(calc.displayValue, "-128")

    def test5_input_for_acceptable_values_range(self):
        # Should not accept input higher than 127
        calc = Calculator()
        calc.dataType = Datatype.byte
        calc.input('1')
        calc.input('2')
        calc.input('8')  # would make input > 127
        self.assertEqual(calc.displayValue, "12")

    def test6_input_for_acceptable_values_range(self):
        calc = Calculator()
        calc.dataType = Datatype.byte
        calc.input('1')
        calc.input('!')
        calc.input('2')
        calc.input('9')
        self.assertEqual(calc.displayValue, "-12")

    def test_operations_should_be_accepted_when_at_the_upper_value_range(self):
        calc = Calculator()
        calc.dataType = Datatype.byte
        for operation in "+-*/=()":
            calc.input('1')
            calc.input('2')
            calc.input('7')
            calc.input(operation)
            self.assertEqual(calc.displayValue, "127")
            self.assertEqual(calc.operation, operation)

    def test_operations_should_be_accepted_when_at_the_lower_value_range(self):
        for operation in "+-*/=()":
            calc = Calculator()
            calc.dataType = Datatype.byte
            calc.input('1')
            calc.input('!')
            calc.input('2')
            calc.input('8')
            calc.input(operation)
            self.assertEqual(calc.displayValue, "-128")
            self.assertEqual(calc.operation, operation)


# class Casting_tests(unittest.TestCase):

#     def test_cast_bin_to_dec(self):
#         # GIVEN
#         calc = Calculator()
#         calc.numericSystem = NumericSystem.bin
#         calc.value = '1101'
#         # WHEN
#         calc.numericSystem = NumericSystem.dec
#         # THEN
#         self.assertEqual(calc.displayValue, '13')

#     def test_cast_bin_to_oct(self):
#         # GIVEN
#         calc = Calculator()
#         calc.numericSystem = NumericSystem.bin
#         calc.value = '1101'
#         # WHEN
#         calc.numericSystem = NumericSystem.oct
#         # THEN
#         self.assertEqual(calc.displayValue, '15')

#     def test_cast_bin_to_hex(self):
#         # GIVEN
#         calc = Calculator()
#         calc.numericSystem = NumericSystem.bin
#         calc.value = '1101'
#         # WHEN
#         calc.numericSystem = NumericSystem.hex
#         # THEN
#         self.assertEqual(calc.displayValue, 'D')

#     def test_cast_hex_to_bin(self):
#         # GIVEN
#         calc = Calculator()
#         calc.numericSystem = NumericSystem.hex
#         calc.value = 'D'
#         # WHEN
#         calc.numericSystem = NumericSystem.bin
#         # THEN
#         self.assertEqual(
#             calc.value, '1101')


unittest.main()
