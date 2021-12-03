from SIRS import SIRS
import sys

if len(sys.argv) < 7:
    print('Incorrect number of arguments. Required format:')
    print('main.py Mode Size of Lattice p1 p2 p3 fraction of immune')
    print('Size of Lattice: Integer representing one side of the square lattice')
    print('p1,p2,p3 and fIM: probabilities ranging from 0 to 1')
    print('Mode: a for animate m for taking measurements')
    quit()
else:
    filename = sys.argv[0]
    Mode = str(sys.argv[1])
    N  = int(sys.argv[2])
    p1 = float(sys.argv[3])
    p2 = float(sys.argv[4])
    p3 = float(sys.argv[5])
    fIM = float(sys.argv[6])
    

if Mode == 'a':	
	model=SIRS(N,p1,p2,p3,fIM)   
	model.display()
	
if Mode == 'm':
	model = SIRS(N,p1,p2,p3,fIM)
	model.runmodel()
