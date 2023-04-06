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

def three(a, b, c):
    return np.kron(np.kron(a, b),c)

H_I_I = three(I, I, H)
CNOT_I = np.kron(CNOT, I)
T_dagger_I_I = three(I, I, T_dagger)
T_I_I = three(I, I, T)
T_T_dagger_I = three(I, T_dagger, T)
CNOT_H = np.kron(CNOT, H)
I_T_dagger_I = three(I, T_dagger, I)
T_S_I = three(T, S, I)



result = np.dot(H_I_I, CNOT_I)
result = np.dot(T_dagger_I_I, result)
result = np.dot(CNOT_I, result)
result = np.dot(T_I_I, result)
result = np.dot(CNOT_I, result)
result = np.dot(T_dagger_I_I, result)
result = np.dot(CNOT_I, result)
result = np.dot(T_T_dagger_I, result)
result = np.dot(CNOT_H, result)
result = np.dot(I_T_dagger_I, result)
result = np.dot(CNOT_I, result)
result = np.dot(T_S_I, result)


print(result)

