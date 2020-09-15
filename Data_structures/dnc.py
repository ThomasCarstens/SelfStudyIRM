#The last element will be taken as a pivot by the use of the function
#The smaller element is placed left to the pivot
#The greater element is placed to the right of the pivot
def partition(array,low,high):
    i = ( low-1 )         # index of smaller element is chosen
    pivot = array[high]     # pivot is chosen

    for j in range(low , high):

        #Is the element less or equal to the pivot
        if   array[j] <= pivot:

            # increment index of smaller element
            i = i+1
            array[i],array[j] = array[j],array[i]

    array[i+1],array[high] = array[high],array[i+1]
    return ( i+1 )
# The main crux of the problem that implements Quick sort is
#array[] is to be sorted
#high is the ending index
#low is the starting index

# Function to do Quick sort
def quickSort(array,low,high):
    if low < high:

       #pit is the partitioning index
        pit = partition(array,low,high)

      #Element sorted before and after partition
        quickSort(array, low, pit-1)
        quickSort(array, pit+1, high)

array=[2,4,6,8,10,12]
n = len(array)
quickSort(array,0,n-1)
print ("The Sorted array is:")
for i in range(n):
    print ("%d" %array[i]),
