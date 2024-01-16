## No cloning theorem
* You can't copy a state if you don't know the $\alpha$ and $\beta$ values


## Measurements
* you create something in the $Z$ basis, then You measure in the $X$ basis, you have 50% of chance of not getting the initial prepared state

## QKD
1. Alice create a sequence of zeros and ones
2. Alice selects a random basis for each bit to be encoded
3. Alice sends the resulting states for Bob
4. Bob pick random basis to try to decode what Alice has sent
5. Alice publishes (publicly) the basis that she's used
6. they discard the values that bob measured with the wrong basis

* after the QKD, the final key Will be roughly 50% of the inital one


* If Eve tries to measure the values in a man-in-the-middle attack, it'll cause disturbance in the Bob's measured values, so the error rate in the system may increase
* If Eve attacks, It may not know the whole key, just about 50% of it

## BB84
* the used basis are non orthogonal one to another

* Hemogenization(random permutation): we distribute equally the disturbance through the whole key, so we know how much disturbance we expect to have in the Bob results.
	* If the final disturbance(QBER, quantum bits error rate) is <= the expected, we just apply a error correction code and a privacy amplification algorithm (these are classical)
	* However, if the QBER is high, we abort the protocol

## Six-state protocol
* You add more basis that a qubit can be measure, this decreases the amount percent of the key that Eve can have during a attack
* it also shrinkins the length of the key by $1\over N$ where $N$ is the number of basis

## Entanglement QKD
* Randomness: it's good because you can create random states just by measuring a quantum satte that are in entanglement
* monogamy: If a state is maximally entangled, it's totally unentangled with other parts, so if Alice and Bob are maximally entangled there's noone attacking the communication
* Whole vs part: You have a qubit in $Z$ basis that came from a entangled state, you can't know from what state it came from

* to check if Alice and bob are maximally entangled, we can Use the CHSH inequality, then if the get the expectation value of the system as $< C > = 2 \sqrt{2}$, so Eve isn't there
