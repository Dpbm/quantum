# Useful notes

## complex numbers and some relations
$z = x + iy = re^{iθ}$

$r = \sqrt{x^2 + y^2}$

$θ = tan^{-1}({y \over x})$

$x = rcosθ$\
$y = rsinθ$\
${y \over x} = tan(θ)$

$e^{iθ} = cosθ + isinθ$\
$e^{iθ} + e^{-iθ}= 2cosθ$

$x^2 + y^2 = r^2$

$z^* = x - iy = re^{-iθ}$

$|z| = r$\
$|z|^2 = r^2 = zz^*$

$e^{iπ} = -1 = i^2$\
$\sqrt{e^{iπ}} = i = e^{iπ \over 2} = e^{iπ \over 6}$\
$e^{i2π} = 1$\
$e^{i3π \over 2} = -i$

$sin(u ± v) = sin(u)cos(v)±cos(u)sin(v)$\
$cos(u ± v) = cos(u)cos(v)±sin(u)sin(v)$

## linear algebra and dirac notation

$\begin{bmatrix}
    α \\
    β
\end{bmatrix}^T = 
\begin{bmatrix}
    α 
    β
\end{bmatrix}$

$\begin{bmatrix}
    α \\
    β
\end{bmatrix}^{\dagger} = 
\begin{bmatrix}
    α^* 
    β^*
\end{bmatrix}$

$|ψ⟩ = \begin{bmatrix}
    α \\
    β
\end{bmatrix}$ \
it's called ket

$⟨ψ| = 
\begin{bmatrix}
    α^* 
    β^*
\end{bmatrix} = 
\begin{bmatrix}
    α^* 
    0
\end{bmatrix} +
\begin{bmatrix}
    0 
    β^*
\end{bmatrix} =
α^*⟨0| + β^*⟨1|$\
it's called bra 

## Inner product

$⟨ψ|Φ⟩ = 
\begin{bmatrix}
    α^* 
    β^*
\end{bmatrix}
\begin{bmatrix}
    γ \\
    δ
\end{bmatrix} =
α^*γ + β^*δ
$\
it's a inner product also called as bra-ket

$⟨Φ|ψ⟩ = ⟨ψ|Φ⟩^*$

$⟨ψ|ψ⟩ = 
\begin{bmatrix}
    α^* 
    β^*
\end{bmatrix}
\begin{bmatrix}
    α \\
    β
\end{bmatrix} =
|α^2| + |β^2| = 1
$\
$⟨Uψ|Uψ⟩ = ⟨ψ|U^{\dagger}U|ψ⟩ = ⟨ψ|ψ⟩ = 1 $\
if the result of $⟨ψ|ψ⟩$ is $1$ so the state is normalized

$⟨+|-⟩ = ⟨0|1⟩ = ⟨i|-i⟩ = 0$\
if the result is 0, so these states are orthogonal

if you test the states and they are normalized and orthogonal, so you have a orthonormal basis

$|ψ⟩ = ⟨0|ψ⟩|0⟩ + ⟨1|ψ⟩|1⟩$

$|ψ⟩ = α|a⟩ + β|b⟩$\
$α = ⟨a|ψ⟩$\
$β = ⟨b|ψ⟩$\
$⟨a|ψ⟩$ is a projection of |ψ⟩ on |a⟩

$(AB)^{\dagger} = A^{\dagger}B^{\dagger}$\
$|ψ⟩^{\dagger} = ⟨ψ|$\
$⟨Uψ| = (|Uψ⟩)^{\dagger} = U^{\dagger}|ψ⟩^{\dagger} = ⟨ψ|U^{\dagger}$

$U^{\dagger}U = I$\
If a matrix $U$ times $U^{\dagger}$ result in $I$, so it's a unitary matrix

$M^{-1}M = I$\
$U^{-1} = U^{\dagger}$

## Outer Product

$|ψ⟩⟨Φ| = 
\begin{bmatrix}
    α\\
    β
\end{bmatrix}
\begin{bmatrix}
    γ^*
    δ^*
\end{bmatrix} = 
\begin{bmatrix}
    αγ^* \space αδ^*\\
    βγ^* \space βδ^*
\end{bmatrix}$

$U = \begin{bmatrix}
    0 \space 1 \\
    1 \space 0
\end{bmatrix}$\
$U = 0|0⟩⟨0| + 1|0⟩⟨1| + 1|1⟩⟨0| + 0|1⟩⟨1| $\
$U = |0⟩⟨1| + |1⟩⟨0| = X$

$|a⟩⟨a| + |b⟩⟨b| = I$

$|ψ⟩ = α|a⟩ + β|b⟩$\
$|ψ⟩ = ⟨a|ψ⟩|a⟩ + ⟨b|ψ⟩|b⟩$\
$|ψ⟩ = |ψ⟩|a⟩⟨a| + |ψ⟩|b⟩⟨b|$\
$|ψ⟩ = (|a⟩⟨a| + |b⟩⟨b|)|ψ⟩$\
$|ψ⟩ = I|ψ⟩$\
If you can do this with an orthonormal basis, this is an complete orthonormal basis 

## Tensor product (Kronecker product)

$|0⟩ ⊗ |0⟩ = |00⟩$\
$⟨0| ⊗ ⟨0| = ⟨00|$

$c_{0}|00⟩ + c_{1}|01⟩ + c_{2}|10⟩ +  c_{3}|11⟩$\
The probability of each state is $|c_{x}|^2$

$|0⟩^{⊗n} = |0⟩ ⊗ |0⟩ ⊗\dots⊗|0⟩ = |0^{n}⟩$

$⟨01|00⟩ = ⟨0|0⟩⟨1|0⟩$

Kronecker product, it's the tensor product for linear algebra

$
\begin{bmatrix}
    0\\
    1
\end{bmatrix}⊗
\begin{bmatrix}
    1\\
    0
\end{bmatrix} = 
\begin{bmatrix}
    0 \\
    0 \\
    1 \\
    0
\end{bmatrix}
$

$c_{0}|00⟩ + c_{1}|01⟩ + c_{2}|10⟩ +  c_{3}|11⟩ = \begin{bmatrix}
    c_{0} \\
    c_{1} \\
    c_{2} \\
    c_{3}
\end{bmatrix}$

$⟨00| = \begin{bmatrix}
    1 \space
    0
\end{bmatrix} ⊗ \begin{bmatrix}
    1 \space
    0
\end{bmatrix} = \begin{bmatrix}
1 \space
0 \space
0 \space
0
\end{bmatrix}
$

$|ψ⟩ = \sum_{j=0}^{n-1} c_{j}|j⟩ = c_{0}|0⟩ + c_{1}|1⟩ + c_{2}|2⟩ + \dots + c_{n-1}|n-1⟩$\
$⟨ψ| = \sum_{j=0}^{n-1} c_{j}⟨j| = c_{0}⟨0| + c_{1}⟨1| + c_{2}⟨2| + \dots + c_{n-1}⟨n-1|$\
where $n$ is the number of qubits 

In a 3 qubits circuit, with the collapsed state for the last and middle qubits are both 0, the state will be
$c_{0}|000⟩ + c_{1}|001⟩ \over \sqrt{|c_{0}|^2 + |c_{1}|^2}$

$(H ⊗ I)(|0⟩⊗|0⟩) = H|0⟩ ⊗ I|0⟩$\
$H^{⊗n} |0⟩^{⊗n} = H|0⟩ ⊗ I|0⟩$

$(H ⊗ I)|00⟩ = {1 \over \sqrt2}(|00⟩ + |10⟩)$\
$(H ⊗ I)|01⟩ = {1 \over \sqrt2}(|01⟩ + |11⟩)$\
$(H ⊗ I)|10⟩ = {1 \over \sqrt2}(|00⟩ - |10⟩)$\
$(H ⊗ I)|11⟩ = {1 \over \sqrt2}(|01⟩ - |11⟩)$

$(H ⊗ X)|00⟩ = {1 \over \sqrt2}(|01⟩ + |11⟩)$

$CNOT(I ⊗ X) = (I ⊗ X)CNOT$ this is represented in a circuit from right to left

## Factoring states

$|ψ_{0}⟩|ψ_{1}⟩ = (α_{0}|0⟩ + β_{0}|1⟩)(α_{1}|0⟩ + β_{1}|1⟩) = α_{0}α_{1}|00⟩ + α_{0}β_{1}|01⟩ + β_{0}α_{1}|10⟩ + β_{0}β_{1}|11⟩$

## Entangled states

An entangled state can't be factored. Because of that, for classical computers, it's difficult to map all the amplitudes, once in a entangled state you need to map all $2^n$ possible states, but with no entangled states you only need to map $2n$

the $CNOT$ with the $H$ gate, can create a entangled state

$CNOT|+⟩|0⟩ = {1\over\sqrt2}(|00⟩ + |11⟩) = |Φ^+⟩$\
$CNOT|-⟩|0⟩ = {1\over\sqrt2}(|00⟩ - |11⟩) = |Φ^-⟩$\
$CNOT|+⟩|1⟩ = {1\over\sqrt2}(|01⟩ + |10⟩) = |ψ^+⟩$\
$CNOT|-⟩|1⟩ = {1\over\sqrt2}(|01⟩ - |10⟩) = |ψ^-⟩$\
These are the bell states

## Normalization constant (A) calculation

$A(α|0⟩ + β|1⟩) = 1$\
$(Aα)(Aα)^* + (Aβ)(Aβ)^* = 1$

## Measurements

Measurements in X\
$|0⟩ = {1 \over \sqrt{2}}(|+⟩ + |-⟩)$\
$|1⟩ = {1 \over \sqrt{2}}(|+⟩ - |-⟩)$

Measurements in Y\
$|0⟩= {1 \over \sqrt{2}}(|i⟩ + |-i⟩)$\
$|1⟩= {-i \over \sqrt{2}}(|i⟩ - |-i⟩)$

Measurements in other basis\
$|a⟩ = α|0⟩ + β|1⟩$\
$|b⟩ = γ|0⟩ + δ|1⟩$\
$|0⟩ = α^*|a⟩ + β^*|b⟩$\
$|1⟩ = γ^*|a⟩ + δ^*|b⟩$

consecutive measurements in different basis the result is always 1/2 for both states

${1 \over \sqrt{2}}|00⟩ + {1 \over 2}|01⟩ + {\sqrt{3} \over 4}|10⟩ + {1 \over 4}|11⟩$\
The probability of $|x0⟩$ is $|{1 \over \sqrt{2}}|^2 + |{\sqrt{3} \over 4}|^2$\
If we measured the first qubit(rightmost in little endian system) and the result is zero, so the state of the circuit is $A({1 \over \sqrt{2}}|00⟩ + {1 \over 2}|01⟩)$

The states can also be measured sequentially
$Prob(|00⟩) = Prob(|0⟩)Prob(|0⟩)$

## Phase

global phase can be ignored at measurements

## Probabilities

${1 \over \sqrt{2}}(|0⟩+i|1⟩) = {1 \over \sqrt{2}}(|0⟩ + e^{iπ \over 2}) = {1 \over \sqrt{2}}(|0⟩+|1⟩) = {1 \over \sqrt{2}}(|+⟩ + |-⟩)$

$|α|^2 + |β|^2 = 1$

α need to be a positive real number and β a complex number\
$α = cos({θ \over 2})$\
$β = e^{iθ}sin({θ \over 2})$

## Ancillas
Ancillas need to be reset.

## Bloch sphere

θ is the angle between the poles (z-axis)\
Φ is the angle between x and y axis (this is present in $e^{iΦ}$)

to know if two states are in opposite sides in the bloch sphere\
$θb = π - θa$\
$Φb = Φa + π$

cartesian coordinates in the bloch sphere\
$z = cosθ$\
$y = sinΦ sinθ$\
$x = cosΦ sinθ$


${\displaystyle \mathbf {\hat {n}} } = n _{x}{\displaystyle \mathbf {\hat {x}} } + n _{y}{\displaystyle \mathbf {\hat {y}} } + n _{z}{\displaystyle \mathbf {\hat {z}} }$\
${\displaystyle \mathbf {\hat {n}} }$ is a unit vector that represents a rotation on bloch sphere\
$n _{(x,y,z)}$ represents the rotation number for each axis\
${\displaystyle \mathbf {\hat {x}} }$,${\displaystyle \mathbf {\hat {y}} }$ and ${\displaystyle \mathbf {\hat {z}} }$  represents points on the sphere\
also $|n _{x}|^2 + |n _{y}|^2 +|n _{z}|^2 = 1$

## Gates

A gate, need to be always unitary and reversible\
The number of outputs of a gate needs to be the same of the inputs to be reversible and map all possible results

$X^{100} = I$\
$X^{101} = X$

$X|0⟩ = |1⟩$\
$X|1⟩ = |0⟩$

$XY = iZ$

$Y|0⟩ = i|1⟩$\
$Y|1⟩ = -i|0⟩$\
Y gate is not a classical gate, since it has a $i$ and $-i$ phase

Y, X, Z gates rotate 180° on its axis(x, y, z respectively)

$S|0⟩ = |0⟩$\
$S|1⟩ = i|1⟩$\
$S = \sqrt{Z}$ or $S^2 = Z$\
S gate rotates 90° on the Z axis

$T|0⟩ = |0⟩$\
$T|1⟩ = e^{iπ \over 4}|1⟩$\
$T^2 = S$\
$T^4 = Z$\
T gate is also called $π \over 8$ gate\
T gate rotates 45° on the Z axis\

$H|0⟩ = {1 \over \sqrt{2}}(|0⟩ + |1⟩) = |+⟩$\
$H|1⟩ = {1 \over \sqrt{2}}(|0⟩ - |1⟩) = |-⟩$\
H gate is also called Hadamard gate\
H gate rotates 180° between X and Y axis

$X^2 = Y^2 = S^4 = T^8 = H^2 = I$

$U = e^{iγ}[cos({θ \over 2})I - isin({θ \over 2})(n _{x}X + n _{y}Y + n _{z}Z)]$\
Where $γ$ is the global phase

$αU|0⟩ + βU|1⟩ = U(α|0⟩ + β|1⟩) = αe^{iγ}[cos({θ \over 2})I - isin({θ \over 2})(n _{x}X + n _{y}Y + n _{z}Z)]|0⟩ + βe^{iγ}[cos({θ \over 2})I - isin({θ \over 2})(n _{x}X + n _{y}Y + n _{z}Z)]|1⟩$

$U|0⟩ = a|0⟩ + b|1⟩ = \begin{bmatrix}
    a\\
    b
\end{bmatrix}$\
$U|1⟩ = c|0⟩ + d|1⟩ = \begin{bmatrix}
    c\\
    d
\end{bmatrix}$\
$U = \begin{bmatrix}
    a \space c \\
    b \space d
\end{bmatrix}$

$U|ψ⟩ = \begin{bmatrix}
    a \space c\\
    b \space d
\end{bmatrix} \begin{bmatrix}
    α\\
    β
\end{bmatrix} = \begin{bmatrix}
    aα + cβ\\
    bα + dβ
\end{bmatrix}$\
$|aα + cβ|^2 + |bα + dβ|^2 = 1$

$U|ψ⟩ = |Uψ⟩$\
$⟨Uψ| = \begin{bmatrix}
    a^*α^* + c^*β^* \space\space\space 
    b^*α^* + d^*β^*\end{bmatrix} = 
\begin{bmatrix}
    α^*\space
    β^*
\end{bmatrix}
\begin{bmatrix}
    a^* \space c^*\\
    b^* \space d^*
\end{bmatrix} = 
\begin{bmatrix}
    α^*\space
    β^*
\end{bmatrix}
\begin{bmatrix}
    a \space c\\
    b \space d
\end{bmatrix}^{\dagger} = ⟨ψ|U^{\dagger}$


CNOT (CX) inverts the right qubit(target) if the left qubit(control) is 1\
$CNOT(|10⟩) = |11⟩$\
the control qubit is not changed because it has a XOR\
$CNOT|a⟩|b⟩ = |a⟩|a ⊗ b⟩$\
$CNOT(c_{0}|00⟩ + c_{1}|01⟩ + c_{2}|10⟩ + c_{3}|11⟩) = c_{0}|00⟩ + c_{1}|01⟩ + c_{2}|11⟩ + c_{3}|10⟩$ it inverts the $c_{2}$ with the $c_{3}$ amplitude\
$CNOT = CNOT_{ij} = CNOT_{10}$ where $i$ is the control and $j$ the target\
$(H ⊗ H) CNOT_{01} (H ⊗ H) = CNOT_{10}$ it inverts the control with the target

$(X ⊗ I) CNOT (X ⊗ I)$ it is called $anti \space CNOT$

Controlled U (CU), it applies U in the right qubit, when the left qubit is 1\
$CU|00⟩ = |00⟩$\
$CU|01⟩ = |01⟩$\
$CU|10⟩ = |1⟩ ⊗ U|0⟩$\
$CU|11⟩ = |1⟩ ⊗ U|1⟩$

SWAP, the swap inverts two qubits positions, but differently from CNOT, it can't create entangled states\
$SWAP|00⟩ = |00⟩$\
$SWAP|01⟩ = |10⟩$\
$SWAP|10⟩ = |01⟩$\
$SWAP|11⟩ = |11⟩$\
it also invert amplitudes
$SWAP(c_{0}|00⟩ + c_{1}|01⟩ + c_{2}|10⟩ + c_{3}|11⟩) = c_{0}|00⟩ + c_{1}|10⟩ + c_{2}|01⟩ + c_{3}|11⟩$\
$SWAP = CNOT \space CNOT_{01} \space CNOT$

Toffoli gate (CCX), inverts the right qubit if the other two are 1\
$Toffoli|111⟩ = |110⟩$\
$Toffoli|110⟩ = |111⟩$

$R{_r} = {360 \degree \over 2^r} \space on \space Z axis$\
$R{_1} = Z$\
$R{_2} = S$\
$R{_3} = T$\
$R{_4} = 22.5 \degree$\
$R{_r}^{\dagger} = -{360 \degree \over 2^r}$

## No cloning theorem

An unknown quantum state can't be reproduced(replicated) if we don't know each amplitude\
$|ψ⟩|0⟩ = |ψ⟩|ψ⟩$\
$U|ψ⟩|0⟩ = |ψ⟩|ψ⟩$ there's no operator $U$ that can pass $|ψ⟩$ state to the right qubit, once the result is $|ψ⟩^2$ which isn't linear

But for $(I ⊗ H)|+⟩|0⟩ = |+⟩|+⟩$ we can clone, $|+⟩$, once we know the amplitudes\
Generally $U$ can only copy states that are orthogonal\
$(I ⊗ H)|+⟩|0⟩ = |+⟩|+⟩$\
$(x ⊗ H)|-⟩|0⟩ = |-⟩|-⟩$\
$(I ⊗ I)|0⟩|0⟩ = |0⟩|0⟩$\
$(I ⊗ X)|1⟩|0⟩ = |1⟩|1⟩$\
$(I ⊗ Y)|i⟩|0⟩ = |i⟩|i⟩$\
$(X ⊗ Y)|-i⟩|0⟩ = |-i⟩|-i⟩$
