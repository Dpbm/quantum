from quantum.circuit import Circuit
from quantum.gates import S, H, T

circuit = Circuit(total_of_qubits=1)

circuit.add_single_qubit_gate(S, 0)
circuit.add_single_qubit_gate(H, 0)
circuit.add_single_qubit_gate(S, 0)
circuit.add_single_qubit_gate(T, 0)

print(circuit.get_circuit_state())
print(circuit.get_qubits_states())
