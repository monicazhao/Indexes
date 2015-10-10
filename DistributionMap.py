# -*- coding: utf-8 -*-
#!/usr/bin/python

# The followings display kinds of distribution map
# such as scatter diagram, quantile plot and box plot

import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

                                                       
class DistributionMap:

    def __init__(self):
        #初始化DistributionMap类时设置的绘图格式
        mpl.rcParams['font.family'] = 'sans-serif'
        mpl.rcParams['font.sans-serif'] = [u'SimHei']

    def drawBoxPlot(self,x):
        #输入一组数据，返回对应的盒图
        
