import random
import numpy
import cv2
import Partition
import GeneralMethods
import PSNR


BlockSize = 8

string = input("msg : ")

str = "Hello bro, I am Ritam Chatterjee. I study in University Of Engineering and Management, Kolkata."

BinaryStr =  GeneralMethods.StringTOBinary(string)

img = cv2.imread("lena.png",0)

newImage = Partition.CreateBlocks(img,BlockSize,BinaryStr)

