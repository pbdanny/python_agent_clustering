#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 22 05:20:36 2018

@author: Danny
"""

"""
K-mean clustering from therory
1. Random k centroid
2. Calculate distance each centroid - each datapoint
3. Assign datapoint to closest centroid = k cluster
4. Calculate new centroid from avg distance of each k cluster
5. Back to 2. until change in each cluster so minimal
"""
import os
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

# read test data
df = pd.read_csv('xclara.csv')
df.shape
df.head(3)

# plot data
df.plot.scatter(x = 'V1', y = 'V2', s = 1)

# Euclidean distance
def dist(df, centroid):
    return (df - centroid).pow(2).sum(axis = 'columns').pow(1/2)