# Python program for implementation of Quicksort Sort 

# This function takes last element as pivot, places 
# the pivot element at its correct position in sorted 
# array, and places all smaller (smaller than pivot) 
# to left of pivot and all greater elements to right 
# of pivot


def partition(arr,low,high): 
        global bo
        bo=bo+1
        i = ( low-1 )
        bo=bo+1
        # index of smaller element 
        pivot = arr[high]        # pivot 
        
        for j in range(low , high): 
                bo=bo+1
                # If current element is smaller than or 
                # equal to pivot 
                if arr[j] <= pivot: 
                        bo=bo+2
                        # increment index of smaller element 
                        i = i+1
                        arr[i],arr[j] = arr[j],arr[i] 
        bo=bo+1
        arr[i+1],arr[high] = arr[high],arr[i+1]
        bo=bo+1
        return ( i+1 ) 

# The main function that implements QuickSort 
# arr[] --> Array to be sorted, 
# low --> Starting index, 
# high --> Ending index 

# Function to do Quick sort 
def quickSort(arr,low,high): 
        global bo
        bo=bo+1
        if low < high: 

                # pi is partitioning index, arr[p] is now 
                # at right place 
                pi = partition(arr,low,high) 

                # Separately sort elements before 
                # partition and after partition 
                quickSort(arr, low, pi-1) 
                quickSort(arr, pi+1, high) 

# Driver code to test above
import random
lst=[]
for i in range(200):
        lst.append(i)
n = len(lst)
bo=0
quickSort(lst,0,n-1)
line=str(n)+","+str(bo)+","+str(n*(n+1)/2)
print(line)
q=open(r"C:\Users\user\Desktop\practical running time\datafilestoplot\QuickSortLastPivot.txt","w+")
#destination file
q.write(line)
q.write("")


  

 
