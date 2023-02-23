from quantum.operations import Operations

operations = Operations()

zero = {
        "vector" : operations.create_vector([[1], [0]]),
        "symbol" : "|0>"
}


one = {
        "vector": operations.create_vector([[0], [1]]),
        "symbol": "|1>"
}
