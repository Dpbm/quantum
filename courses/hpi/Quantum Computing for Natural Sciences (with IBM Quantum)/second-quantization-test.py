import numpy as np

def get_sign(state, position):
    sign = 1
    for i in range(position-1):
        sign *= (-1)**state.item(i)
    return sign

def creation_operator(ground_state, position):
    ground_state.itemset(position-1, 1)
    return ground_state

def annihilation_operator(ground_state, position):
    ground_state.itemset(position-1, 0)
    return ground_state

ground_state = np.array([1, 1, 1, 0, 0])
print(f"ground state: {ground_state}")

a_dagger_4 = creation_operator(ground_state.copy(), 4)
a_dagger_4_sign = get_sign(a_dagger_4, 4)
print(f"a_4 dagger: {a_dagger_4_sign}*{a_dagger_4}")

a_3 = annihilation_operator(ground_state.copy(), 3)
a_3_sign = get_sign(a_3, 3)
print(f"a_3: {a_3_sign}*{a_3}")

result = np.bitwise_xor(np.bitwise_xor(a_dagger_4,  a_3), ground_state)
print(f"result: {a_3_sign*a_dagger_4_sign}*{result}")
