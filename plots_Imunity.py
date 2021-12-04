import numpy as np
import matplotlib.pyplot as plt
import sys

data = np.genfromtxt(sys.argv[1],delimiter=' ')

ImF=data[:,0]
Av_I=data[:,1]

Av_ImF=[]
Av_Av_I=[]
error_I =[]


for i in range(101):
	Av_ImF.append(np.mean(ImF[i::101]))
	Av_Av_I.append(np.mean(Av_I[i::101]))
	error_I.append(np.std(Av_I[i::101]))
	
	

plt.axhline(y=0, color='k', linestyle=':')
plt.errorbar(Av_ImF,Av_Av_I,error_I,capsize=2) 
plt.plot(Av_ImF,Av_Av_I,'bx') 
plt.title('SIRS Model - Fraction of Immunity vs Average Fraction of Infection Sites',fontsize=18, fontweight = 'bold')
plt.xlabel('Average Fraction of Infection Sites',fontsize=12, fontweight = 'bold')
plt.ylabel('Fraction of Immunity',fontsize=12, fontweight = 'bold')
plt.show()  

