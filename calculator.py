class Datatype:
    byte = '8'
    word = '16'
    dword = '32'
    qword = '64'


class NumericSystem:
    bin = 'b'
    dec = 'd'
    hex = 'X'
    oct = 'o'


class Operations:
    add = 'add'
    sub = 'sub'
    mul = 'mul'
    div = 'div'


class Calculator:

    def __init__(self):
        self._value = '0'
        self._numericSystem = NumericSystem.dec
        self._dataType = Datatype.qword
        self._binaryValue = 64 * '0'
        self._operation = ''

    @property
    def operation(self):
        return self._operation

    @operation.setter
    def operation(self, value):
        self._operation = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value

    @property
    def binaryValue(self):
        return self._binaryValue

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
            self.value = self.castValue(newNumericSystem)
            self._numericSystem = newNumericSystem

    def input(self, character):
        if self.numericSystem == NumericSystem.bin:
            self.binInput(character)
        elif self.numericSystem == NumericSystem.oct:
            self.octInput(character)
        elif self.numericSystem == NumericSystem.dec:
            self.decInput(character)
        elif self.numericSystem == NumericSystem.hex:
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

    def hexInput(self, character):
        if character in "0123456789ABCDEF":
            if self.value == '0':
                self.value = character
            else:
                self.value += character
        if character in "+-*/=!()":
            self.operation = character

    #         self.evaluateOperation(character)

    # def evaluateOperation(self, character):
    #     if character == '+':
    #         pass
    #     if character == '-':
    #         pass
    #     if character == '*':
    #         pass
    #     if character == '/':
    #         pass
    #     if character == '=':
    #         pass
    #     if character == '!':
    #         self.changeSign()

    def decimalRepresentation(self):
        if self.numericSystem == NumericSystem.bin:
            return str(int(self.value, 2))
        else:
            raise Exception("Unknown numericSystem!")

    def binaryRepresentation(self):
        if self.numericSystem == NumericSystem.bin:
            return format(
                int(self.value, 2), NumericSystem.bin)
        if self.numericSystem == NumericSystem.hex:
            return format(
                int(self.value, 16), NumericSystem.bin)
        if self.numericSystem == NumericSystem.dec:
            return format(
                int(self.value, 10), NumericSystem.bin)
        else:
            raise Exception("Unknown numericSystem!")

    def hexRepresentation(self):
        if self.numericSystem == NumericSystem.bin:
            return format(
                int(self.value, 2), NumericSystem.hex)
        if self.numericSystem == NumericSystem.dec:
            return format(
                int(self.value, 10), NumericSystem.hex)
        else:
            raise Exception("Unknown numericSystem!")

    def octRepresentation(self):
        if self.numericSystem == NumericSystem.bin:
            return format(
                int(self.value, 2), NumericSystem.oct)
        if self.numericSystem == NumericSystem.dec:
            return format(
                int(self.value, 10), NumericSystem.oct)
        else:
            raise Exception("Unknown numericSystem!")

    def castValue(self, newNumericSystem):
        if newNumericSystem == NumericSystem.dec:
            return self.decimalRepresentation()
        elif newNumericSystem == NumericSystem.oct:
            return self.octRepresentation()
        elif newNumericSystem == NumericSystem.hex:
            return self.hexRepresentation()
        elif newNumericSystem == NumericSystem.bin:
            return self.binaryRepresentation()
