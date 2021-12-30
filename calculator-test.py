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
        for i in "+-*/=()":
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


class word_dataType_tests(unittest.TestCase):
    def test_input_for_acceptable_values_range(self):
        calc = Calculator()
        calc.dataType = Datatype.word
        calc.input('0')
        self.assertEqual(calc.displayValue, '0')

    def test2_input_for_acceptable_values_range(self):
        calc = Calculator()
        calc.dataType = Datatype.word
        calc.input('0')
        calc.input('0')
        calc.input('0')
        self.assertEqual(calc.displayValue, '0')

    def test3_input_for_acceptable_values_range(self):
        calc = Calculator()
        calc.dataType = Datatype.word
        calc.input('3')
        calc.input('2')
        calc.input('7')
        calc.input('6')
        calc.input('7')
        print(calc.displayValue)
        self.assertEqual(calc.displayValue, "32767")

    def test4_input_for_acceptable_values_range(self):
        calc = Calculator()
        calc.dataType = Datatype.word
        calc.input('3')
        calc.input('!')
        calc.input('2')
        calc.input('7')
        calc.input('6')
        calc.input('8')
        self.assertEqual(calc.displayValue, "-32768")

    def test5_input_for_acceptable_values_range(self):
        # Should not accept input higher than 127
        calc = Calculator()
        calc.dataType = Datatype.word
        calc.input('3')
        calc.input('2')
        calc.input('7')
        calc.input('6')
        calc.input('8')
        self.assertEqual(calc.displayValue, "3276")

    def test6_input_for_acceptable_values_range(self):
        calc = Calculator()
        calc.dataType = Datatype.word
        calc.input('3')
        calc.input('!')
        calc.input('2')
        calc.input('7')
        calc.input('6')
        calc.input('9')
        self.assertEqual(calc.displayValue, "-3276")

    def test_operations_should_be_accepted_when_at_the_upper_value_range(self):
        calc = Calculator()
        calc.dataType = Datatype.word
        for operation in "+-*/=()":
            calc.input('3')
            calc.input('2')
            calc.input('7')
            calc.input('6')
            calc.input('7')
            calc.input(operation)
            self.assertEqual(calc.displayValue, "32767")
            self.assertEqual(calc.operation, operation)

    def test_operations_should_be_accepted_when_at_the_lower_value_range(self):
        for operation in "+-*/=()":
            calc = Calculator()
            calc.dataType = Datatype.word
            calc.input('3')
            calc.input('!')
            calc.input('2')
            calc.input('7')
            calc.input('6')
            calc.input('8')
            calc.input(operation)
            self.assertEqual(calc.displayValue, "-32768")
            self.assertEqual(calc.operation, operation)


class Binary_casting_tests(unittest.TestCase):
    def test1_binary_to_decimal_casting(self):
        calc = Calculator()
        calc.numericSystem = NumericSystem.bin
        calc.input('1')
        calc.input('1')
        calc.input('1')
        calc.numericSystem = NumericSystem.dec
        self.assertEqual(calc.displayValue, "7")

    def test2_binary_to_decimal_casting(self):
        calc = Calculator()
        calc.numericSystem = NumericSystem.bin
        calc.input('1')
        calc.input('0')
        calc.input('1')
        calc.numericSystem = NumericSystem.dec
        self.assertEqual(calc.displayValue, "5")

    def test3_binary_to_decimal_casting(self):
        calc = Calculator()
        calc.numericSystem = NumericSystem.bin
        calc.input('1')
        calc.input('0')
        calc.input('1')
        calc.input('0')
        calc.input('1')
        calc.numericSystem = NumericSystem.dec
        self.assertEqual(calc.displayValue, "21")

    def test1_binary_to_octadecimal_casting(self):
        calc = Calculator()
        calc.numericSystem = NumericSystem.bin
        calc.input('1')
        calc.input('1')
        calc.input('1')
        calc.numericSystem = NumericSystem.oct
        self.assertEqual(calc.displayValue, "7")

    def test2_binary_to_octadecimal_casting(self):
        calc = Calculator()
        calc.numericSystem = NumericSystem.bin
        calc.input('1')
        calc.input('0')
        calc.input('0')
        calc.input('0')
        calc.numericSystem = NumericSystem.oct
        self.assertEqual(calc.displayValue, "10")

    def test3_binary_to_octadecimal_casting(self):
        calc = Calculator()
        calc.numericSystem = NumericSystem.bin
        calc.input('1')
        calc.input('0')
        calc.input('1')
        calc.input('0')
        calc.input('1')
        calc.numericSystem = NumericSystem.oct
        self.assertEqual(calc.displayValue, "25")

    def test1_binary_to_hexadecimal_casting(self):
        calc = Calculator()
        calc.numericSystem = NumericSystem.bin
        calc.input('1')
        calc.input('1')
        calc.input('1')
        calc.numericSystem = NumericSystem.hex
        self.assertEqual(calc.displayValue, "7")

    def test2_binary_to_hexadecimal_casting(self):
        calc = Calculator()
        calc.numericSystem = NumericSystem.bin
        calc.input('1')
        calc.input('0')
        calc.input('0')
        calc.input('0')
        calc.input('0')
        calc.numericSystem = NumericSystem.hex
        self.assertEqual(calc.displayValue, "10")

    def test3_binary_to_hexadecimal_casting(self):
        calc = Calculator()
        calc.numericSystem = NumericSystem.bin
        calc.input('1')
        calc.input('0')
        calc.input('1')
        calc.input('0')
        calc.input('1')
        calc.numericSystem = NumericSystem.hex
        self.assertEqual(calc.displayValue, "15")


class Byte_casting_tests(unittest.TestCase):
    def test1_byte_to_word_casting(self):
        calc = Calculator()
        calc.dataType = Datatype.byte
        calc.input('1')
        calc.input('1')
        calc.input('1')
        calc.dataType = Datatype.word
        self.assertEqual(calc.displayValue, "111")

    def test2_byte_to_word_casting(self):
        calc = Calculator()
        calc.dataType = Datatype.byte
        calc.input('1')
        calc.input('1')
        calc.input('1')
        calc.dataType = Datatype.word
        self.assertEqual(calc.binaryValue, "0000000001101111")

    def test3_byte_to_word_casting(self):
        calc = Calculator()
        calc.dataType = Datatype.byte
        calc.input('1')
        calc.input('!')
        calc.input('1')
        calc.input('1')
        calc.dataType = Datatype.word
        self.assertEqual(calc.binaryValue, "1111111110010001")


unittest.main()
