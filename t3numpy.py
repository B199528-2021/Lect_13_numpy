#!/usr/local/bin/python3

import os, subprocess, shutil

input_seqs = ['ATTGTACGG', 'AATGAACCG', 'AATGAACCC', 'AATGGGAAT']

s=''
myseqs=s.join(str(e) for e in input_seqs)

import numpy as np
import numpy

# Both commands are the same, they are just creating arrays with different names
o = numpy.array([[1,2,3],[4,5,6]])
a = np.array([[1,2,3],[4,5,6]])

# Create a 12 by 4 array of all zeros
b = np.zeros((12,4))

# Create a 5 by 2 array of all ones
c = np.ones((5,2))

# Create a 3 by 2 array with all values being 6
d = np.full((3,2), 6)

# Create a 2 by 2 array filled with random (floating point) values
e = np.random.random((2,2))

# Create a 3 by 3 identity matrix
f = np.eye(3)

IDmatrix = np.eye(len(myseqs),dtype=int)

xcounter=0

for xbase in myseqs :
   xcounter+=1
   ycounter=0
   for ybase in myseqs :
     ycounter+=1
     print(xcounter,ycounter,xbase,ybase)
     if ybase==xbase :
       IDmatrix[(xcounter-1),(ycounter-1)]=1

print(IDmatrix[0:9,0:9])

print(IDmatrix[0:18,0:18])

print("The similarity was",int((IDmatrix[0:9,9:18].diagonal().sum()/9)*100),"percent")



