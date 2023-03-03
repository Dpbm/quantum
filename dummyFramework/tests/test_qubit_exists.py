import pytest
from quantum.circuit import Circuit

def test_function_qubit_exists_test_that_qubit_exists():
    circuit = Circuit(10)
    selected_qubit = 3
    assert circuit.qubit_exists(selected_qubit) == True

def test_function_qubits_exists_test_that_qubit_does_not_exists_by_upper_bound():
    circuit = Circuit(3)
    selected_qubit = 4
    assert circuit.qubit_exists(selected_qubit) == False


def test_function_qubits_exists_test_that_qubit_does_not_exists_by_lower_bound():
    circuit = Circuit(3)
    selected_qubit = -1
    assert circuit.qubit_exists(selected_qubit) == False


def test_function_qubits_exists_test_that_qubit_exists_by_zero():
    circuit = Circuit(1)
    selected_qubit = 0
    assert circuit.qubit_exists(selected_qubit) == True


def test_function_qubits_exists_test_that_qubit_doesnt_exists_by_zero_total_qubits_raises_error():
    with pytest.raises(ValueError):
        circuit = Circuit(0)

