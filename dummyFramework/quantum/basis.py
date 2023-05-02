from quantum.operations import Operations

operations = Operations()

class Basis:
    basis_vector = None
    basis_symbol = None
    
    def get_basis_vector(self):
        return self.basis_vector
    
    def get_basis_symbol(self):
        return self.basis_symbol

class Zero(Basis):
    def __init__(self):
        self.basis_vector = operations.create_vector([[1], [0]])
        self.basis_symbol = '|0⟩'

class One(Basis):
    def __init__(self):
        self.basis_vector = operations.create_vector([[0], [1]])
        self.basis_symbol = '|1⟩'

class Plus(Basis):
    def __init__(self):
        self.basis_vector = operations.create_vector([[1/operations.square_root(2)], [1/operations.square_root(2)]])
        self.basis_symbol = '|+⟩'

class Minus(Basis):
    def __init__(self):
        self.basis_vector = operations.create_vector([[1/operations.square_root(2)], [-1/operations.square_root(2)]])
        self.basis_symbol = '|-⟩'

class Plus_i(Basis):
    def __init__(self):
        self.basis_vector = operations.create_vector([[0], [1j]])
        self.basis_symbol = '|i⟩'

class Minus_i(Basis):
    def __init__(self):
        self.basis_vector = operations.create_vector([[-1j], [0]])
        self.basis_symbol = '|-i⟩'
