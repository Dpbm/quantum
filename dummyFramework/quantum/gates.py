from quantum.operations import Operations

operations = Operations()

class Gate:
    gate_vector = None
    gate_symbol = None

    def get_gate_vector(self):
        return self.gate_vector

    def get_gate_symbol(self):
        return self.gate_symbol

    def apply(self, state):
        return operations.dot(self.gate_vector, state)

class X(Gate):
    def __init__(self):
        self.gate_vector = operations.create_vector([[0, 1], [1, 0]])
        self.gate_symbol = 'X'


class Z(Gate):
    def __init__(self):
        self.gate_vector = operations.create_vector([[1, 0], [0, -1]])
        self.gate_symbol = 'Z'

class H(Gate):
    def __init__(self):
        one_by_two_square_root = 1/operations.square_root(2)
        self.gate_vector = operations.create_vector([[one_by_two_square_root, one_by_two_square_root], [one_by_two_square_root, -one_by_two_square_root]])
        self.gate_symbol = 'H'

class I(Gate):
    def __init__(self):
        self.gate_vector = operations.create_vector([[1, 0], [0, 1]])
        self.gate_symbol = 'I'

class S(Gate):
    def __init__(self):
        self.gate_vector = operations.create_vector([[1, 0], [0, 1j]])
        self.gate_symbol = 'S'

class T(Gate):
    def __init__(self):
        self.gate_vector = operations.create_vector([[1, 0], [0, operations.power(operations.euler(), (1j*operations.pi()) / 4)]])
