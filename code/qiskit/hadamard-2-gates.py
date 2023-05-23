from qiskit import QuantumCircuit
from qiskit.providers.aer import AerSimulator

sim = AerSimulator()

qc = QuantumCircuit(1,1)
qc.h(0)
qc.h(0)
qc.measure([0], [0])
print(qc)

job = sim.run(qc)
result = job.result()
print(result.get_counts())

qc2 = QuantumCircuit(1,1)
qc2.x(0)
qc2.h(0)
qc2.h(0)
qc2.measure([0], [0])
print(qc2)

job2 = sim.run(qc2)
result2 = job2.result()
print(result2.get_counts())

# Using in sequence two Hadamard gates the cancel each other
