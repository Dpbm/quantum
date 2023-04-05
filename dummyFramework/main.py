from quantum.circuit import Circuit
from quantum.gates import X, H, Z, I

circuit = Circuit(total_of_qubits=1)
circuit.add_single_qubit_gate(I, 0)
#circuit.add_single_qubit_gate(Z, 3)
print(circuit.get_states())

#circuit.show_circuit()
#circuit.show_states()
