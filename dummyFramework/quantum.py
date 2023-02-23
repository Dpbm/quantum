import numpy

class Basis:
    zero = numpy.array([[1], [0]])
    one = numpy.array([[0], [1]])
    
class Gates:
    x = numpy.array([[0, 1], [1, 0]])

class Circuit:
    def __init__(self, n_qubits, n_bits):
        self.n_qubits = n_qubits
        self.states = numpy.array([n_qubits * Basis.zero])

    def set_initial_state(self, state, qubit):
        assert qubit >= 0 and qubit < self.n_qubits
        
        self.states[qubit] = state

    def add_single_qubit_gate(self, gate, qubit):
        qubit_state = self.states[qubit]
        self.states[qubit] = numpy.dot(gate, qubit_state)

    def show_circuit(self):
        print(self.states)

