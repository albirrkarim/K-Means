import csv
import matplotlib.pyplot as plt
from math import sqrt
import random


from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np

print("K-Means Clustering Algorithm")


def getData():
    # Buka File CSV lalu return kan menjadi array
    with open('datasets/iris.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        return list(csv_reader)


def euclidean_distance(row1, row2):
    # Euclidean distance, Menghitung jarak dua titik
    distance = 0.0
    for i in range(0,len(row1)):
        distance += (row1[i] - row2[i])**2
    return sqrt(distance)

def cariMinimum(arr):
    min=arr[0]
    idx=0
    for i in range(0,len(arr)):
        if(arr[i]<min):
            min=arr[i]
            idx=i

    return idx

def hitungJarak(data,Cluster):
    new_data=list()
    for row in data: # Loop semua titik 

        arr=[]
        for C in Cluster: # Titik tersebut terhadap ketiga cluster jaraknya berapa
            jarak = euclidean_distance(C,[float(row[0]),float(row[1])])
            arr.append(jarak)

        # Titik tersebut dekat ke cluster yang mana ?
        # maka cari yang jaraknya paling minimum
        idx=cariMinimum(arr) 
        # lalu labeli titik tersebut dengan label 1,2,3 dst 
        # ini idx+1 karena array itu dari 0 
        new_data.append([float(row[0]),float(row[1]),idx+1])
    
    # return array semua titik, yang telah ter update labelnya
    return new_data




# hitung Tengah cluster lagi

def updateTitikTengahCluster(new_data,Cluster):
    for i in range(0,len(Cluster)): # update titik tengah Cluster
        arrData=[0,0]
        banyak=0
        for m in new_data:
            
            if(m[2]==i+1):
                for j in range(0,len(arrData)):
                    arrData[j]+=m[j]

                banyak+=1


        if(banyak==0):
            Cluster[i]=arrData
        else:
            for j in range(0,len(arrData)):
                arrData[j] = arrData[j]/banyak

            Cluster[i]=arrData
    
    
    # Cluster baru
    return Cluster

def cariNilaiMinimum(new_data):
    minim=100
    for i in new_data:
        for j in range(0,len(i)-1):
            itu=float(i[j])
            if(itu < minim):
                minim=itu

    return minim


def cariNilaiMaximal(new_data):
    max=0
    for i in new_data:
        for j in range(0,len(i)-1):
            itu=float(i[j])
            if(itu > max):
                max=itu

    return max


def newCluster(k,new_data):
    mini=cariNilaiMinimum(new_data)
    maxi=cariNilaiMaximal(new_data)
    Cluster=[]
    for i in range(0,k):
        Cluster.append([
            random.uniform(mini,maxi),
            random.uniform(mini,maxi)
        ])
    
    return Cluster



def countVariation(new_data,k):
    arr=[]
    for i in range(1,k+1):
        count=0
        for j in new_data:
            if(j[2]==i):
                count+=1

        arr.append(count)

    return arr







def itsGreat(points):
    sum=0
    banyak=0
    for i in points:
        sum+=i
        banyak+=1
    
    rata = sum/banyak

    sumSelisih=0
    for m in points:
        sumSelisih+=abs(rata-m)

    return sumSelisih


def itsSame(points1,points2):
    for i in range(len(points1)):
        if(points1[i]!=points2[i]):
            return False

    return True



fig = plt.figure()
ax = fig.add_subplot(1,1,1)

def outputkan(new_data,Cluster,clear=False):
    color=["red","green","blue","black","yellow","pink"]
    for row in new_data:
        ax.scatter(row[0],row[1],color=color[row[2]-1])
      
    for i in range(0,len(Cluster)):
        ax.scatter(Cluster[i][0],Cluster[i][1], c=color[i],marker="+")

    plt.pause(0.01)
    if(not clear):
        ax.clear()



data = getData()
K=3
# print(data)


new_data=data
Cluster=newCluster(K,new_data)
# # print(Cluster)

# new_data=hitungJarak(new_data,Cluster)
# # print(new_data)
# # outputkan(new_data,Cluster)

# Cluster=updateTitikTengahCluster(new_data,Cluster)
# # print(Cluster)


# # print(new_data)
# outputkan(new_data,Cluster)

dataCluster=[]

for j in range(0,30):
    # print(j)
    for i in range(0,30):
        # print(i)
        if(i!=0):
            varBefore=var

        new_data=hitungJarak(new_data,Cluster)
        Cluster=updateTitikTengahCluster(new_data,Cluster)
        var = countVariation(new_data,K)
    
        # outputkan(new_data,Cluster)
        
        if(i!=0):
            if(itsSame(var,varBefore)):
                # print("SAME")
                
                aa=itsGreat(var)
                
                dataCluster.append([Cluster,aa])

                break

    
    Cluster=newCluster(K,new_data)

# print(dataCluster)


def minimumSelisih(dataCluster):
    
    minim=dataCluster[0][1]
    idxMin=0
    for i in range(0,len(dataCluster)):
        if(dataCluster[i][1]<minim):
            minim=dataCluster[i][1]
            idxMin=i

    return idxMin



Cluster=dataCluster[minimumSelisih(dataCluster)][0]

for i in range(0,10):
    if(i!=0):
        varBefore=var

    new_data=hitungJarak(new_data,Cluster)
    Cluster=updateTitikTengahCluster(new_data,Cluster)
    var = countVariation(new_data,K)

    if(i!=0):
        if(itsSame(var,varBefore)):
            outputkan(new_data,Cluster,True)
            print(Cluster)
            break




plt.show()  

    





