from quantum.gates import I, X
from quantum.basis import zero, one
from quantum.circuit import Circuit


def test_identity_after_zero():
    circuit = Circuit(1)
    circuit.add_single_qubit_gate(I, 0)
    assert (circuit.get_states() == zero["vector"]).all()

def test_identity_after_one():
    circuit = Circuit(1)
    circuit.add_single_qubit_gate(X, 0)
    circuit.add_single_qubit_gate(I, 0)
    assert (circuit.get_states() == one["vector"]).all()

