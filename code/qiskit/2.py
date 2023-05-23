from qiskit import QuantumCircuit
from qiskit.providers.aer import AerSimulator

qc = QuantumCircuit(3, 3)

# this is relative to NOT gate
# this X gate will be use in the 0 and 1 qubit
qc.x([0,1])

qc.measure([0, 1, 2], [0, 1, 2])
print(qc)

sim = AerSimulator()
job = sim.run(qc)
result = job.result()
print(result.get_counts())
