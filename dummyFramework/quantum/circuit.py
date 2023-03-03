from quantum.operations import Operations
from quantum.basis import zero as zero_basis
from quantum.errors import Errors

operations = Operations()
errors = Errors()



class Circuit:
    def __init__(self, total_of_qubits):
        if(not self.valid_total_of_qubits(total_of_qubits)):
            errors.invalid_total_of_qubits()

        self.total_of_qubits = total_of_qubits
        self.gates_sequence = self.initialize_gates_sequence()
        self.states = self.initialize_gates_states()

    def valid_total_of_qubits(self, total_of_qubits):
        return total_of_qubits >= 1

    def initialize_gates_sequence(self):
        zero_basis_symbol = zero_basis["symbol"]
        return [f'Q{qubit}: {zero_basis_symbol}' for qubit in range(self.total_of_qubits)]
    
    def initialize_gates_states(self):
        zero_basis_vector = zero_basis["vector"]
        return operations.create_vector([zero_basis_vector for _ in range(self.total_of_qubits)])
    
    def add_single_qubit_gate(self, gate, qubit):
        if(not self.qubit_exists(qubit)): 
            errors.selected_qubit_out_of_bound()

        gate_vector = gate["vector"]
        gate_symbol = gate["symbol"]
    
        self.apply_gate_vector_to_the_qubit(gate_vector, qubit)
        self.add_gate_symbol_to_the_list(gate_symbol, qubit)
    
    def qubit_exists(self, selected_qubit):
        return selected_qubit >= 0 and selected_qubit < self.total_of_qubits


    def apply_gate_vector_to_the_qubit(self, gate_vector, qubit):
        qubit_state = self.states[qubit]
        self.states[qubit] = operations.dot(gate_vector, qubit_state)
    
    def add_gate_symbol_to_the_list(self, gate_symbol, qubit):
        self.gates_sequence[qubit] += f" {gate_symbol}"

    def show_circuit(self):
        for qubit_gates_list in self.gates_sequence:
            print(qubit_gates_list)

    def show_states(self):
        for qubit, qubit_state in enumerate(self.states):
            print(f'Q{qubit}: {qubit_state}')
