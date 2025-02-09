
import numpy
import math

def decimalToBinary(n):
    return bin(n).replace("0b", "")

def getSize(img):
    c = 0
    r = 0
    for i in img:
        r += 1
    for i in img[0]:
        c += 1
    return r , c


def check(val,valstr,size):

    bin = str(decimalToBinary(val))

    for s in range(1,size+1):
        if(bin[-s] != valstr[-s]):
            return -999
    return val



def getDiComp(DArray,str):
    nArray = [1, 2, 3, 4, 5, 6, 7, 8]
    Range = [[0, 1], [2, 5], [6, 11], [12, 19], [20, 29], [30, 41], [42, 55], [56, 63]]
    mArray = [[[1]], [[2]], [[3],[2]], [[3]], [[4], [3]], [[4], [3]], [[4], [3]], [[4]]]
    SubRange = [[[0, 1]], [[2, 5]], [[6, 7], [8, 11]], [[12, 19]], [[20, 21], [22, 29]], [[30, 33], [34, 41]],
                [[42, 47], [48, 55]], [[56, 63]]]

    index = 0
    for s in range(0,8):
        if(DArray >= Range[s][0] and DArray <= Range[s][1]):
            index = s
            break

    n = nArray[index]
    embedStr = ""
    for l in range(0,len(mArray[index])):

        m = mArray[index][l]

        embedStr = ""
        for i in range(0, m[0]):
            embedStr = embedStr + str[i]

        subUpper = SubRange[index][l][1]
        subLower = SubRange[index][l][0]


        for i in range(subLower,subUpper+1):
            ans = check(i,embedStr,m[0])
            if(ans != -999):
                return ans,str[m[0]:]

    return 0,str[m[0]:]




def mod(a,b):
    c= a-b
    if(c < 0): c = c * -1
    return c





def getQiComp(Qi,QiP,Di,DiC):
    QiC = 0
    if(Qi >= QiP and DiC > Di):
        QiC = QiP - math.floor(mod(Di,DiC)/2)
        Qi = Qi + math.ceil(mod(Di,DiC)/2)
    elif(Qi < QiP and DiC > Di):
        QiC = QiP + math.ceil(mod(Di, DiC) / 2)
        Qi = Qi - math.floor(mod(Di, DiC) / 2)
    elif(Qi >= QiP and DiC <= Di):
        QiC = QiP + math.floor(mod(Di, DiC) / 2)
        Qi = Qi - math.ceil(mod(Di, DiC) / 2)
    elif(Qi < QiP and DiC <= Di):
        QiC = QiP - math.floor(mod(Di, DiC) / 2)
        Qi = Qi + math.ceil(mod(Di, DiC) / 2)

    if Qi > QiC:
        if Qi >=64:
            QiC = QiC - (Qi-63)
            Qi = 63
        elif QiC < 0:
            Qi = Qi + (QiC * -1)
            QiC = 0
    else:
        if Qi < 0:
            QiC = QiC + (Qi * -1)
            Qi = 0
        elif QiC >= 64:
            Qi = Qi - (QiC - 63)
            QiC = 63

    return Qi,QiC




def Define(block,msg) :
    nArray = [1,2,3,4,5,6,7,8]
    Range = [[0,1],[2,5],[6,11],[12,19],[20,29],[30,41],[42,55],[56,63]]
    mArray = [[1],[2],[3,2],[3],[4,3],[4,3],[4,3],[4]]
    SubRange = [[[0,1]],[[2,5]],[[6,7],[8,11]],[[12,19]],[[20,21],[22,29]],[[30,33],[34,41]],[[42,47],[48,55]],[[56,63]]]

    strCompleted = 0

    Coloumn,row = getSize(block)

    QArray = numpy.zeros((Coloumn,row),dtype=int)
    QcArray = numpy.zeros((Coloumn,row),dtype=int)



    DArray = numpy.zeros((Coloumn,int((row/2))),dtype=int)
    DcArray = numpy.zeros((Coloumn,int((row/2))),dtype=int)

    k=0
    for i in range(0,Coloumn):
        for j in range(0,row,2):
            QArray [i][j] = math.floor(block [i][j] / 4)
            QArray [i][j+1] = math.floor(block [i][j+1] / 4)

            DArray [i][k] = mod(QArray[i][j],QArray [i][j+1])              # Computing the Di
            DcArray[i][k],msg = getDiComp(DArray[i][k],msg)                # Computiong Di'
            QcArray[i][j],QcArray[i][j+1] = getQiComp(QArray[i][j],QArray [i][j+1],DArray[i][k],DcArray[i][k])        # Computing Qi'
            k=k+1
        k=0

    return QcArray,msg







def getExtracedMessage(DiC):
    nArray = [1, 2, 3, 4, 5, 6, 7, 8]
    Range = [[0, 1], [2, 5], [6, 11], [12, 19], [20, 29], [30, 41], [42, 55], [56, 63]]
    mArray = [[[1]], [[2]], [[3], [2]], [[3]], [[4], [3]], [[4], [3]], [[4], [3]], [[4]]]
    SubRange = [[[0, 1]], [[2, 5]], [[6, 7], [8, 11]], [[12, 19]], [[20, 21], [22, 29]], [[30, 33], [34, 41]],
                [[42, 47], [48, 55]], [[56, 63]]]

    index = 10
    m = 10
    for i in range(0,8):
        for j in range(0,len(SubRange[i])):
            if(DiC >= SubRange[i][j][0] and DiC <= SubRange[i][j][1]):
                index = i
                m = mArray[i][j][0]
                break

    if(m != 10 and index!=10):
        bin = str(decimalToBinary(DiC))
        ExtratedStr = bin[-m:]

        return ExtratedStr

    return ""



def extractQuotentMatrix(img):

    msg = ""

    Coloumn, row = getSize(img)

    QcArray = numpy.zeros((Coloumn, row), dtype=int)

    DcArray = numpy.zeros((Coloumn, int((row / 2))), dtype=int)

    k = 0
    for i in range(0, Coloumn):
        for j in range(0, row, 2):
            QcArray[i][j] = math.floor(img[i][j] / 4)
            QcArray[i][j + 1] = math.floor(img[i][j + 1] / 4)
            DcArray[i][k] = mod(QcArray[i][j], QcArray[i][j + 1])  # Computing the Di'
            newMsg = getExtracedMessage(DcArray[i][k])  # Computiong Di'
            msg = msg + newMsg
            k = k + 1
        k = 0

    return msg
