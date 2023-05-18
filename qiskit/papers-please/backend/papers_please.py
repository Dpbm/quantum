from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister, Aer

class PapersPlease:
    def __init__(self):
        self.accept = QuantumRegister(1, name="accept")
        self.detain = QuantumRegister(1, name="detain")
        self.justify = QuantumRegister(1, name="justify")
        self.bribe = QuantumRegister(1, name="bribe")
        self.false_info = QuantumRegister(1, name="false_info")
        self.wanted = QuantumRegister(1, name="wanted")
        self.passport = QuantumRegister(1, name="passport")
        self.other_documents = QuantumRegister(1, name="documents")
        self.ancilla = QuantumRegister(2, name="ancilla")
        self.measure = ClassicalRegister(3, name="out")

        self.qc = self.init_qubits()
        self.sim = Aer.get_backend('aer_simulator') 
    
    def init_qubits(self):
        return QuantumCircuit(self.accept, self.detain, self.justify, self.ancilla, self.passport, self.other_documents, self.bribe, self.wanted, self.false_info, self.measure)

    def create_circuit(self, bribe=0, false_info=0, wanted=0, passport=0, other_documents=0):
        self.add_inputs(bribe, false_info, wanted, passport, other_documents)
        self.add_barrier()
        self.set_accept()
        self.add_barrier()
        self.set_justify()
        self.add_barrier()
        self.set_detain()
        self.add_barrier()
        self.add_measurement()

    def add_inputs(self, bribe, false_info, wanted, passport, other_documents):
        if(bribe):
            self.qc.x(self.bribe)
        if(false_info):
            self.qc.x(self.false_info)
        if(wanted):
            self.qc.x(self.wanted)
        if(passport):
            self.qc.x(self.passport)
        if(other_documents):
            self.qc.x(self.other_documents)

    def add_barrier(self):
        self.qc.barrier()

    def set_accept(self):
        self.qc.x(self.accept)
        self.qc.x(self.bribe)
        self.qc.x(self.passport)
        self.qc.ccx(self.bribe, self.passport, self.accept)
        self.qc.x(self.passport)

    def set_justify(self):
        self.qc.x(self.ancilla[-1])
        self.qc.x(self.ancilla[-2])
        self.qc.x(self.false_info)
        self.qc.ccx(self.false_info, self.other_documents, self.ancilla[-1])
        self.qc.x(self.ancilla[-1])
        self.qc.ccx(self.passport, self.ancilla[-1], self.ancilla[-2])
        self.qc.cx(self.ancilla[-2], self.justify)
        self.qc.ccx(self.passport, self.ancilla[-1], self.ancilla[-2])
        self.qc.x(self.ancilla[-1])
        self.qc.ccx(self.false_info, self.other_documents, self.ancilla[-1])
        self.qc.x(self.ancilla[-1])
        self.qc.x(self.ancilla[-2])

    def set_detain(self):
        self.qc.x(self.wanted)
        self.qc.x(self.ancilla[-1])
        self.qc.x(self.ancilla[-2])
        self.qc.ccx(self.false_info, self.wanted, self.ancilla[-1])
        self.qc.x(self.ancilla[-1])
        self.qc.ccx(self.bribe, self.ancilla[-1], self.ancilla[-2])
        self.qc.cx(self.ancilla[-2], self.detain)
        self.qc.ccx(self.bribe, self.ancilla[-1], self.ancilla[-2])
        self.qc.x(self.ancilla[-1])
        self.qc.ccx(self.false_info, self.wanted, self.ancilla[-1])
        self.qc.x(self.false_info)
        self.qc.x(self.wanted)
        self.qc.x(self.bribe)
        self.qc.x(self.ancilla[-1])
        self.qc.x(self.ancilla[-2])

    def add_measurement(self):
        self.qc.measure(self.accept, self.measure[0])
        self.qc.measure(self.detain, self.measure[1])
        self.qc.measure(self.justify, self.measure[2])

    def save_circuit_image(self):
        self.qc.draw(output="mpl", filename='static/circuit.png')

    def get_states(self):
        results = self.sim.run(self.qc).result().get_counts()
        bit_string = list(results.keys())[0]
        return {
            "accept": bit_string[-1],
            "detain": bit_string[-2],
            "justify": bit_string[-3],
        }