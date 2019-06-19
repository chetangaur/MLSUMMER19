import numpy as np
from tempfile import TemporaryFile
print("Enter number of rows")
R=int(input())
print("Enter number of coloumn ")
C=int(input()) 
N=[]
N=np.random.randint(1,9,R*C)
matrix = np.array(N).reshape(R, C) 
print(matrix)
f1 = TemporaryFile()
np.save(f1, matrix)
f1.seek(0)
np.load(f1)
