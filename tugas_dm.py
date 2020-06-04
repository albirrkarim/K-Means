import csv
import matplotlib.pyplot as plt
from math import sqrt
import random


from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np

print("K-Means Clustering Algorithm")
# http://studyshut.blogspot.com/2018/12/contoh-perhitungan-manual-menggunakan.html



def euclidean_distance(row1, row2):
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

def hitungJarakFirst(data,Cluster):
    new_data=list()
    for nama,x,y in data:
        arr=[]
        for C in Cluster:
            jarak = euclidean_distance(C,[float(x),float(y)])
            arr.append(jarak)

        idx=cariMinimum(arr)
        new_data.append([nama,float(x),float(y),idx+1])

    return new_data

def hitungJarak(data,Cluster):
    new_data=list()
    for nama,x,y,label in data:
        arr=[]
        for C in Cluster:
            jarak = euclidean_distance(C,[float(x),float(y)])
            arr.append(jarak)

        idx=cariMinimum(arr)
        new_data.append([nama,float(x),float(y),idx+1])
    return new_data


# print(new_data)

# hitung Tengah cluster lagi

def updateTitikTengahCluster(new_data,Cluster):
    for i in range(0,len(Cluster)):
        x=0.0
        y=0.0
      
        banyak=0
        for m in new_data:
            if(m[3]==i+1):
                x   +=m[1]
                y   +=m[2]
         
                banyak+=1

        if(banyak==0):
            Cluster[i]=[x,y]
        else:
            Cluster[i]=[x/banyak,y/banyak]

    return Cluster

def cariNilaiMinimum(new_data):
    minim=100
    for i in new_data:
        for j in range(1,len(i)-1):
            itu=float(i[j])
            if(itu < minim):
                minim=itu

    return minim


def cariNilaiMaximal(new_data):
    max=0
    for i in new_data:
        for j in range(1,len(i)-1):
            itu=float(i[j])
            if(itu > max):
                max=itu

    return max


def newCluster(k,new_data):
    mini=cariNilaiMinimum(new_data)
    maxi=cariNilaiMaximal(new_data)

    each=(maxi-mini)/k
    
    maxP=each+mini
    maxPbefore=mini

    Cluster=[]
    for i in range(0,k):
        maxP=float(maxP)
        maxPbefore=float(maxPbefore)
        Cluster.append([
            random.uniform(mini,maxi),
            random.uniform(mini,maxi),
        ])
        maxPbefore+=each
        maxP+=each
    return Cluster



def countVariation(new_data,k):
    arr=[]
    for i in range(1,k+1):
        count=0
        for j in new_data:
            if(j[3]==i):
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
ax = fig.add_subplot(111)

def outputkan(new_data,Cluster,clear=False):
    
    for nama,x,y,label in new_data:
        if(label==1):
            ax.scatter(float(x),float(y), c="red")
        elif(label==2):
            ax.scatter(float(x),float(y), c="green")

        ax.text(float(x),float(y),nama, size=20, zorder=1,color='k') 
        

    color=["red","green"]

    for i in range(0,len(Cluster)):
        ax.scatter(Cluster[i][0],Cluster[i][1], c=color[i],marker="+")

    ax.set_xlabel('x')
    ax.set_ylabel('y')

    plt.pause(0.001)

    if(not clear):
        fig.canvas.draw()
        fig.canvas.flush_events()
        ax.clear()



# data = getData()

data=[
    ["p1",0.40,0.53],
    ["p2",0.22,0.38],
    ["p3",0.35,0.32],
    ["p4",0.26,0.19],
    ["p5",0.08,0.41],
    ["p6",0.45,0.30],
]


new_data=data
Cluster=newCluster(1,new_data)

new_data=hitungJarakFirst(new_data,Cluster)
Cluster=updateTitikTengahCluster(new_data,Cluster)

dataCluster=[]

for j in range(0,50):
   
    for i in range(0,20):
        if(i!=0):
            varBefore=var

        new_data= hitungJarak(new_data,Cluster)
        Cluster = updateTitikTengahCluster(new_data,Cluster)
        var     = countVariation(new_data,2)
    
        outputkan(new_data,Cluster)
        

        if(i!=0):
            if(itsSame(var,varBefore)):
                print("SAME")
                aa=itsGreat(var)
                dataCluster.append([Cluster,aa])

                break

    
    Cluster=newCluster(2,new_data)


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

    new_data    = hitungJarak(new_data,Cluster)
    Cluster     = updateTitikTengahCluster(new_data,Cluster)
    var         = countVariation(new_data,2)

    if(i!=0):
        if(itsSame(var,varBefore)):
            outputkan(new_data,Cluster,True)
            print(Cluster)
            break




plt.show()