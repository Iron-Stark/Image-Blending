'''
  File name: getCoefficientMatrix.py
  Author: Dewang Sultania
  Date created: 09/27/2018
'''

import numpy as np

def getCoefficientMatrix(indexes):
    #Enter Your Code Here
    coeffA = np.zeros((np.amax(indexes).astype(int),np.amax(indexes).astype(int)+1))
    index_rows = indexes.shape[0]
    index_cols = indexes.shape[1]
    np.fill_diagonal(coeffA,4)
    xx, yy = np.meshgrid(range(indexes.shape[0]),range(indexes.shape[1]),indexing='ij')
    indexespad = np.pad(indexes.copy(), ((1,1),(1,1)),'constant',constant_values = 0)
    row_down = indexespad[xx,yy+1]
    row_up = indexespad[xx+2,yy+1]
    col_right = indexespad[xx+1,yy]
    col_left = indexespad[xx+1,yy+2]
    i,j = np.where(indexes!=0)
    coeffA[indexes[i,j].astype(int)-1,row_up[i,j].astype(int)-1] = -1
    coeffA[indexes[i,j].astype(int)-1,row_down[i,j].astype(int)-1] = -1
    coeffA[indexes[i,j].astype(int)-1,col_left[i,j].astype(int)-1] = -1
    coeffA[indexes[i,j].astype(int)-1,col_right[i,j].astype(int)-1] = -1
    coeffA = coeffA[:,:-1]
    return coeffA
