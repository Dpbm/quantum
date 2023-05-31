from qiskit import QuantumCircuit
from qiskit.providers.aer import AerSimulator

sim = AerSimulator()
qc = QuantumCircuit(2, 2)

qc.cx(0, 1)
qc.measure([0,1], [0,1])
print(qc)


job = sim.run(qc)
result = job.result()
print(result.get_counts())


qc2 = QuantumCircuit(2,2)
qc2.x(0)
qc2.cx(0, 1)
qc2.measure([0,1], [0,1])
print(qc2)

job2 = sim.run(qc2)
result2 = job2.result()
print(result2.get_counts())

qc3 = QuantumCircuit(2,2)
qc3.x(1)
qc3.cx(0, 1)
qc3.measure([0,1], [0,1])
print(qc3)

job3 = sim.run(qc3)
result3 = job3.result()
print(result3.get_counts())

qc4 = QuantumCircuit(2,2)
qc4.x(0)
qc4.x(1)
qc4.cx(0, 1)
qc4.measure([0,1],[0,1])
print(qc4)

job4 = sim.run(qc4)
result4 = job4.result()
print(result4.get_counts())

# the CNOT (CX) acts like a XOR gate
# the circle is named as control, and the circle with a X in the middle is the target
# the CNOT flips the target qubit if the control is 1
# https://en.wikipedia.org/wiki/Controlled_NOT_gate
