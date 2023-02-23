from quantum import Circuit, Basis, Gates

circuit = Circuit(1, 1)
circuit.set_initial_state(Basis.one, 0)
circuit.show_circuit()
circuit.add_single_qubit_gate(Gates.x, 0)
circuit.show_circuit()

