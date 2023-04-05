from quantum.circuit import Circuit
from quantum.gates import X
from quantum.operations import Operations
from quantum.patterns import big_endian, little_endian

operations = Operations()

def test_little_endian():
    circuit = Circuit(2, little_endian)
    circuit.add_single_qubit_gate(X, 0)
    
    expected_result = operations.create_vector([[0], [1], [0], [0]])

    assert (circuit.get_qubit_states_list() == expected_result).all()

def test_big_endian():
    circuit = Circuit(2, big_endian)
    circuit.add_single_qubit_gate(X, 0)

    expected_result = operations.create_vector([[0], [0], [1], [0]])

    assert (circuit.get_qubit_states_list() == expected_result).all()

