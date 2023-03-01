from quantum.circuit import Circuit
from quantum.gates import X, H, Z

circuit = Circuit(total_of_qubits=1)
circuit.add_single_qubit_gate(H, 0)
circuit.add_single_qubit_gate(Z, 0)



circuit.show_circuit()
circuit.show_states()
