import numpy as np
from numpy.random import rand
np.random.seed(0)

from numba import jit

from tqdm.auto import tqdm, trange

class IsingLattice():

    def __init__(self, T, N=8, h=0, drive_to_equilibrium=True,
                 want_samples=True):
        '''
        Initialize the class
        '''
        self.N = N
        self.T = T
        self.h = 0
        self.drive_to_equilibrium = drive_to_equilibrium
        self.want_samples = want_samples

        self.state0 = 2*np.random.randint(2, size=(N,N))-1

        self.equilibriation_steps = N**2

        if self.drive_to_equilibrium:
            self.equilibriate()

        self.samples = {}
        self.Nsamples = 10**4
        
        self.E, self.E2, self.M, self.M2 = 0, 0, 0, 0

        if self.want_samples:
            self.generate_samples()

    def plot_spins(self):
        '''
        Plot the spin lattice
        '''
        plt.clf()
        f, ax = plt.subplots(figsize=(8, 8))
        ax.imshow(self.state0, cmap=plt.cm.binary)
        ax.set_title('N = {}, T = {}'.format(self.N, self.T), fontsize=20)
        return ax

    @staticmethod
    @jit(nopython=True,fastmath=True,nogil=True)
    def mc_update(state, T, h):
        '''
        Make Monte-Carlo Metropolis-Hastings update to the state.
        '''
        beta = 1/T
        N = state.shape[0]
        
        for i in range(N):
            for j in range(N):
                
                a, b = np.random.randint(0, N), np.random.randint(0, N)
                s = state[a, b]
                neightbours_sum = state[(a+1)%N, b] + state[a, (b+1) % N] +\
                                state[(a-1)%N, b] + state[a, (b-1) % N]
                
                cost = 2 * s * neightbours_sum + 2 * h * s
                
                if cost < 0 or rand() < np.exp(-beta * cost):
                    s = -s
                
                state[a, b] = s
                
        return state
    
    @staticmethod
    @jit(nopython=True,fastmath=True,nogil=True)
    def calculate_energy(state, h):
        '''
        Calculate the energy of the system.
        '''
        N = state.shape[0]
        E = 0
        
        for i in range(N):
            for j in range(N):
                s = state[i, j]
                neightbours_sum = state[(i+1)%N, j] + state[i, (j+1) % N] +\
                                state[(i-1)%N, j] + state[i, (j-1) % N]
                E = E - s * neightbours_sum - h * s
                
        return E/2.0 # Remove counting redundancy
    
    @staticmethod
    @jit(nopython=True,fastmath=True,nogil=True)
    def calculate_magnetization(state):
        '''
        Calculate magnetization of the system.
        '''
        N = state.shape[0]
        Magnetization = np.abs(np.sum(state)) # Direction is irrelevant
        return Magnetization

    def equilibriate(self):
        '''
        Transform the random initial state into an equilirbium state through MC updates.
        '''
        state = self.state0
        for i in range(self.equilibriation_steps):
            state = self.mc_update(state, self.T, self.h)
            
        self.state0 = state

    def generate_samples(self):
        '''
        Generate samples for measurement by MC updating equilibriated lattice.
        '''
        state = self.state0
    
        states, Es, Ms = [], [], []
        
        for _ in range(self.Nsamples):
            state = self.mc_update(state, self.T, self.h)
            states.append(state)
            Es.append(self.calculate_energy(state, self.h))
            Ms.append(self.calculate_magnetization(state))
            
        self.samples = {'states': states,
                        'Es': np.array(Es),
                        'Ms': np.array(Ms)}