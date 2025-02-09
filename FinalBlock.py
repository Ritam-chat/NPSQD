import numpy


def getSize(img):
    c = 0
    r = 0
    for i in img:
        r += 1
    for i in img[0]:
        c += 1
    return r , c


def Construct(QArray,RArray):
    Coloumn,row = getSize(QArray)

    NewImage = numpy.zeros((Coloumn,row),dtype=int)

    for i in range(0,Coloumn):
        for j in range(0,row):
            NewImage [i][j] = (QArray [i][j] * 4) + RArray [i][j]
            # if NewImage[i][j]> 255 or NewImage[i][j] < 0:
            #     print(NewImage[i][j])
    return NewImage
