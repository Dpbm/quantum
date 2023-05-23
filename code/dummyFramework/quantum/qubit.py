from quantum.basis import Zero

def generate_qubits_sequence(n):
    return [ Qubit(name=f'q{i}') for i in range(n) ]

class Qubit:
    def __init__(self, name, state=Zero().get_basis_vector()):
        self.state = state
        self.name = str(name)

    def get_state(self):
        return self.state

    def set_state(self, new_state):
        self.state = new_state
