
import numpy
import math

def getSize(img):
    c = 0
    r = 0
    for i in img:
        r += 1
    for i in img[0]:
        c += 1
    return r , c


def decimalToBinary(n):
    return bin(n).replace("0b", "")

def binaryToDecimal(n):
    return int(n,2)

def getRcArray(arr,Msg):
    Coloumn,row = getSize(arr)
    Arr = arr.copy()
    k = 0
    for i in range(0,Coloumn):
        for j in range(0,row):
            m1 =  Msg[k]
            m2 = Msg[k+1]
            number = m1 + m2
            Arr[i][j] =  binaryToDecimal(number)
            k = k+2
    return Arr,Msg[k:]



def Remainder_Embedding(Image,Message):

    Coloumn, row = getSize(Image)

    rArray = numpy.zeros((Coloumn,row),dtype=int)

    for i in range(0,Coloumn):
        for j in range(0,row):
            rArray [i][j] = Image[i][j] % 4

    RcArray,Message = getRcArray(rArray,Message)
    return RcArray,Message

