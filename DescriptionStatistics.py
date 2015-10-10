# -*- coding: utf-8 -*-
#!/usr/bin/python

# description statistics of dataset
# first: central tendency, including mean, median and mode
# second: discrete tendency, including range, quartile, standard variance and quartile deviation

import math

class DescriptionStatistics:
    
    """statistics of central tendency"""
    def mean(self,x):
        """average value of x"""
        total = 0
        average = 0
        n = len(x)
        for item in x:
            total += item
        average = float(total)/n
        return average

    def median(self,x):
        """median value of x"""
        n = len(x)
        try:
            x.sort()
            if n % 2 == 0:
                return float(x[n/2] + x[(n/2)-1])/2
            else:
                return x[int(n/2)]
        except:
            print "wrong median problem"

    def mode(self,x):
        """mode value of x"""
        dic = {}
        modes = []     # the number of mode can be more than one
        for item in x:
            if item not in dic.keys():
                dic[item] = x.count(item)
        for key in dic.keys():
            if dic[key] == max(dic.values()):
                modes.append(key)
        return modes

    """statistics of discrete tendency"""
    def range(self,x):
        """range value of x"""
        max = max(x)
        min = min(x)
        range = max - min
        return range

    def quartile(self,x):
        """quartile value of x"""
        x.sort()
        n = len(x)
        if n % 2 != 0:
            q1 = x[(n+1) * (1/4) - 1]
            q3 = x[(n+1) * (3/4) - 1]
        else:
            q1 = float(x[n/4-1] + x[n/4])/2
            q3 = float(x[3*n/4+1] + x[3*n/4])/2
        return q1,q3

    def quartile_deviation(self,x):
        """quartile deviation value of x"""
        q1, q3 = self.quartile(x)
        return (q3-q1)

    def variance(self,x):
        """variance value of x"""
        average = self.mean(x)
        sum = 0
        for num in x:
            sum += math.pow((num-average),2)
        return sum

    def standard_variance(self,x):
        """standard variance value of x"""
        variance = self.variance(x)
        return math.sqrt(variance)

