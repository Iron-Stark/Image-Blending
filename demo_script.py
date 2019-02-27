import numpy as np
import matplotlib.pyplot as plt
import os
from PIL import Image
import time

from getIndexes import getIndexes
from getCoefficientMatrix import getCoefficientMatrix
from getSolutionVect import getSolutionVect
from seamlessCloningPoisson import seamlessCloningPoisson
from mask_creator import mask_creator
from reconstructImg import reconstructImg
if __name__=="__main__":
    sourceImage = Image.open('source.png').convert('RGB')
    targetImage = Image.open('target.png').convert('RGB')
    #mask = mask_creator(sourceImage.convert('L'))
    offsetX = 0
    offsetY = 0
    #mask = np.array(Image.open('mask1.png').convert('L'))
    mask = mask_creator(sourceImage.convert('L'))
    plt.imshow(mask)
    plt.show()

    sourceImage = np.array(sourceImage)
    targetImage = np.array(targetImage)
    #print(targetImage.shape)
    #print(sourceImage.shape)
    indexes = getIndexes(mask, targetImage.shape[0],targetImage.shape[1],offsetX,offsetY)
    coeffA = getCoefficientMatrix(indexes)
    redChannelSource, redChannelTarget = sourceImage[:,:,0], targetImage[:,:,0]
    blueChannelSource, blueChannelTarget = sourceImage[:,:,2], targetImage[:,:,2]
    greenChannelSource, greenChannelTarget =  sourceImage[:,:,1], targetImage[:,:,1]
    redSolVectorb = getSolutionVect(indexes, redChannelSource, redChannelTarget, offsetX,offsetY)
    redFinalimg = seamlessCloningPoisson(redChannelSource, redChannelTarget, mask, offsetX,offsetY)
    blueSolVectorb = getSolutionVect(indexes, blueChannelSource, blueChannelTarget, offsetX,offsetY)
    blueFinalimg = seamlessCloningPoisson(blueChannelSource, blueChannelTarget, mask, offsetX,offsetY)
    greenSolVectorb = getSolutionVect(indexes, greenChannelSource, greenChannelTarget, offsetX,offsetY)
    greenFinalimg = seamlessCloningPoisson(greenChannelSource, greenChannelTarget, mask, offsetX,offsetY)
    finalimg = reconstructImg(indexes, redFinalimg, greenFinalimg, blueFinalimg, targetImage)
    plt.imshow(finalimg)
    plt.show()
