0# -*- coding: utf-8 -*-
"""
Created on Fri Apr 19 08:20:58 2024
#test on monday python,advance python,pandas,numpy
@author: Vaishnavi
"""
#use stack overflow to find what is the error and what does it mean
#19-04-2024
#numpy is also used when we want to crop the image and again reset it to original dimension
#numpy is used in image processing
#the 1 dimensional array is called as 1-d array
#mul
import numpy as np
multi_arr=np.array([[10,20,10,40],[40,50,70,90],
                    [60,10,70,80],[30,90,40,30]])
multi_arr
multi_arr[1,2]
multi_arr[:3]


#integer array indexing
arr=np.arange(35).reshape(5,7)
print(arr)


#boolean array indexing
import numpy as np
#boolean array indexing
arr=np.arange(12).reshape(3,4)
print(arr)
"""[[ 0  1  2  3]
 [ 4  5  6  7]
 [ 8  9 10 11]]"""
rows=np.array([False,True,True])#here 0th row will be omitted 
rows
wanted_rows=arr[rows,:]#here rows will be of our choice but columns will be all as : is for column
print(wanted_rows)
"""[[ 4  5  6  7]
 [ 8  9 10 11]]"""

#convert array
list=[20,40,60,80]
array=np.array(list)
print("array",array)
"""array [20,40,60,80]"""
#use asarray
list=[20,40,60,80]
array=np.asarray(list)
print("array",array)
print(type(array))
"""array [20 40 60 80]
<class 'numpy.ndarray'>
"""
#ndarray.itemsize
#ndaray.size
#ndarray.dtype

#ndarray.shape
#to get the shape of a python numpy array use numpy
#shape
array=np.array([[1,2,3],[4,5,6]])
array
print(array.shape)
"""(2, 3)"""

array=np.array([[10,20,30],[40,50,60]])
array.shape=(3,2)
print(array)
"""[[10 20]
 [30 40]
 [50 60]]"""

#numpy also provides a numpy.reshape( )function
#numpy usage

#reshape
array=np.array([[10,20,30],[40,50,60]])
new_array=array.reshape(3,2)#3 rows and 2 columns
print(new_array)
"""[[10 20]
 [30 40]
 [50 60]]"""

#arithmetic operations

arr1=np.arange(16).reshape(4,4)
arr2=np.array([1,3,2,4])

#ADD
#add()
add_arr=np.add(arr1,arr2)
print(f"adding two arrays:\n{add_arr}")
#adding two arrays:
""" [[ 1  4  4  7]#here 1st column will be adding 1
     [ 5  8  8 11]#2nd column will be adding 3
     [ 9 12 12 15]#3rd column will be adding 2 in it
     [13 16 16 19]]#4th column will be adding 4 to it 
    #as arr2 contains 1 column 
"""
#substract()
sub_array=np.subtract(arr1,arr2)
print(f"substracting two array:\n{sub_array}")
"""[[-1 -2  0 -1]
 [ 3  2  4  3]
 [ 7  6  8  7]
 [11 10 12 11]]"""
    
#multiply()
mul_arr=np.multiply(arr1,arr2)
print(f"multiplication of two arrays:\n{mul_arr}")
"""[[ 0  3  4 12]
 [ 4 15 12 28]
 [ 8 27 20 44]
 [12 39 28 60]]"""

    #divide()
div_arr=np.divide(arr1,arr2)
print(f"dividing two arrays:\n{div_arr}")
"""dividing two arrays:
[[ 0.          0.33333333  1.          0.75      ]
 [ 4.          1.66666667  3.          1.75      ]
 [ 8.          3.          5.          2.75      ]
 [12.          4.33333333  7.          3.75      ]]"""

#numpy.reciprocal()
#this function returns the reciprocsl of the argumnet


#to perform reciprocal operation
arr1=np.array([50,10.3,5,1,100])
rep_arr1=np.reciprocal(arr1)
print(f"after applyinng reciprocal {rep_arr1}")
"""after applyinng reciprocal [0.02       0.09708738 0.2        1.         0.01      ]"""


#numpy.power()
#this numpy power() function treats elements in the first input as each having power

#to perform power operation
arr1=np.array([3,10,5])
pow_arr=np.power(arr1,3)
print(pow_arr)
"""[  27 1000  125]"""

arr1=np.array([3,10,5])
arr2=np.array([3,2,1])
print("my array is:",arr2)
pow_arr2=np.power(arr1,arr2)
print(f"array is{pow_arr2}")
"""array is[ 27 100   5]"""

#to perform mod operation
#on numpy array
import numpy as np
arr1=np.array([7,20,13])
arr2=np.array([3,5,2])
arr1
arr1.dtype
"""dtype('int32')"""
#mod()
mod_arr=np.mod(arr1,arr2)
print(f"the array is:\n{mod_arr}")
"""the array is:
[1 0 1]"""

#create empty array
from numpy import empty
a=empty([3,3])
print(a)
"""[[0. 0. 0.]
 [0. 0. 0.]
 [0. 0. 0.]]"""
###########################################
    #create zero array
from numpy import zeros
a=zeros([3,5])
print(a)
#################33
import numpy as np
np.__version__
# '1.26.4'

##########################
#create one array
#1-d and 0-array is used in eigen value and eigen vector
from numpy import ones
a=ones([5])
print(a)
"""[1. 1. 1. 1. 1.]"""
#create array with vstack
from numpy import array
from numpy import vstack
#create 1st array
a1=array([1,2,3])
print(a1)
#create 2nd array
a2=array([4,5,6])
print(a2)
#vertical stack
a3=vstack((a1,a2))
print(a3)
print(a3.shape)
"""[[1 2 3]
 [4 5 6]]
(2, 3)"""
from numpy import array
from numpy import hstack
#create 1st array
a1=array([1,2,3])
print(a1)
#create 2nd array
a2=array([4,5,6])
print(a2)
#create horizontal stack
a3=hstack((a1,a2))
print(a3)
print(a3.shape)
"""[1 2 3 4 5 6]
(6,)"""

##############################################
#23-04-2024

#index array out of bounds
from numpy import array
#define array
data=array([11,22,33,44,55])
#index data
print(data[5])
#index 5 is out of bound
#it gives us the error as array out of bound

#index data
print(data[0,0])
##################################
#index row of two dimensional array
from numpy import array
#define array
data=array([
    [11,12],
    [33,44],
    [55,66]])
#index data
print(data[0,])
#oth row and all columns 
"""[11 12]"""
#########################################
#slice a one dimensional array
from numpy import array
#define array
data=array([11,22,33,44,55])
print(data[-2:])
"""[44 55]"""

################################
#split input and output data
from numpy import array
#define array
data=array([
    [11,22,33],
    [44,55,66],
    [77,88,99]])
#   x_____,y
#separate data
x,y=data[:,:-1],data[:,-1]
#here we will get x as all rows and upto -1 slicing is done for columns
#so....-3 -2 positions will be in the x
#and all rows and -1 column will be in the y field
x
y

#so here we use for x as the features and y as labels

#########################################33
#broadcast scalar to one dimensional array
"""important"""
from numpy import array
#define array
a=array([1,2,3])
print(a)
#define scalar
b=2
print(b)
#broadcast
c=a+b
print(c)
"""[3 4 5]"""
#here each element will be added with the scalar
#########################################33
"""vector L1Norm
The L1 norm is calculated as the sum of the 
absolute vector values,where  the absolute values of
a scalar uses the notation |a1|.
in effect , the norm is a 
calculation of the manhattan distance
from the origin of the vector space.

||v||1=|a1|+|a2|+|a3|
...
"""
#we are going to use it in euclinity norm.....l1 and l2 norm
#suppose amazon are given the reviews so it will be in the text form 
#so converting into the numeric form we will get the ratings or reviews 
from numpy import array
from numpy.linalg import norm
#define vector
a=array([1,2,3])
print(a)
#calculate norm
l1=norm(a,1)
print(l1)
"""6.0"""
###################################
#vector l2 norm
"""l2norm =sqroot of x1^2+x2^2+x3^2

the notation for the l2 norm of a vector
x is ||x|| power of 2
to calculate the l2 norm of a vector ,
take the squareroot of the sum of the sqaured vector values
another name for l2 of a norm vector is euclidean distance
this is often used for calculating the error in machin learning"""
from numpy import array
from numpy.linalg import norm #linag is a linear algebra
a=array([1,2,3])
#define a vector
print(a)
#calculating the norm
l2=norm(a)#1+4+9 underroot of 14 is 3.74
print(l2)
"""3.7416573867739413"""
#####################################
#triangular matrices
#it is used in image processing for cropping of image anf enlarging of the image

from numpy import array
from numpy import tril
from numpy import triu
#define square matrix
m=array([[1,2,3],
        [1,2,3],
        [1,2,3]])
print(m)
"""[[1 2 3]
   [1 2 3]
  [1 2 3]]"""#here comma will not be thee as we have printed it 
    #if weuse print then the specific format will be displayed
m
"""array([[1, 2, 3],
       [1, 2, 3],
       [1, 2, 3]])"""
    #if we just give the variable as it is then it will directly write the as it content of that variable here eg is m
#lower triangular matrix
lower=tril(m)
print(lower)
#upper triangular matrix
upper=triu(m)
print(upper)
"""[[1 2 3]
 [1 2 3]
 [1 2 3]]
[[1 0 0]
 [1 2 0]
 [1 2 3]]
[[1 2 3]
 [0 2 3]
 [0 0 3]]"""

#######################################3
#diagonal matrix
from numpy import array
from numpy import diag
#define square matrix
m=array([[1,2,3],
        [1,2,3],
        [1,2,3]])
print(m)
#extract diagonal vector
d=diag(m)
print(d)
#create diagonal matrix from vector
D=diag(d)
print(D)
"""[[1 0 0]
 [0 2 0]
 [0 0 3]]"""
###########################
#identity matrix
from numpy import identity
I=identity(3)
print(I)
"""[[1. 0. 0.]
 [0. 1. 0.]
 [0. 0. 1.]]"""
################################
#ORTHOGONAL MATRIX
"""the matrix is said to be an orthogonal matrix 
if the product of a matrix and its transpose gives
an identity value"""
from numpy import array
from numpy.linalg import inv
#define orthogonal matrix
q=array([[1,0],
        [0,-1]]) 
print(q)
#inverse equivalence
v=inv(q)
print(q.T)#here T is the transpose
print(v)
"""[[ 1  0]
 [ 0 -1]]
[[ 1.  0.]
 [-0. -1.]]"""
#identity equivalence
I=q.dot(q.T)
print(I)
"""[[1 0]
 [0 1]]"""
  ##########################
#24-04-2024
from numpy import array
#define matrix
# =============================================================================
a=array([[1,2],[3,4],[5,6]])
print(a)
c=a.T
#calculate transpose
print(c)
"""[[1 3 5]
 [2 4 6]]"""
# =============================================================================
#inverse matrix
from numpy import array
from numpy.linalg import inv
#define matrix
a=array([
    [1.0,2.0],
    [3.0,4.0]])
print(a)
#inverse of matrix
b=inv(a)
print(b)
"""[[-2.   1. ]
 [ 1.5 -0.5]]"""
#######################################
#multiply a and b
#a *a^-1(a into a inverse is I)
I=a.dot(b)
print(I)
"""[[1.00000000e+00 1.11022302e-16]
 [0.00000000e+00 1.00000000e+00]]"""
###################################3
#sparse matrix
#it is a matrix consist of some values in the row and remaining wil be having values as zero
from numpy import array
from scipy.sparse import csr_matrix
#create dense matrix
a=array([[1,0,0,1,0,0],
         [0,0,2,0,0,1],
         [0,0,0,2,0,0]])
print(a)
#construct to sparse matrix(csr method)
s=csr_matrix(a)
print(s)
"""(0, 0)	1
(0, 3)	1
(1, 2)	2
(1, 5)	1
(2, 3)	2"""
#reconstruct the dense matrix ie the original matrix
b=s.todense()
print(b)
"""[[1 0 0 1 0 0]
 [0 0 2 0 0 1]
 [0 0 0 2 0 0]]"""



