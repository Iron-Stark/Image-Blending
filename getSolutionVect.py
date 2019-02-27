'''
  File name: getSolutionVect.py
  Author:  Dewang Sultania
  Date created: 09/28/2018
'''



from scipy import signal
import numpy as np
def getSolutionVect(indexes, source, target, offsetX, offsetY):
    #Enter Your Code Here
    size = indexes[indexes>0].shape[0]
    M = [[0,-1,0],
        [-1,4,-1],
        [0,-1,0]]
    sourceLaplacian = signal.convolve2d(source, M, mode = 'same',boundary = 'symm')
    sourceEnlarged = np.zeros((target.shape[0],target.shape[1]))
    sourceEnlarged[offsetY:offsetY+sourceLaplacian.shape[0],offsetX:offsetX+sourceLaplacian.shape[1]] = sourceLaplacian
    SolVectorb = sourceEnlarged[indexes>0]
    SolVectorb = np.reshape(SolVectorb,size)
    indexespad = np.pad(indexes.copy(), ((1,1),(1,1)),'constant',constant_values = 0)
    targetCopy = np.pad(target.copy(), ((1,1),(1,1)),'constant',constant_values = 0)
    xx, yy = np.meshgrid(range(indexespad.shape[0]),range(indexespad.shape[1]),indexing='ij')
    neigh = np.zeros((4,size))
    i,j = np.where(indexes!=0)
    targetCopy[i,j] = 0
    neigh[0,:] = targetCopy[i+1,j]
    neigh[1,:] = targetCopy[i-1,j]
    neigh[2,:] = targetCopy[i,j-1]
    neigh[3,:] = targetCopy[i,j+1]
    SolVectorb += neigh[0,:] + neigh[1,:] + neigh[2,:] + neigh[3,:]
    return SolVectorb
