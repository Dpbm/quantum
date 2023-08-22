from quantum.circuit import Circuit
from quantum.gates import S, H, T, CNOT

circuit = Circuit(total_of_qubits=2)

#circuit.add_single_qubit_gate(S, 0)
circuit.add_single_qubit_gate(H, 0)
circuit.add_multi_qubit_gate(CNOT, [0,1])
#circuit.add_single_qubit_gate(S, 0)
#circuit.add_single_qubit_gate(T, 0)

print(circuit.get_circuit_state())
