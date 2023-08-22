from quantum.gates import MultiQubitGate
from quantum.operations import Operations
from quantum.errors import Errors
from quantum.qubit import Qubit, generate_qubits_sequence

operations = Operations()
errors = Errors()


class Circuit:
    def __init__(self, total_of_qubits):
        assert total_of_qubits >= 1, errors.invalid_total_of_qubits()
        self.qubits = generate_qubits_sequence(total_of_qubits)

    def add_single_qubit_gate(self, gate, qubit):
        self.valid_qubit(qubit)
        selected_qubit = self.qubits[qubit]
        selected_qubit.set_state(gate().apply(selected_qubit.get_state()))

    def valid_qubit(self, qubit):
        assert (qubit >= 0 and qubit < len(self.qubits)
                ), errors.selected_qubit_out_of_bound()

    def valid_qubits(self, qubits):
        for qubit in qubits:
            self.valid_qubit(qubit)

    def add_multi_qubit_gate(self, gate, qubits):
        self.valid_qubits(qubits)
        gate = gate()
        assert isinstance(gate, MultiQubitGate), errors.multi_qubit_gate()
        assert gate.gate_total_qubits == len(
            qubits), errors.missing_qubits()

        selected_qubits = [self.qubits[qubit] for qubit in qubits]
        selected_qubits_states = [selected_qubit.get_state()
                                  for selected_qubit in selected_qubits]
        tensor_state = self.apply_tensor_product(selected_qubits_states)
        gate.apply(tensor_state)

    def apply_tensor_product(self, states):
        final_state = states[0]
        for state in states[1:]:
            final_state = operations.tensor_product(final_state, state)
        return final_state

    def get_qubits_states(self):
        return [qubit.get_state() for qubit in self.qubits]

    def get_circuit_state(self):
        qubits_states = self.get_qubits_states()
        circuit_state = self.apply_tensor_product(qubits_states)
        return circuit_state