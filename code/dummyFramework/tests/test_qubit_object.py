from quantum.qubit import Qubit, generate_qubits_sequence
from quantum.basis import Zero

def test_one_qubit_definition():
    qubit = Qubit(name='q0')
    assert(qubit.get_state() == Zero().get_basis_vector()).all()

def test_multiple_qubits_definition():
    qubits = generate_qubits_sequence(2)    
    assert(qubits[0].get_state() == Zero().get_basis_vector()).all()
    assert(qubits[1].get_state() == Zero().get_basis_vector()).all()
