import csv
import matplotlib.pyplot as plt
from math import sqrt
import random


from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np

print("K-Means Clustering Algorithm")


def euclideanDist(row1,row2):
    distance = 0.0
    for i in range(0,len(row1)-1):
        distance += (row1[i] - row2[i])**2
    return sqrt(distance)


def manhattanDist(row1,row2):
    distance = 0.0
    for i in range(0,len(row1)-1):
        distance += abs(row1[i] - row2[i])
    return distance


def countDistance(data,point):
    # distance between the "point" and all "point" in dataset

    distArr=[]
    for row in data:
        distArr.append(manhattanDist(row,point)) # Using manhattan distance
    return distArr


def findMin(arr):
    return arr.index(min(arr))

def updateCluster(arrPointCluster,data):

    distArr=[]
    for i in range(len(data)):

        # distance between row in data set and [point1, point2,...]

        arrDist=[]
        for point in arrPointCluster:
            arrDist.append(manhattanDist(data[i],point))

        # [dist1,dist2,...]
        # then find the minimum value, and save the index

        # save cluster 0,1,2 dst..
        data[i][3]=findMin(arrDist)

    return data

def eliminateDataset(data,clusterIdx):
    newDataset=[]
    for row in data:
        if(row[3]==clusterIdx):
            newDataset.append(row)

    return newDataset

def makeNewCenter(data):
    newPoint=[]

    for i in range(3):
        a=0.0
        for row in data:
            a+=row[i]
        
        a/=len(data)
        newPoint.append(a)

    return newPoint

def updateCenterOfCluster(data,arrPointCluster):
    for i in range(len(arrPointCluster)):
        a = eliminateDataset(data,i)
        b = makeNewCenter(a)

        arrPointCluster[i]=b

    return arrPointCluster



def isClustersSame(data1,data2):
    for i in range(len(data1)):
        if(data1[3]!=data2[3]):
            return False
    return True
    

def train():

    # [ x, y, z, cluster ]
    data =[
        [5,5,2,0], #1
        [8,7,3,0], #2
        [4,8,2,0], #3
        [2,4,3,0], #4
        [2,2,1,0], #5
        [6,7,8,0], #6
    ]

    point1=data[1]
    point2=data[4]

    arrPointCluster=[point1,point2]

    dataBefore=data

    for i in range(10):
        # Find Cluster
        data = updateCluster(arrPointCluster,data)

        # Update center of cluster
        arrPointCluster = updateCenterOfCluster(data,arrPointCluster)

        # if cluster doesnt change then stop iteration
        if(isClustersSame(data,dataBefore)):
            print("Same")
            print("Dataset")
            print(data)
            print("Center of Cluster")
            print(arrPointCluster)
            break
        else:
            dataBefore=data


train()