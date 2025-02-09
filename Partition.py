import GeneralMethods
import QuotentEmbedding
import RemainderEmbedding
import FinalBlock
import random
import numpy



def ReplaceBlock(NewImage,newBlock,i,j,Size):
    row, col = GeneralMethods.GetSize(NewImage)
    x, y = Size-1, Size-1
    for I in range(i, -1, -1):
        for J in range(j, -1, -1):
            NewImage[I][J] = newBlock[x][y]
            if x == 0 and y == 0:
                return NewImage
            if y == 0:
                y = Size
                x -= 1
            y -= 1
            if J == 0: j = row - 1
        if I == 0: i = col - 1
    return NewImage


def getSequence(rowCount, colCount, size):
    seed = rowCount*colCount
    Size = (size * size)
    sequence = list()
    for i in range(0,Size,2):
        sequence.append(i)
    random.seed(seed)
    random.shuffle(sequence)
    return sequence



def ReShuffle(newblock,sequence,size):
    Size = size * size
    block = numpy.zeros(Size, dtype=int)
    index = 0
    Block = newblock.ravel()
    for n in range(0,Size,2):
        i = sequence.index(n)
        block[index] = Block[i*2]
        block[index+1] = Block[(i*2)+1]
        index += 2
    block.resize((size,size))
    return block

def ShuffleBlock(block, sequence, Size):
    newblock = numpy.zeros((Size, Size), dtype=int)

    ind = 0
    block = block.ravel()
    for i in range(0, Size):
        for j in range(0, Size, 2):
            newblock[i][j] = block[sequence[ind]]
            newblock[i][j + 1] = block[sequence[ind] + 1]
            ind += 1
    return newblock


def CreateBlocks(Image,PartisionCount,Message):

    rowCount , colCount = GeneralMethods.GetSize(Image)

    sequence = getSequence(rowCount,colCount,PartisionCount)
    newImage = Image.copy()
    block = numpy.zeros((PartisionCount,PartisionCount),dtype=int)
    x , y = 0 , 0
    for i in range(0,colCount):
        for j in range(0,rowCount):
            block[x][y] = Image[i][j]
            if y == PartisionCount-1:
                y = -1
                x += 1
            if y == -1 and x == PartisionCount:

                block = ShuffleBlock(block,sequence,PartisionCount)
                newQBlock , Message = QuotentEmbedding.Define(block,Message)

                # if (len(Message) % 8 != 0):
                #     while (len(Message) % 8 != 0): Message = Message[1:]

                newRBlock , Message = RemainderEmbedding.Remainder_Embedding(block,Message)
                newBlock = FinalBlock.Construct(newQBlock,newRBlock)

                newBlock = ReShuffle(newBlock,sequence,PartisionCount)
                newImage = ReplaceBlock(newImage,newBlock,i,j,PartisionCount)
                block = numpy.zeros((PartisionCount, PartisionCount), dtype=int)
                x , y = 0 , -1
            y += 1

    return newImage


