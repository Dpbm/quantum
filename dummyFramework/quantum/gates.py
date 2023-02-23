from quantum.operations import Operations

operations = Operations()
two_square_root = operations.square_root(2)


X = {
    "vector": operations.create_vector([[0, 1], [1, 0]]),
    "symbol": "X"
}
    
Z = {
    "vector": operations.create_vector([[1, 0], [0, -1]]),
    "symbol": "Z"
}
    
H = {
    "vector" : operations.create_vector([
                    [ 1/two_square_root,  1/two_square_root ],
                    [ 1/two_square_root, -1/two_square_root ]
                ]),
    "symbol": "H"
}
