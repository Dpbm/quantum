from quantum.operations import Operations
from quantum.errors import Errors
from quantum.qubit import generate_qubits_sequence

operations = Operations()
errors = Errors()

class Circuit:
    def __init__(self, total_of_qubits):
        assert total_of_qubits >= 1, errors.invalid_total_of_qubits() 
        self.qubits = generate_qubits_sequence(total_of_qubits)
        
    def add_single_qubit_gate(self, gate, qubit):
        assert (qubit >= 0 and qubit < len(self.qubits)), errors.selected_qubit_out_of_bound()
        selected_qubit = self.qubits[qubit]
        selected_qubit.set_state(gate().apply(selected_qubit.get_state()))
    
    def get_qubits_states(self):
        return [ qubit.get_state() for qubit in self.qubits ]
    
    def get_circuit_state(self):
        qubits_states = self.get_qubits_states()
        circuit_state = qubits_states[0]
        for qubit_state in qubits_states[1:]:
            circuit_state = operations.tensor_product(circuit_state, qubit_state)
        return circuit_state
        


