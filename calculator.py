class Datatype:
    byte  = '8'
    word  = '16'
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
        self._numericSystem = NumericSystem.bin
        self._dataType = Datatype.qword

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value

    @property
    def binaryValue(self):
        return self.binaryRepresentation()

    @property
    def octValue(self):
        return self.octRepresentation()

    @property
    def hexValue(self):
        return self.hexRepresentation()

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
            return # do nothing
        else:
            self.value = self.castValue(newNumericSystem)
            self._numericSystem = newNumericSystem

    def input(self, character):
        if self.numericSystem == NumericSystem.bin:
            self.binInput(character)

    def binInput(self, character):
        if character in "01":
            if self.value == '0':
                self.value = character
            else:   
                self.value += character        

    def decimalRepresentation(self):
        if self.numericSystem == NumericSystem.bin:
            return str(int(self.value, 2))

    def binaryRepresentation(self):
        if self.numericSystem == NumericSystem.bin:
            return format(
                int(self.value, 2), '0' + self.dataType + NumericSystem.bin)
    
    def hexRepresentation(self):
        if self.numericSystem == NumericSystem.bin:
            return format(
                int(self.value, 2), NumericSystem.hex)

    def octRepresentation(self):
        if self.numericSystem == NumericSystem.bin:
            return format(
                int(self.value, 2), NumericSystem.oct)

    def castValue(self, newNumericSystem):
        if newNumericSystem == NumericSystem.dec:
            return self.decimalRepresentation()
        elif newNumericSystem == NumericSystem.oct:
            return self.octRepresentation()