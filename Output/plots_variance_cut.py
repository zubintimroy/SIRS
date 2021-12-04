import numpy as np
import matplotlib.pyplot as plt
import sys
"""
file = open(sys.argv[1], 'r')
#file = open('Data 2 for GoL Equilibrate Time.txt', 'r')
data = file.readlines()[1:]
file.close()
"""

data = np.genfromtxt(sys.argv[1],delimiter=' ')

p1=data[:,0]
p3=data[:,1]
Av_I=data[:,2]
error_I=data[:,3]
var_I =data[:,4]
error_var_I=data[:,5]


#variance cut graph

plt.errorbar(p1,(var_I),(error_var_I),ecolor='k', capthick=2,fmt ='o', markersize=3)
plt.plot(p1,(var_I),linewidth=1,color='c') 
plt.title("Variance of Average Fraction of Infection Sites for p2 = p3 = 0.5",fontsize=14, fontweight = 'bold')
plt.xlabel("p1",fontsize=12, fontweight = 'bold')
plt.ylabel("Average Fraction of Infection Sites",fontsize=12, fontweight = 'bold')
#plt.savefig(Variance of Average Fraction of Infection Sites for p2 = p3 = 0.5.jpg")
plt.show() 
plt.close()





