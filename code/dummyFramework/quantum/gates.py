from quantum.operations import Operations

operations = Operations()


class BaseGate:
    gate_vector = None
    gate_symbol = None
    gate_total_qubits = None

    def apply(self, state):
        return operations.dot(self.gate_vector, state)


class SingleQubitGate(BaseGate):
	gate_total_qubits = 1


class MultiQubitGate(BaseGate):
	gate_total_qubits = 2


class X(SingleQubitGate):
    def __init__(self):
        self.gate_vector = operations.create_vector([[0, 1], [1, 0]])
        self.gate_symbol = 'X'


class Z(SingleQubitGate):
    def __init__(self):
        self.gate_vector = operations.create_vector([[1, 0], [0, -1]])
        self.gate_symbol = 'Z'


class H(SingleQubitGate):
    def __init__(self):
        one_by_two_square_root = 1/operations.square_root(2)
        self.gate_vector = operations.create_vector([[one_by_two_square_root, one_by_two_square_root], [
                                                    one_by_two_square_root, -one_by_two_square_root]])
        self.gate_symbol = 'H'


class I(SingleQubitGate):
    def __init__(self):
        self.gate_vector = operations.create_vector([[1, 0], [0, 1]])
        self.gate_symbol = 'I'


class S(SingleQubitGate):
    def __init__(self):
        self.gate_vector = operations.create_vector([[1, 0], [0, 1j]])
        self.gate_symbol = 'S'


class T(SingleQubitGate):
    def __init__(self):
        self.gate_vector = operations.create_vector(
            [[1, 0], [0, operations.power(operations.euler(), (1j*operations.pi()) / 4)]])
        self.gate_symbol = 'T'


class CNOT(MultiQubitGate):
    def __init__(self):
        self.gate_vector = operations.create_vector(
            [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0]])
        self.gate_symbol = 'CX'