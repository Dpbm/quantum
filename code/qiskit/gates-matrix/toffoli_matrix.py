import numpy as np

H = (1/np.sqrt(2)) * np.matrix([[1, 1], [1,-1]])
CNOT = np.matrix([
    [1, 0, 0, 0],
    [0, 1, 0, 0],
    [0, 0, 0, 1],
    [0, 0, 1, 0]
])


T = np.matrix([
    [1, 0],
    [0, np.exp((1j * np.pi)/4)]
    ])

T_dagger = T.H

S = np.matrix([
    [1, 0],
    [0, 1j]
])

CCX = np.matrix([
    [1, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 0, 1, 0]
])

I = np.matrix([
    [1, 0],
    [0, 1]
])

def thre(a, b, c):
    return np.kron(np.kron(a, b),c)

def cnot_top():
    return np.matrix([
        [1, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1],
        [0, 0, 0, 0, 0, 0, 1, 0],
        ])

def cnot_bound(): 
    return np.matrix([
        [1, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1],
        [0, 0, 0, 0, 0, 0, 1, 0],
        ])

def cnot_bottom():
    return np.matrix([
        [1, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 1],
        [0, 0, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 1, 0, 0],
        ])



result = np.dot(thre(I, I, H), cnot_top())
result = np.dot(thre(I, I, T_dagger), result)
result = np.dot(cnot_bound(), result)
result = np.dot(thre(I, I, T), result)
result = np.dot(cnot_top(), result)
result = np.dot(thre(I, I, T_dagger), result)
result = np.dot(cnot_bound(), result)
result = np.dot(thre(I, T_dagger, I), result)
result = np.dot(thre(I, I, T), result)
result = np.dot(thre(I, I, H), result)
result = np.dot(cnot_bottom(), result)
result = np.dot(thre(I, S, I), result)
result = np.dot(thre(T, I, I), result)

print(result)

