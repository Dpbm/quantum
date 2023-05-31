import numpy as np

H = (1/np.sqrt(2))*np.matrix([
    [1, 1],
    [1, -1]
    ])

X = np.matrix([
    [0, 1],
    [1, 0]
    ])


assert (np.kron(H, X) == np.kron(X, H)).all(), 'Are different'
