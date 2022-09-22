# Ising Model (in progress)

Monte-Carlo simulation results for the 2 dimensional Ising model along with the results from the tensor network formulation of the partition function.

## The Problem

The Ising model is defined by the Hamiltonian (or energy function),
$$H = J \sum_{\langle ij \rangle} s_{i} s_{j} + h \sum_{i} s_{i}.$$

$s_{i}$, often called spins, take values $\pm 1$. The first summation is over neighbouring spins, defined by the topology of the spine lattice. $J$ is called the coupling costant, it specifies how neighbouring spins interact. $h$ is analogous to a magnetic field trying to align spins in its direction. When this model is used to study magnetism, $J > 0$ for anti-ferromagents (opposing neighbouring spins are energetically favourable) and $J < 0$ for ferromagnets (aligned neighbouring spins are energetically favourable). Remember that the model is completely classical, $s_{i}$'s are not spin operators.

Given the Hamiltonian, the formalism of statistical physics reduces the problem of evaluating the macroscopic variables essentially to a counting problem. All the these variables and correlation functions are encoded in the partition function,

$$Z = \sum_{\text{all states}} e^{-\beta H (\text{state})}.$$

$\beta$ is the inverse temperature.

The probability of a single state, $\text{Pr (state)} = \frac{e^{-\beta H (\text{state})}}{Z}$, following the fundamental assumption of statistical mechanics (that states all the microscopic configurations of an isolated system are equally likely) extended to systems in thermal equilibrium. With some pretty algebra, we can arrive at,

$$ \text{Energy}, \langle E \rangle = -\frac{\partial}{\partial \beta} ln Z, $$

$$ \text{Specific heat capacity}, C_{v} = \frac{\partial}{\partial T} \langle E \rangle = \frac{\Delta E^{2}}{k_{B}T^{2}}, $$

$$ \text{Magentisation},\langle M \rangle = \frac{\partial}{\partial h} E, \text{and}, $$

$$ \text{Magnetic susceptibility},\langle \chi \rangle = \frac{\partial}{\partial h} M = \frac{\Delta M^{2}}{T} .$$

### Lattice Topologies

Though the formalism is simple, the counting problem associated with  evaluating $Z$ is non-trivial in most cases. For the Ising Hamiltonian, it is easy for a $1d$ lattice that does not exhibit a phase transition. For the 2d square lattice (see the following figure), Onsager gave a solution for the $h =0$ Hamiltonian (10-20 pages of difficult math) and analytic solutions are not known in higher dimensions.

We take periodic boundary conditions but the differences disappear as the lattice size grows.
![2d Ising Lattice](https://user-images.githubusercontent.com/43025445/191721054-ddb2fd4c-a998-457a-b058-5697b4a65d25.png)

## Monte-Carlo Method

Monte-Carlo method allows us to generate an ensemble of possible spin configurations so that we can evaluate the thermodynamic variables without $Z$. It can transform a random spin state into a possible configuration after some steps and then generate more samples as it treads through the configuration space. We will be using the Metropolis-Hastings algorithm that changes one spin at a time but faster cluster algorithms like the Wolff algorithm that updates blocks of spins at a time.

### Algorithm
1) Choose a spin at random.
2) Flip it.
3) Accept the flip with a probability $e^{-\beta \Delta E}$.
4) Back to 1).

Monte-Carlo updates satisfy the conditions of ergodicity and detailed balance.

1) Ergodicity: The algorithm can reach all possible configurations at least in theory.
2) Detailed balance: $\text{Pr}(i \rightarrow j) = \text{Pr}(j \rightarrow i)$

### Results

We generate an ensemble for $N = 8$ square lattice in $2d$ with $h = 0 \text{and} J = 1$. Equilibriated samples are taken after $N^{2}$ updates to the random state. One update consists of $N^{2}$ spin flips. Then the thermodynamical variables are evaluated on an ensemble of $10^{4}$ states generated using similar updates.

![Monte_Carlo_Equilibriated_Lattices](https://user-images.githubusercontent.com/43025445/189493373-4086e11a-47ef-40d2-bd60-900272930892.jpg)

![Monte_Carlo_Results](https://user-images.githubusercontent.com/43025445/189493379-50c35ff5-23d2-42cd-8950-2c57db613098.jpg)

## Tensor Network formulation

Tensor network is an increasingly popular paradigm in computation that allows to parametrize high dimensional state spaces by expressing them as a contraction of arrays. Lattice Hamiltonians can be expressed as a contraction of tensor network and you can obtain the exact answer if you have the computational power to contrat it. The amount of computation required to evaluate the contractions is highly dependent on the contraction path. So either we can search for an optimal path or use renormalization approaches that progressively approximates the matrices and truncate the network.

Luckily then tensor network corresponding to the Ising model corresponds to the topology of the spin lattice itself, with matrices at nodes and edges correspond to contraction of indices.

Let's make some definitions.
$$
S = \begin{bmatrix}
    e^{\beta} & e^{-\beta} \\
    e^{-\beta} & e^{\beta} \\
\end{bmatrix}
$$
For this symmetric matrix, we can take a matrix square root: $S^{root} = \sqrt{S}$. The tensor to be placed at at the lattice site is 

$$
T_{abcd} = S^{root}_{ia} S^{root}_{ib} S^{root}_{ic} S^{root}_{id}
$$
It is not very hard to convince yourself that the contraction of such a tensor network yields the partition function for the Ising model with $h=0$. We will use Google's `Tensor Network` library to perform the contraction.
**Add an example**

$Z$, on itself, is not of much physical interest. You can calculate the free energy $F = -k_{B} T ln Z$ directly and the thermodynamic variables by taking numerical derivatives of $Z$.
![Free energy](https://user-images.githubusercontent.com/43025445/191744779-91d57dfb-61e2-49e6-8e6b-87615661868e.jpg)
![TN E and C](https://user-images.githubusercontent.com/43025445/191744812-3d4b31e8-2b90-4432-8f05-9dde4b28962a.jpg)

To compute $M \text{and} \chi$, we need to use a different tensor network that is lightly more complicated.
