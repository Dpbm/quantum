from collections import OrderedDict
from qiskit import QuantumRegister, ClassicalRegister
import pprint
from qiskit.circuit.parameter import Parameter

_QASM2_FIXED_PARAMETERS = [Parameter("param0"), Parameter("param1"), Parameter("param2")]

def _qasm2_define_custom_operation(operation, existing_gate_names, gates_to_define):
    from qiskit.circuit import library as lib  # pylint: disable=cyclic-import

    
    
    if operation.name in existing_gate_names:
        return operation
    print(f'operation: {operation}', end='\n')
    print("existing_gate_names: does'nt exists!", end="\n")
        
    # Check instructions names or label are valid
    escaped = _qasm_escape_name(operation.name, "gate_")
    if escaped != operation.name:
        operation = operation.copy(name=escaped)
    print(f'new name: {escaped}', end="\n")

    # These are built-in gates that are known to be safe to construct by passing the correct number
    # of `Parameter` instances positionally, and have no other information.  We can't guarantee that
    # if they've been subclassed, though.  This is a total hack; ideally we'd be able to inspect the
    # "calling" signatures of Qiskit `Gate` objects to know whether they're safe to re-parameterise.
    known_good_parameterized = {
        lib.PhaseGate,
        lib.RGate,
        lib.RXGate,
        lib.RXXGate,
        lib.RYGate,
        lib.RYYGate,
        lib.RZGate,
        lib.RZXGate,
        lib.RZZGate,
        lib.XXMinusYYGate,
        lib.XXPlusYYGate,
        lib.UGate,
        lib.U1Gate,
        lib.U2Gate,
        lib.U3Gate,
    }

    # In known-good situations we want to use a manually parametrised object as the source of the
    # definition, but still continue to return the given object as the call-site object.
    if type(operation) in known_good_parameterized:
        print('known_good_parameterized: is parameterized', end="\n")
        parameterized_operation = type(operation)(*_QASM2_FIXED_PARAMETERS[: len(operation.params)])
    elif hasattr(operation, "_qasm2_decomposition"):
        print('has _qasm2_decomposition: has!!', end="\n")
        new_op = operation._qasm2_decomposition()
        parameterized_operation = operation = new_op.copy(
            name=_qasm_escape_name(new_op.name, "gate_")
        )
    else:
        parameterized_operation = operation

    # If there's an _equal_ operation in the existing circuits to be defined, then our job is done.
    previous_definition_source, _ = gates_to_define.get(operation.name, (None, None))
    if parameterized_operation == previous_definition_source:
        print('same as previous: yes!', end="\n\n")
        return operation
        
    # Otherwise, if there's a naming clash, we need a unique name.
    if operation.name in gates_to_define:
        new_name = f"{operation.name}_{id(operation)}"
        print(f'in gates_to_define: yes',end="\n")
        print(f'new name: {new_name}', end="\n")
        operation = operation.copy(name=new_name)
    else:
        new_name = operation.name

    if parameterized_operation.params:
        parameters_qasm = (
            "(" + ",".join(f"param{i}" for i in range(len(parameterized_operation.params))) + ")"
        )
        print(f'parameters: {parameters_qasm}', end="\n")
    else:
        parameters_qasm = ""

    
    qubits_qasm = ",".join(f"q{i}" for i in range(parameterized_operation.num_qubits))
    print(f"qubits: {qubits_qasm}", end="\n")
    
    parameterized_definition = getattr(parameterized_operation, "definition", None)
    if parameterized_definition is None:
        print("no parameterized_definition: yes")
        gates_to_define[new_name] = (
            parameterized_operation,
            f"opaque {new_name}{parameters_qasm} {qubits_qasm};",
        )
    else:
        statements = []
        qubit_labels = {bit: f"q{i}" for i, bit in enumerate(parameterized_definition.qubits)}
        for instruction in parameterized_definition.data:
            
            new_operation = _qasm2_define_custom_operation(
                instruction.operation, existing_gate_names, gates_to_define
            )
            print(f'new_operation: {new_operation}', end='\n')
            bits_qasm = ",".join(qubit_labels[q] for q in instruction.qubits)
            print(f'bits_qasm: {bits_qasm}', end='\n')
            statements.append(f"{new_operation.qasm()} {bits_qasm};")
        body_qasm = " ".join(statements)
        definition_qasm = f"gate {new_name}{parameters_qasm} {qubits_qasm} {{ {body_qasm} }}"
        print(f'definition_qasm: {definition_qasm}')
        gates_to_define[new_name] = (parameterized_operation, definition_qasm)
    print('\n\ngates_to_define: ', end='')
    pprint.pprint(gates_to_define)
    print('\n\n\n\n')
    return operation


def qasm(qc, formatted=False, filename=None, encoding=None):

        existing_gate_names = {
            "barrier",
            "measure",
            "reset",
            "u3",
            "u2",
            "u1",
            "cx",
            "id",
            "u0",
            "u",
            "p",
            "x",
            "y",
            "z",
            "h",
            "s",
            "sdg",
            "t",
            "tdg",
            "rx",
            "ry",
            "rz",
            "sx",
            "sxdg",
            "cz",
            "cy",
            "swap",
            "ch",
            "ccx",
            "cswap",
            "crx",
            "cry",
            "crz",
            "cu1",
            "cp",
            "cu3",
            "csx",
            "cu",
            "rxx",
            "rzz",
            "rccx",
            "rc3x",
            "c3x",
            "c3sx",  # This is the Qiskit gate name, but the qelib1.inc name is 'c3sqrtx'.
            "c4x",
        }

        gates_to_define = OrderedDict()

        regless_qubits = [bit for bit in qc.qubits if not qc.find_bit(bit).registers]
        regless_clbits = [bit for bit in qc.clbits if not qc.find_bit(bit).registers]
    
        dummy_registers = []
        if regless_qubits:
            dummy_registers.append(QuantumRegister(name="qregless", bits=regless_qubits))
        if regless_clbits:
            dummy_registers.append(ClassicalRegister(name="cregless", bits=regless_clbits))
        register_escaped_names = {}
    
        for regs in (qc.qregs, qc.cregs, dummy_registers):
            for reg in regs:
                register_escaped_names[
                    _make_unique(_qasm_escape_name(reg.name, "reg_"), register_escaped_names)
                ] = reg
                
        bit_labels = {
            bit: "%s[%d]" % (name, idx)
            for name, register in register_escaped_names.items()
            for (idx, bit) in enumerate(register)
        }
    
        register_definitions_qasm = "".join(
            f"{'qreg' if isinstance(reg, QuantumRegister) else 'creg'} {name}[{reg.size}];\n"
            for name, reg in register_escaped_names.items()
        )
    
        instruction_calls = []

        print('operations: ', end=' ')
        pprint.pprint([instruction.operation for instruction in qc._data])
        print('\n\n')
    
        for instruction in qc._data:
            operation = instruction.operation
            if operation.name == "measure":
                qubit = instruction.qubits[0]
                clbit = instruction.clbits[0]
                instruction_qasm = f"measure {bit_labels[qubit]} -> {bit_labels[clbit]};"
            elif operation.name == "reset":
                instruction_qasm = f"reset {bit_labels[instruction.qubits[0]]};"
            elif operation.name == "barrier":
                qargs = ",".join(bit_labels[q] for q in instruction.qubits)
                instruction_qasm = "barrier;" if not qargs else f"barrier {qargs};"
            else:
                operation = _qasm2_define_custom_operation(
                    operation, existing_gate_names, gates_to_define
                )

                # Insert qasm representation of the original instruction
                bits_qasm = ",".join(
                    bit_labels[j] for j in itertools.chain(instruction.qubits, instruction.clbits)
                )
                #print(operation.qasm(), bits_qasm)
                instruction_qasm = f"{operation.qasm()} {bits_qasm};"
            instruction_calls.append(instruction_qasm)
        #print(instruction_calls)
        instructions_qasm = "".join(f"{call}\n" for call in instruction_calls)
        print(f'instructions_qasm: {instructions_qasm}', end='\n\n')
        print(f'gates_to_define: {dict(gates_to_define)}', end='\n\n')
        gate_definitions_qasm = "".join(f"{qasm}\n" for _, qasm in gates_to_define.values())
        #print(gate_definitions_qasm)
        out = "".join(
            (
                qc.header,
                "\n",
                qc.extension_lib,
                "\n",
                gate_definitions_qasm,
                register_definitions_qasm,
                instructions_qasm,
            )
        )

        if filename:
            with open(filename, "w+", encoding=encoding) as file:
                file.write(out)

        
        return out