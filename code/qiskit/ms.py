import numpy as np

MS = (1/np.sqrt(2)) * np.array([
    [1, 0,  0,  1j],
    [0, 1, -1j, 0],
    [0, -1j, 1, 0],
    [1j, 0,  0, 1]
])

actual = MS
for _ in range(7):
    actual = np.dot(actual, MS)

print(actual)
