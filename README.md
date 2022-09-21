# Ising Model (in progress)

Monte-Carlo simulation results for the 2 dimensional Ising model along with the results from the tensor network formulation of the partition function.

## The Problem

The Ising model is defined by the Hamiltonian (or energy function),
$$H = J \sum_{\langle ij \rangle} s_{i} s_{j} + h \sum_{i} s_{i}.$$

$s_{i}$, often called spins, take values $\pm 1$. The first summation is over neighbouring spins, defined by the topology of the spine lattice. $J$ is called the coupling costant, it specifies how neighbouring spins interact. $h$ is analogous to a magnetic field trying to align spins in its direction. When this model is used to study magnetism, $J > 0$ for anti-ferromagents (opposing neighbouring spins are energetically favourable) and $J < 0$ for ferromagnets (aligned neighbouring spins are energetically favourable). Remember that the model is completely classical, $s_{i}$'s are not spin operators.

Given the Hamiltonian, the formalism of statistical physics reduces the problem of evaluating the macroscopic variables essentially to a counting problem. All the these variables and correlation functions are encoded in the partition function,

$$Z = \sum_{\text{all states}} e^{-\beta H (\text{state})}.$$

$\beta$ is the inverse temperature.

The probability of a single state, $\text{Pr (state)} = \frac{e^{-\beta H (\text{state})}}{Z}$, following the fundamental assumption of statistical mechanics. With some pretty algebra, we can arrive at,

$$ \text{Energy}, \langle E \rangle = -\frac{\partial}{\partial \beta} ln Z $$

## Monte-Carlo Method


### Results

![Monte_Carlo_Equilibriated_Lattices](https://user-images.githubusercontent.com/43025445/189493373-4086e11a-47ef-40d2-bd60-900272930892.jpg)

![Monte_Carlo_Results](https://user-images.githubusercontent.com/43025445/189493379-50c35ff5-23d2-42cd-8950-2c57db613098.jpg)

## Tensor Network formulation
![TN Ising Result](https://user-images.githubusercontent.com/43025445/190865191-087e5006-9e8b-4857-9ca6-2cc0391d940b.png)
