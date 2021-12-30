class Datatype:
    byte = '8'
    word = '16'
    dword = '32'
    qword = '64'


class NumericSystem:
    bin = ('b', 2)
    dec = ('d', 10)
    hex = ('X', 16)
    oct = ('o', 8)


class Operations:
    add = 'add'
    sub = 'sub'
    mul = 'mul'
    div = 'div'


class Calculator:

    def __init__(self):
        self.negative = False
        self._value = '0'
        self._numericSystem = NumericSystem.dec
        self._dataType = Datatype.qword
        self._binaryValue = 64 * '0'
        self._operation = ''

    @property
    def operation(self):
        return self._operation

    @operation.setter
    def operation(self, v):
        self._operation = v

    @property
    def value(self):
        if self.negative:
            return self._value
        return self._value

    @property
    def displayValue(self):
        if self.negative:
            return '-' + self._value
        return self._value

    @value.setter
    def value(self, value):
        self._value = value

    @property
    def binaryValue(self):
        if self.value == '0':
            return int(self.dataType) * '0'
        if not self.negative:
            binaryLength = len(self.binaryRepresentation())
            return (int(self.dataType)-binaryLength) * '0' + self.binaryRepresentation()
        return bin(int(self.displayValue) + (1 << (int(self.dataType))))[2:]

    @property
    def dataType(self):
        return self._dataType

    @dataType.setter
    def dataType(self, newDataType):
        self._dataType = newDataType

    @property
    def numericSystem(self):
        return self._numericSystem

    @numericSystem.setter
    def numericSystem(self, newNumericSystem):
        if self.numericSystem == newNumericSystem:
            return  # do nothing
        else:
            self.value = self.castValue(newNumericSystem[0])
            self._numericSystem = newNumericSystem

    def valueIsinRange(self, inputValue):
        acceptedValues = ""
        if self.numericSystem == NumericSystem.bin:
            acceptedValues = "01"
        if self.numericSystem == NumericSystem.oct:
            acceptedValues = "01234567"
        if self.numericSystem == NumericSystem.dec:
            acceptedValues = "01234567890"
        if self.numericSystem == NumericSystem.hex:
            acceptedValues = "01234567890ABCDEF"

        if inputValue in acceptedValues:
            upper = 2 ** (int(self.dataType)-1)  # 128
            lower = (2 ** (int(self.dataType)-1)) * -1  # -128
            newValue = self.value + inputValue

            if self.negative:
                return int(newValue, self.numericSystem[1]) * -1 < upper and int(newValue, self.numericSystem[1]) * -1 >= lower
            return int(newValue, self.numericSystem[1]) < upper and int(newValue, self.numericSystem[1]) >= lower
        else:
            return True

    def changeSign(self):
        if self.value != '0':
            self.negative = not self.negative

    def evaluateOperation(self, character):
        if character == '!':
            self.changeSign()
            self.operation = ''

    def input(self, character):
        if self.valueIsinRange(character):
            if self.numericSystem[0] == NumericSystem.bin[0]:
                self.binInput(character)
            elif self.numericSystem[0] == NumericSystem.oct[0]:
                self.octInput(character)
            elif self.numericSystem[0] == NumericSystem.dec[0]:
                self.decInput(character)
            elif self.numericSystem[0] == NumericSystem.hex[0]:
                self.hexInput(character)
            else:
                raise Exception("Unknown numericSystem!")

    def binInput(self, character):
        if character in "01":
            if self.value == '0':
                self.value = character
            else:
                self.value += character
        if character in "+-*/=!()":
            self.operation = character
            self.evaluateOperation(character)

    def octInput(self, character):
        if character in "01234567":
            if self.value == '0':
                self.value = character
            else:
                self.value += character
        if character in "+-*/=!()":
            self.operation = character

    def decInput(self, character):
        if character in "0123456789":
            if self.value == '0':
                self.value = character
            else:
                self.value += character
        if character in "+-*/=!()":
            self.operation = character
            self.evaluateOperation(character)

    def hexInput(self, character):
        if character in "0123456789ABCDEF":
            if self.value == '0':
                self.value = character
            else:
                self.value += character
        if character in "+-*/=!()":
            self.operation = character

    def decimalRepresentation(self):
        if self.numericSystem[0] == NumericSystem.bin[0]:
            return str(int(self.value, 2))
        else:
            raise Exception("Unknown numericSystem!")

    def binaryRepresentation(self):
        if self.numericSystem[0] == NumericSystem.bin[0]:
            return format(
                int(self.value, 2), NumericSystem.bin[0])
        if self.numericSystem[0] == NumericSystem.hex[0]:
            return format(
                int(self.value, 16), NumericSystem.bin[0])
        if self.numericSystem[0] == NumericSystem.dec[0]:
            return format(
                int(self.value, 10), NumericSystem.bin[0])
        else:
            raise Exception("Unknown numericSystem!")

    def hexRepresentation(self):

        if self.numericSystem[0] == NumericSystem.dec[0]:
            return format(
                int(self.value, 10), NumericSystem.hex[0])
        if self.numericSystem[0] == NumericSystem.bin[0]:
            return format(
                int(self.value, 2), NumericSystem.hex[0])
        else:
            raise Exception("Unknown numericSystem!")

    def octRepresentation(self):
        if self.numericSystem[0] == NumericSystem.dec[0]:
            return format(
                int(self.value, 10), NumericSystem.oct[0])
        if self.numericSystem[0] == NumericSystem.bin[0]:
            return format(
                int(self.value, 2), NumericSystem.oct[0])
        else:
            raise Exception("Unknown numericSystem!")

    def castValue(self, newNumericSystem):
        if newNumericSystem == NumericSystem.dec[0]:
            return self.decimalRepresentation()
        elif newNumericSystem == NumericSystem.oct[0]:
            return self.octRepresentation()
        elif newNumericSystem == NumericSystem.hex[0]:
            return self.hexRepresentation()
        elif newNumericSystem == NumericSystem.bin[0]:
            return self.binaryRepresentation()
