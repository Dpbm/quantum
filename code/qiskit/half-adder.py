from qiskit import QuantumCircuit
from qiskit.providers.aer import AerSimulator

sim = AerSimulator()
qc = QuantumCircuit(4, 2)

# inputs
qc.x(0)
qc.x(1)

# the sum part
qc.cx(0, 2)
qc.cx(1, 2)
qc.measure([2], [0])
print(qc)


# carry part
# this is a Toffoli gate, if all the first two bits are 1 the target will be flipped
qc.ccx(0, 1, 3)
qc.measure([3], [1])
print(qc)

job = sim.run(qc)
result = job.result()
print(result.get_counts())
