from quantum.circuit import Circuit
from quantum.gates import X
from quantum.basis import One, Zero

def test_x_gate_with_zero():
    circuit = Circuit(1)
    circuit.add_single_qubit_gate(X, 0)
    assert (circuit.get_qubits_states()[0] == One().get_basis_vector()).all()

def test_x_gate_with_one():
    circuit = Circuit(1)
    circuit.add_single_qubit_gate(X, 0)
    circuit.add_single_qubit_gate(X, 0)
    assert (circuit.get_qubits_states()[0] == Zero().get_basis_vector()).all()
