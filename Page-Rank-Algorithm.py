import numpy as np
import numpy.linalg as la
from readonly.PageRankFunctions import *
np.set_printoptions(suppress=True)
#fn to applay page rank algorthm 
#linkMatrix is matrix whis each row idicates no of links refer to websites divided by no of links these sites refers to
#d here is a number taking randomly ti indicates the user will choose the webiste and (1-d) is the website is viewing randomly
def pageRank(linkMatrix, d) :
# n here is our internet size of websites
    n = linkMatrix.shape[0]
#M here is the matrix applying for our rank vector ang J is matrin nXn of ones
    M=d*linkMatrix+((1-d)/n)*np.ones([n,n])
'''The multiplication by 100 is not done for "scaling" purpose.
Assume that there are a total of 100 surfers in the network. 
Given the probability vector, the no of surfers each n webpage
 '''
 r=100*np.ones(n)/n
    lastR=r
    r=M@r
    i=0
    while la.norm(lastR-r)>0.01:
        lastR=r
        r=M@r
        i+=1
    print(str(i) + " iterations to convergence.")    
    return r 
#Alg is faster for large internet
#calculating the eigenvalues of the link matrix, M,
eVals, eVecs = la.eig(M) # Gets the eigenvalues and vectors
order = np.absolute(eVals).argsort()[::-1] # Orders them by their eigenvalues
eVals = eVals[order]
eVecs = eVecs[:,order]
%pylab notebook
r = pageRank(generate_internet(100), 0.9)
plt.bar(arange(r.shape[0]), r);
r = eVecs[:, 0]
100 * np.real(r / np.sum(r))
%pylab notebook
r = pageRank(generate_internet(100), 0.9)
plt.bar(arange(r.shape[0]), r);
