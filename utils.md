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
$cos(u ± v) = cos(u)cos(v)sin(u)sin(v)$

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

## Normalization constant (A) calculation

$A(α|0⟩ + β|1⟩) = 1$\
$(Aα)(Aα)^* + (Aβ)(Aβ)^* = 1$

## Measurements

Measurements in X\
$|0⟩= {1 \over \sqrt{2}}(|+⟩ + |-⟩)$\
$|1⟩= {1 \over \sqrt{2}}(|+⟩ - |-⟩)$

Measurements in Y\
$|0⟩= {1 \over \sqrt{2}}(|i⟩ + |-i⟩)$\
$|1⟩= {-i \over \sqrt{2}}(|i⟩ - |-i⟩)$

Measurements in other basis\
$|a⟩ = α|0⟩ + β|1⟩$\
$|b⟩ = γ|0⟩ + δ|1⟩$\
$|0⟩ = α^*|a⟩ + β^*|b⟩$\
$|1⟩ = γ^*|a⟩ + δ^*|b⟩$

consecutive measurements in different basis the result is always 1/2 for both states

## Phase

global phase can be ignored at measurements

## Probabilities

${1 \over \sqrt{2}}(|0⟩+i|1⟩) = {1 \over \sqrt{2}}(|0⟩ + e^{iπ \over 2}) = {1 \over \sqrt{2}}(|0⟩+|1⟩) = {1 \over \sqrt{2}}(|+⟩ + |-⟩)$

$|α|^2 + |β|^2 = 1$

α need to be a positive real number and β a complex number\
$α = cos({θ \over 2})$\
$β = e^{iθ}sin({θ \over 2})$

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

A gate, need to be always unitary and reversible

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
