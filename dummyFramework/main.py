from quantum.circuit import Circuit
from quantum.gates import X, H

circuit = Circuit(total_of_qubits=2)
circuit.add_single_qubit_gate(X, 0)
circuit.add_single_qubit_gate(H, 0)
#circuit.add_single_qubit_gate(X, 0)
circuit.add_single_qubit_gate(H, 0)


circuit.add_single_qubit_gate(X, 1)

circuit.show_circuit()
circuit.show_states()
