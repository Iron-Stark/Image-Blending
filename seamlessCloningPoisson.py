'''
  File name: seamlessCloningPoisson.py
  Author: Dewang Sultania
  Date created: 09/29/2018
'''


from getIndexes import getIndexes
from getCoefficientMatrix import getCoefficientMatrix
from getSolutionVect import getSolutionVect
import numpy as np
from scipy.sparse import csc_matrix
from scipy.sparse.linalg import spsolve
def seamlessCloningPoisson(sourceImg, targetImg, mask, offsetX, offsetY):
    indexes = getIndexes(mask, targetImg.shape[0],targetImg.shape[1],offsetX,offsetY)
    coeffA = getCoefficientMatrix(indexes)
    SolVectorb = getSolutionVect(indexes, sourceImg, targetImg, offsetX, offsetY)
    coeffA = csc_matrix(coeffA)
    f = spsolve(coeffA,SolVectorb)
    f[f<=0] = 0
    f[f>255] = 255
    f = np.array(f, dtype = np.uint8)
    return f
