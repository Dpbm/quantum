from quantum.circuit import Circuit
from quantum.gates import X, H, Z, I

circuit = Circuit(total_of_qubits=2)

circuit.add_single_qubit_gate(X, 0)
print(circuit.get_circuit_state())
print(circuit.get_qubits_states())
