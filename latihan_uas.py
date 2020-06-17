import csv
import matplotlib.pyplot as plt
from math import sqrt
import random


from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np

print("K-Means Clustering Algorithm")
# http://studyshut.blogspot.com/2018/12/contoh-perhitungan-manual-menggunakan.html


def getData():
    with open('datasets/mhs.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        return list(csv_reader)


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
    for nama,xpoint,ypoint,zpoint in data:
        arr=[]
        for C in Cluster:
            jarak = euclidean_distance(C,[int(xpoint),int(ypoint),int(zpoint)])
            arr.append(jarak)

        idx=cariMinimum(arr)
        new_data.append([nama,float(xpoint),float(ypoint),float(zpoint),idx+1])
    return new_data

def hitungJarak(data,Cluster):
    new_data=list()
    for nama,xpoint,ypoint,zpoint,label in data:
        arr=[]
        for C in Cluster:
            jarak = euclidean_distance(C,[int(xpoint),int(ypoint),int(zpoint)])
            arr.append(jarak)

        idx=cariMinimum(arr)
        new_data.append([nama,float(xpoint),float(ypoint),float(zpoint),idx+1])
    return new_data


# print(new_data)

# hitung Tengah cluster lagi

def updateTitikTengahCluster(new_data,Cluster):
    for i in range(0,len(Cluster)):
        xpoint=0.0
        ypoint=0.0
        zpoint=0.0
        banyak=0
        for m in new_data:
            if(m[4]==i+1):
                xpoint   +=m[1]
                ypoint +=m[2]
                zpoint   +=m[3]
                banyak+=1
        if(banyak==0):
            Cluster[i]=[xpoint,ypoint,zpoint]
        else:
            Cluster[i]=[xpoint/banyak,ypoint/banyak,zpoint/banyak]
    return Cluster

def cariNilaiMinimum(new_data):
    minim=100
    for i in new_data:
        for j in range(1,len(i)-1):
            itu=int(i[j])
            if(itu < minim):
                minim=itu

    return minim


def cariNilaiMaximal(new_data):
    max=0
    for i in new_data:
        for j in range(1,len(i)-1):
            itu=int(i[j])
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
        maxP=int(maxP)
        maxPbefore=int(maxPbefore)
        Cluster.append([
            random.randint(mini,maxi),
            random.randint(mini,maxi),
            random.randint(mini,maxi)
        ])
        maxPbefore+=each
        maxP+=each
    return Cluster



def countVariation(new_data,k):
    arr=[]
    for i in range(1,k+1):
        count=0
        for j in new_data:
            if(j[4]==i):
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
ax = fig.add_subplot(111, projection='3d')

def outputkan(new_data,Cluster,clear=False):
    
    for nama,xpoint,ypoint,zpoint,label in new_data:
        if(label==1):
            ax.scatter(int(xpoint),int(ypoint),int(zpoint), c="red")
        elif(label==2):
            ax.scatter(int(xpoint),int(ypoint),int(zpoint), c="green")
        else:
            ax.scatter(int(xpoint),int(ypoint),int(zpoint), c="blue")

        ax.text(float(xpoint),float(ypoint),float(zpoint),nama, size=20, zorder=1,color='k') 
        

    color=["red","green","blue"]
    for i in range(0,len(Cluster)):
        ax.scatter(Cluster[i][0],Cluster[i][1],Cluster[i][2], c=color[i],marker="+")

    ax.set_xlabel('xpoint')
    ax.set_ylabel('ypoint')
    ax.set_zlabel('zpoint')
    plt.pause(0.001)

    if(not clear):
        fig.canvas.draw()
        fig.canvas.flush_events()
        ax.clear()



data = [
    ["p1",5,5,2],
    ["p2",8,7,3],
    ["p3",4,8,2],
    ["p4",2,4,3],
    ["p5",2,2,1],
    ["p6",6,7,8],
]


K=2

new_data=data
Cluster=newCluster(K,new_data)
# print(Cluster)

new_data=hitungJarakFirst(new_data,Cluster)

Cluster=updateTitikTengahCluster(new_data,Cluster)


dataCluster=[]

for j in range(0,50):
   
    for i in range(0,10):
        if(i!=0):
            varBefore=var

        new_data=hitungJarak(new_data,Cluster)
        Cluster=updateTitikTengahCluster(new_data,Cluster)
        var = countVariation(new_data,K)
    
        outputkan(new_data,Cluster)
        

        if(i!=0):
            if(itsSame(var,varBefore)):
                print("SAME")
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




# for i in dataCluster:
#     print(i)

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