from qiskit import QuantumCircuit
from qiskit.providers.aer import AerSimulator

qc = QuantumCircuit(1,1)
# the H-gate (Hadamard gate) is a gate that put a qubit in superposition, given it 50% to be 1 and 50% to be 0
qc.h(0)
qc.measure([0], [0])
print(qc)

sim = AerSimulator()
job = sim.run(qc)
result = job.result()
print(result.get_counts())
