import numpy as np
import matplotlib.pyplot as plt
import sys

data = np.genfromtxt(sys.argv[1],delimiter=' ')

p1=data[:,0]
p3=data[:,1]
Av_I=data[:,2]
error_I=data[:,3]
var_I =data[:,4]
error_var_I=data[:,5]


p1=np.unique(p1)
p3=np.unique(p3)
P1,P3 = np.meshgrid(p1,p3)

I=Av_I.reshape(len(p3),len(p1))
Var_I=var_I.reshape(len(p3),len(p1))

plt.pcolormesh(P1,P3,(I/2500))
plt.title('SIRS Model - Average of Infected Fraction Heatmap for p2 = 0.5',fontsize=18, fontweight = 'bold')
plt.xlabel('p1',fontsize=12, fontweight = 'bold')
plt.ylabel('p3',fontsize=12, fontweight = 'bold')
cbar = plt.colorbar()
cbar.ax.set_ylabel('Average Fraction of Infection Sites',fontsize=12, fontweight = 'bold')
#plt.savefig(SIRS Model - Average Infection Contour Plot.jpg)
plt.show()

plt.pcolormesh(P1,P3,(Var_I/2500))
plt.title('SIRS Model - Variance of Infected Fraction Heatmap for p2 = 0.5',fontsize=18, fontweight = 'bold')
plt.xlabel('p1',fontsize=12, fontweight = 'bold')
plt.ylabel('p3',fontsize=12, fontweight = 'bold')
cbar = plt.colorbar()
cbar.ax.set_ylabel('Variance of Fraction of Infection Sites',fontsize=12, fontweight = 'bold')
#plt.savefig(SIRS Model - Variance Infection Contour Plot.jpg)
plt.show()

