from scipy import *
from matplotlib.pyplot import *
from scipy.linalg import *
import scipy.special as sp
from scipy import mat, dot
from PIL import Image
import scipy.misc as misc
im=Image.open("test.jpg")
A = asarray(im)
misc.imsave("test1.jpg", A)
print A.shape
rows,cols,colors=A.shape
str=["red","green","blue"] # legends
figure(0)
d = 0.001
A1=zeros((rows,cols,3))
for i in range(3):
  matrix=A[:,:,i]
  U,s,V = svd(matrix,full_matrices=0)
  semilogy(s,'ro')
  l = s.max()
  ii=where(s<d*l);ii=ii[0]
  s[ii]=0
  print len(ii)/rows.__float__()
  A1[:,:,i]=dot(dot(U,diag(s)),V)
misc.imsave("test2.jpg", A1)
show()
show()
