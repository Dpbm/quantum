from quantum.operations import Operations
from quantum.basis import Zero
from quantum.errors import Errors
from quantum.patterns import little_endian

operations = Operations()
errors = Errors()

class Circuit:
    def __init__(self, total_of_qubits, sequene_pattern=little_endian):
        if(not self.valid_total_of_qubits(total_of_qubits)):
            errors.invalid_total_of_qubits()

        self.total_of_qubits = total_of_qubits
        self.qubits_sequence_pattern = sequene_pattern(total_of_qubits) 
        self.gates_sequence = self.initialize_gates_sequence()
        self.states = self.initialize_gates_states()

    def valid_total_of_qubits(self, total_of_qubits):
        return total_of_qubits >= 1

    def initialize_gates_sequence(self):
        return [f'Q{qubit}: {Zero().get_basis_symbol()}' for qubit in range(self.total_of_qubits)]
    
    def initialize_gates_states(self):
        return operations.create_vector([Zero().get_basis_vector() for _ in range(self.total_of_qubits)])
    
    def add_single_qubit_gate(self, gate, qubit):
        if(not self.qubit_exists(qubit)): 
            errors.selected_qubit_out_of_bound()
 
        self.apply_gate_vector_to_the_qubit(gate().get_gate_vector(), qubit)
        self.add_gate_symbol_to_the_list(gate().get_gate_symbol(), qubit)
    
    def qubit_exists(self, selected_qubit):
        return selected_qubit >= 0 and selected_qubit < self.total_of_qubits

    def apply_gate_vector_to_the_qubit(self, gate_vector, qubit):
        qubit_state = self.states[qubit]
        self.states[qubit] = operations.dot(gate_vector, qubit_state)
    
    def add_gate_symbol_to_the_list(self, gate_symbol, qubit):
        self.gates_sequence[qubit] += f" {gate_symbol}"

    def get_states(self):
        return self.states
    
    def get_qubit_states_list(self):
        final_state = None
        
        for state_index in self.qubits_sequence_pattern:
            qubit_state = self.states[state_index]
            
            if(final_state is None):
                final_state = qubit_state
                continue

            final_state = operations.tensor_product(final_state, qubit_state)
    
        return final_state
        


    def show_circuit(self):
        for qubit_gates_list in self.gates_sequence:
            print(qubit_gates_list)

    def show_states(self):
        for qubit, qubit_state in enumerate(self.states):
            print(f'Q{qubit}: {qubit_state}')
