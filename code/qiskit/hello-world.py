from qiskit import QuantumCircuit
from qiskit.providers.aer import AerSimulator


# 3 qubits 3 classical bits
qc = QuantumCircuit(3, 3)
# measure the three qubits and put the info inside the three classical bits
qc.measure([0, 1, 2], [0, 1, 2])

print(qc)

sim = AerSimulator()
job = sim.run(qc)
result = job.result()
# how the default values to qubits are 0, and we didn't change anything, so the results are always 0
print(result.get_counts())



