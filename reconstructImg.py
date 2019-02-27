'''
  File name: reconstructImg.py
  Author:  Dewang Sultania
  Date created: 09/28/2018
'''



import numpy as np
import matplotlib.pyplot as plt
def reconstructImg(indexes, red, green, blue, targetImg):
    resultImg = targetImg.copy()
    resultImg[:,:,0][np.where(indexes!=0)] = red
    resultImg[:,:,1][np.where(indexes!=0)] = green
    resultImg[:,:,2][np.where(indexes!=0)] = blue
    return resultImg
