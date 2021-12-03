import numpy as np
import matplotlib.animation as animation
import matplotlib.pyplot as plt
import matplotlib.patches as patch
import math
class SIRS:
    
    def __init__(self,N,p1,p2,p3,fIm, sweeps = 10000, Immunity_lattice = None,lattice = None):
                """
                Initialises square lattice of infected,recovered and suseptable cells
                :param N: System size will be N x N
                :param p1: probability of S -> I
                :param p2: probability of I -> R
                :param p3: probability of R -> S
                :param fIm: Fraction of lattice sites which are immune to infection. Default is 0
                :param Immunity_lattice: This is the lattice showing immunity states of all the cells of the system. 1 -> Immune. 0 -> not Immune. 
                :param lattice: size * size system of cells which are in states S, I or R. Immune cells permanently in R state. Infected = 1, Suseptable = 0 and Recovered = -1 
                :param sweeps: number of sweeps completed in the simulation as an integer
                :param steps: There will be N x N steps in each sweep
                """
                self.N = N
                self.p1 = p1
                self.p2 = p2
                self.p3 = p3
                self.fIm = fIm
                if Immunity_lattice is None:
                    Immunity_lattice = np.zeros((self.N, self.N))
                    for i in range(self.N):
                        for j in range(self.N):
                            if np.random.random() < fIm:
                                Immunity_lattice[i][j] = -1
                self.Immunity_lattice = Immunity_lattice             
                if lattice is None:
                    lattice = np.random.choice((-1,0,1),(self.N,self.N))
                self.lattice = lattice
                self.sweeps = sweeps
                self.steps = self.N * self.N
                                                      
    def S_I(self,i,j):
        """
        Calculates probability of a cell going from a suseptable state to an infected state.
        """
        
        nn = [self.lattice[(i+1)%self.N,j],self.lattice[i,(j+1)%self.N],self.lattice[(i-1)%self.N,j],self.lattice[i,(j-1)%self.N]]
        
        #only need 1 infected neighbour to be suseptable and to account for recovered being -1 use max 
        if max(nn) >= 1:
            if np.random.random() <= self.p1:
                return 1
            else:
                return 0        
        else:
            return 0 
            
    def I_R(self):
        """
        Calculates probability of a cell going from an infected state to a recovered state.
        """
        if np.random.random() <= self.p2:
            return -1
        else:
            return 1  

    def R_S(self):
        """
        Calculates probability of a cell going from a recovered state to a suseptable state.
        """
        if np.random.random() <= self.p3:
            return 0
        else:
            return -1  
                
    def update(self):
        """
        Updates lattice stochastically using functions above.
        :return self.lattice: updated lattice
        """
        i = np.random.randint(0,self.N)
        j = np.random.randint(0,self.N)
        nn = [self.lattice[(i+1)%self.N,j],self.lattice[i,(j+1)%self.N],self.lattice[(i-1)%self.N,j],self.lattice[i,(j-1)%self.N]]
        

        immunity = self.Immunity_lattice[i][j]
        
        if immunity == -1:
            self.lattice[i][j] = -1
        else:
            if self.lattice[i][j] ==0:
                if max(nn) >= 1:
                    rand = np.random.random()
                    if rand <= self.p1:
                        self.lattice[i][j] = 1
            elif self.lattice[i][j] ==1:
                rand = np.random.random()
                if rand <= self.p2:
                    self.lattice[i][j] = -1
            elif self.lattice[i][j] ==-1:
                rand = np.random.random()
                if rand<= self.p3:
                    self.lattice[i][j] = 0
                
        return self.lattice         
            


    def infected_frac(self):
            """
            Calculates total number infected sites of the lattice
            :return: fraction of number of infected sites for the lattice 
            """
            I = 0.
            # Iterating over all spins in the lattice and adds them up
            for i in range(self.N):
                    for j in range(self.N):
                        if self.lattice[i][j] == 1:
                            I += 1
                
            return (float(I))
                       
    def animate(self,i):
        """
        Function that makes frames for animation.
        
        :return [frame]: plot of frame created in a list which is used in display
        """
        X,Y = np.meshgrid(range(self.N), range(self.N))
        mesh = plt.pcolormesh(X,Y, self.lattice ,cmap='cool',vmin=-1,vmax=1)
        
        for step in range(self.steps):          
            self.update()
        
        #self.implot.set_data(self.lattice)

        return mesh,
   
                
    def display(self):
        """
        Allows user to visualize every sweep (2500 updates) and how the SIRS model changes over time using Funcanimation
        """
        fig = plt.figure(figsize=(10,10),dpi=80)
        
        
        fig.suptitle("SIRS Model for p1=" + str(self.p1)+ ', p2=' + str(self.p2) + ', p3=' + str(self.p3),fontsize=20, fontweight = 'bold')
        a = animation.FuncAnimation(fig, self.animate, frames = int(self.sweeps), interval = 0.001, blit = True, repeat = True)
              
              
        recovered = patch.Patch(color='cyan', label='Recovered')
        infected = patch.Patch(color='magenta', label='Infected')
        susceptible = patch.Patch(color = '#858AE3', label = 'Susceptible')
        fig.legend(handles = [recovered, susceptible,infected], loc = 3)
              


        plt.show()
        
    def bootstrap(self,infec_frac):
        """
        Calculates the errors on the average infection number and variance of the average infection number using the bootstrap method for sampling
        
        :param infec_frac: list of the fraction of infected sites for the lattice at a given timestep (sweep)
        :return error_I: the error on the fraction of infected sites
        :return error_var_I: the error on the variance of the fraction of infected sites
        """
        #empty lists of infected number and it's variance
        I = []
        Var_I = []

        #chooses 100 resamples
        for l in range (0,100):
            
            n = np.random.randint(0,len(infec_frac),len(infec_frac))
            
            #empty lists of resampled data
            
            sample_I = []
            
            for x in n:
                #resamples fraction of infected sites of the lattice from lists for those given update probabilities
                sample_I.append(infec_frac[x])

            #updates resampled data and calculates average and variance of fraction of infected sites of the lattice 
            
            sample_Infected_frac = np.average(sample_I)
            sample_variance_I = np.var(sample_I)
            
            I.append(sample_Infected_frac)
            Var_I.append(sample_variance_I) 
        
        #calculates errors on average fraction of infected sites of the lattice and its variance
        error_I = np.std(I)
        error_var_I = np.std(Var_I)
        
        return error_I, error_var_I,
        
    def runmodel(self):
        """
        Runs model without animation and make measurements.
        
   
        :return Av_I: Average fraction of infected sites of the lattice
        :return Var_I: Variance of the average fraction of infected sites of the lattice
        :return error_I: the error of the average fraction of infected sites of the lattice
        :return error_var_I: the variance of the average fraction of infected sites of the lattice
        """
        
        
        # make empty list for fraction of infected sites within lattice
        infection_no = []

       
        for sweep in range(0, self.sweeps):
            
            # indicate percentage of completion
            if sweep % int(self.sweeps/10) == 0:
                print(str(sweep*100/self.sweeps) + '% of sweeps' + ' complete')
            
            for step in range(self.steps):          
                self.update()
                
            I = self.infected_frac()


            if sweep >= 100:
                infection_no.append(I)


                

        Av_I = (np.average(infection_no)/(self.N*self.N))
        Var_I = (np.var(infection_no)/(self.N*self.N))
        errors = self.bootstrap(infection_no)
        error_I, error_var_I = (errors[0]/(self.N*self.N)), (errors [1]/(self.N*self.N))
        
        
        file = open('FINAL Variance Cut.txt', 'a+')
        file.write('\n' + str(self.p1) + ' ' + str(self.p3) + ' ' + str(Av_I) + ' ' + str(error_I)+ ' ' + str(Var_I) + ' ' + str(error_var_I))
        file.close()
        
        
        file = open('Imunity Data.txt', 'a+')
        file.write('\n' + str(self.fIm) + ' ' + str(Av_I) + ' ' + str(error_I))
        file.close()
       
