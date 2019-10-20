import numpy as np
import matplotlib.pyplot as plt

#initial conditions
theta = np.deg2rad(2*np.pi)
length = 200
x = int(length*np.cos(theta))
y = int(length*np.sin(theta))
lattice = []
random_number= np.random.randint(1,5,1000)



#setting the seed particle in the centre of lattice
def initialise(length):
    
    for i in range(length):
        lattice.append([])

    for i in range(length):        
        for j in range(length):
            lattice[i].append(0)
        
    initialSeed = [int(length/2.0), int(length/2.0)]
    lattice[initialSeed[0]][initialSeed[1]] = 1
      
    return lattice
  
j=0
initialise(length)

lattice[50][50]=1
for i in range(1000):  # no of particles to try
    theta = np.random.uniform(0,2*np.pi)
    length = 100
    x = int(length*np.cos(theta))
    y = int(length*np.sin(theta))
    
    
    
    print i
    j=0 #reset
    while   j!=-10:
        move=np.random.randint(1,5)
        if move==1:
            x = x + 1
    
        elif move==2:
            y = y + 1
        
        elif move==3:
           x = x - 1
            
        else:
            y = y - 1
        
        #check to see if particle wandered outside kill radius
        if np.sqrt(x**2+y**2) > 300 :
            print 'Went too far'
            j=-10
        
        #check to see if walker is within lattice
        if np.sqrt(x**2+y**2) < 50 :
            if (lattice[x-1+50][y+50] == 1 or lattice[x+1+50][y+50] == 1 or lattice[x+50][y+1+50]
                or lattice[x+50][y-1+50]==1):
                lattice[x+50][y+50] = 1
                print 'Stuck'
                print i,x,y
                j=-10                
                  
#print lattice
plt.figure()
for i in range(100):
    for j in range(100):#for a particular x value
            if lattice[i][j]==1:
                plt.scatter(i,j, c='b')
plt.xlim([0,100])
plt.ylim([0,100])
plt.show() 