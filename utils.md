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
$\sqrt{e^{iπ}} = i = e^{iπ \over 2} = e^{iπ \over 6}$

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

## Gates

$X^{100} = I$\
$X^{101} = X$

$X|0⟩ = |1⟩$\
$X|1⟩ = |0⟩$

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


