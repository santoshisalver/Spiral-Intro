# -*- coding: utf-8 -*-
"""
Created on Mon Nov 18 00:41:38 2024

@author: santo
"""

def spiral(m,n,a):
#m=number of rows,n=number of columns
#a=list through which we represent matrix
    k=0#starting index of row
    l=0#starting index of column
    while(k<m and l<n):
        #printing first row from remaining rows
        for i in range(l,n):
            print(a[k][i],end=' ')
        k+=1
        #printing last column from remaining columns
        for i in range(k,m):
            print(a[i][n-1],end=' ')
        n-=1
        '''we check again because k might had incremented after the 
        k+=1, if k>m it would try to traverse non-existing rows 
        give index error'''
        if(k<m):
            #printing last row from remaining rows
            for i in range(n-1,l-1,-1):
                print(a[m-1][i],end=' ')
            m-=1
        if(l<n):
            #printing the first column from,the remaining columns
            for i in range(m-1,k-1,-1):
                print(a[i][l],end=' ')
            l+=1
a=[]
count=1
for i in range(4):
    l=[]
    for j in range(4):
        l.append(count)
        count+=1
    a.append(l)
spiral(4,4,a)