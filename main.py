import random
import numpy
import cv2
import Partition
import GeneralMethods
import PSNR


BlockSize = 8

string = input("msg : ")

str = "This is a Secret messafe, I Will Encrypt this inside an Image."

BinaryStr =  GeneralMethods.StringTOBinary(string)

img = cv2.imread("lena.png",0)  # Add a PNG Image to directory to embed into.

newImage = Partition.CreateBlocks(img,BlockSize,BinaryStr)

