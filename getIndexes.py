'''
  File name: getIndexes.py
  Author:   Dewang Sultania
  Date created: 09/27/2018
'''

import numpy as np


def getIndexes(mask, targetH, targetW, offsetX, offsetY):
    # Enter Your Code Here
    indexes = np.zeros((targetH,targetW))
    maskrows, maskcols = mask.shape
    mask = mask.flatten()
    mask = mask.astype(int)
    noOfOnes = np.where(mask!=0)[0].shape[0]
    np.put(mask,np.where(mask!=0)[0], range(1,noOfOnes+1))
    mask = np.reshape(mask,(maskrows,maskcols))
    indexes[offsetY:offsetY+maskrows,offsetX:offsetX+maskcols] = mask
    return indexes
