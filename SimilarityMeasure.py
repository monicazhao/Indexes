# -*- coding: cp936 -*-
#计算数据行列之间的相似性

import math

class SimilarityMeasure():

    def Manhattan(self,x,y):
        """Computing Manhattan Distance Value Between x And y"""
        if(len(x) != len(y)):
            return "invalid length of array"
        else:
            manhattan = 0
            for i in range(len(x)):
                manhattan += abs(x[i]-y[i])
            return manhattan

    def Euclidean(self,x,y):
        """Computing Euclidean Distance Value Between x And y"""
        if(len(x) != len(y)):
            return "invalid length of array"
        else:
            euclidean = 0
            total = 0
            for i in range(len(x)):
                total += math.pow(x[i]-y[i],2)
            euclidean = math.sqrt(total)
            return euclidean

    def Minkowski(self,p,x,y):
        """Computing Minkowski Distance Value Between x And y"""
        if (len(x) != len(y)):
            return "invalid length of array"
        else:
            if (p < 1):
                return "valid value of parameter"
            else:
                if (p == 1):
                    return self.Manhattan(x,y)
                elif (p == 2):
                    return self.Euclidean(x,y)
                else:
                    total = 0
                    for i in range(len(x)):
                        ele = abs(x[i]-y[i])
                        total += math.pow(ele,p)
                    minkowski = math.pow(total,(1.0/p))
                    return minkowski

    def Cosine(self,x,y):
        """Computing Cosine Distance Value Between x And y"""
        if(len(x) != len(y)):
            return "invalid length of array"
        else:
            total_x = 0
            total_y = 0
            total_xy = 0
            for i in range(len(x)):
                total_x += math.pow(x[i],2)
                total_y += math.pow(y[i],2)
                total_xy += x[i] * y[i]
            return (total_xy)/(math.sqrt(total_x)*(math.sqrt(total_y)))

    def Supremum(self,x,y):
        """Computing Supremum Distance Value Between x And y"""
        if(len(x) != len(y)):
            return "invalid length of array"
        else:
            rangeList = []
            for i in range(len(x)):
                temp = abs(x[i]-y[i])
                rangeList.append(temp)
            return max(rangeList)

        
if __name__ == "__main__":
    x = [8,0,3,0,2,0,0,2,0,0]
    y = [3,0,2,0,1,1,0,1,0,1]
    similarityMeasure = SimilarityMeasure()
    print similarityMeasure.Supremum(x,y)
