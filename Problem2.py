    
# if we make matrix without difference of 5
import numpy as np
z= np.random.randint(100,200,size=(8,2))
z

# to make matrix with difference of 5 but in range of 100 to 180
 q=np.arange(100,180,5)

r=q.reshape(8,2)
r

# to print each and every set of 8*2 matrix having difference of 5 
a=[]
for i in range(100,125):
  j=i+16*5
  z=np.arange(i,j,5).reshape((8,2))
  a.append(z)
  
#Printing each matrix
for i in a:
  print(i)
