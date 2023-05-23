class Errors:
    def __init__(self):
        pass

    def selected_qubit_out_of_bound(self):
        raise ValueError("Selected qubit out of bound")

    def invalid_total_of_qubits(self):
        raise ValueError("You need to have at least, 1 qubit")

    def missing_qubits(self):
        raise ValueError("You need to provide the correct number of qubits")
