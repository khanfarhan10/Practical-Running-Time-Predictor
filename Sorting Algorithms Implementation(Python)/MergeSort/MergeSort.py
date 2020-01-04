# Python program for implementation of MergeSort 
  
# Merges two subarrays of arr[]. 
# First subarray is arr[l..m] 
# Second subarray is arr[m+1..r] 
def merge(arr, l, m, r):
    global bo
    n1 = m - l + 1
    n2 = r- m
    bo=bo+n1+n2+2
    L=[]
    R=[]
    # create temp arrays
    for i in range(0,n1):
        L.append(0)
    for i in range(0,n2):
        R.append(0)
     
  
    # Copy data to temp arrays L[] and R[] 
    for i in range(0 , n1): 
        L[i] = arr[l + i] 
  
    for j in range(0 , n2): 
        R[j] = arr[m + 1 + j] 
  
    # Merge the temp arrays back into arr[l..r] 
    i = 0     # Initial index of first subarray 
    j = 0     # Initial index of second subarray 
    k = l     # Initial index of merged subarray 
  
    while i < n1 and j < n2 :
        bo=bo+3
        if L[i] <= R[j]: 
            arr[k] = L[i]
            bo=bo+1
            i += 1
        else: 
            arr[k] = R[j] 
            j += 1
        k += 1
  
    # Copy the remaining elements of L[], if there 
    # are any 
    while i < n1:
        bo=bo+1
        arr[k] = L[i] 
        i += 1
        k += 1
  
    # Copy the remaining elements of R[], if there 
    # are any 
    while j < n2:
        bo=bo+1
        arr[k] = R[j] 
        j += 1
        k += 1
  
# l is for left index and r is right index of the 
# sub-array of arr to be sorted 
def mergeSort(arr,l,r):
    global bo
    bo=bo+1
    if l < r: 
  
        # Same as (l+r)/2, but avoids overflow for 
        # large l and h 
        m = (l+(r-1))/2
        bo=bo+1
  
        # Sort first and second halves 
        mergeSort(arr, int(l), int(m)) 
        mergeSort(arr, int(m+1), int(r)) 
        merge(arr, int(l), int(m), int(r)) 
  
  
# Driver code to test above
#erase all previous content on the file
open(r"C:\Users\user\Desktop\practical running time\MergeSort.txt", 'w').close()
import random
i=10
limit=100000
while(i<=limit):
  lst = []
  for x in range(i):
    lst.append(random.randint(1,20*i))
  n=i
  bo=0
  mergeSort(lst,0,i-1)
  #line=str(n)+","+str(bo)+","+str(n*(n-1)/2)
  line=str(bo)+","+str(n)
  print(line)
  q=open(r"C:\Users\user\Desktop\practical running time\MergeSort.txt","a+")
  #destination file
  q.write(line)
  q.write("\n")
  i=i+100
