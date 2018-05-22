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
import random
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

# random centroid
def rand_centroid(df, k):
    dim = df.ndim
    list_cen = []
    for i in range(k):
        for j in range(dim):
            rand_centroid = random.choice(df.iloc[:,j])
            list_cen.append(rand_centroid)
    out = pd.DataFrame(np.array(list_cen).reshape(k,dim),
                      columns = df.columns)
    return out

# calculate distance each centroid
def dist_centroids(df, centroids):
    dim = df.ndim
    list_dist = []
    for centroid in centroids:
         dist(df, centroid)

