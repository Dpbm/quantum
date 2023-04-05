from quantum.circuit import Circuit
from quantum.gates import X, H, Z, I
from quantum.patterns import big_endian

circuit = Circuit(total_of_qubits=2, sequene_pattern=big_endian)

circuit.add_single_qubit_gate(X, 0)
#circuit.add_single_qubit_gate(Z, 3)
print(circuit.get_qubit_states_list())

circuit.show_circuit()
#circuit.show_states()
