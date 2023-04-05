def little_endian(qubits):
    return range(qubits-1, -1, -1)

def big_endian(qubits):
    return range(qubits)
