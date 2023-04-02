"""
-------------------------CS 3364 Algorithms: Project1 -------------------------

Find source reliability by counting inversions during sorting

@Author: Santona Subedi - R11737206, 


#A program in python that is utilized in checking the reliability of the search engines. The steps are:
# 1) Reads the data from the file.
# 2) Stores them in their respective arrays.
# 3) Adds the contents from the corresponding indexes in the array and stores in an array.
# 4) Sorts the combined array and sorts the sources 1, 2, 3, 4 and 5 with the indexes from the cobined array.
# 6) Individually sorts the sorted file and check inversions for comparisions implementing different algorithms.

"""


#importing required library for data and array management
import numpy as np

#creating individual arrays for each source file to keep the page rankings
source1 = np.loadtxt("source1.txt", dtype="int")
source2 = np.loadtxt("source2.txt", dtype="int")
source3 = np.loadtxt("source3.txt", dtype="int")
source4 = np.loadtxt("source4.txt", dtype="int")
source5 = np.loadtxt("source5.txt", dtype="int")


"""  Arrays and Variables declaration  """

#keeps the value of inversions in QuickSort
q_inv_count = 0

#saving the length of the source file array as variable arrayLen
arrayLen = len(source1)


##creating the combList array that will be used to hold the sum of page rankings(elements)
combList = np.empty([arrayLen], dtype="int")

"""A loop to add the contents of the corresponding indexes from each source file"""
for n in range(arrayLen):
    combList [n] = source1[n] + source2[n] + source3[n] + source4[n] + source5[n]


"""
Function: BubbleSort
input: Source arrays
output:Adjusted arrays
Usage: sort the combinedList Array and adjusts elements in the SourceArrays to match
"""

def BubbleSort(s1, s2, s3, s4, s5, s6):
    for i in range(arrayLen):
        for j in range(arrayLen - i - 1):
            if(s1[j] > s1[j + 1]):
                temp = s1[j]
                s1[j] = s1[j + 1]
                s1[j+1] = temp

                #swaps all the remaining contents in all arrays
                temp1 = s2[j]
                s2[j] = s2[j + 1]
                s2[j+1] = temp1

                temp2 = s3[j]
                s3[j] = s3[j + 1]
                s3[j+1] = temp2

                temp3 = s4[j]
                s4[j] = s4[j + 1]
                s4[j+1] = temp3

                temp4 = s5[j]
                s5[j] = s5[j + 1]
                s5[j+1] = temp4

                temp5 = s6[j]
                s6[j] = s6[j + 1]
                s6[j+1] = temp5

""""call BubbleSort on the combList array and the source arrays"""
BubbleSort(combList, source1, source2, source3, source4, source5)


"""saving a copy of the adjusted arrays"""
newS1 = list(source1)
newS2 = list(source2)
newS3 = list(source3)
newS4 = list(source4)
newS5 = list(source5)

newS11 = list(source1)
newS12 = list(source2)
newS13 = list(source3)
newS14 = list(source4)
newS15 = list(source5)



""""Function: MergeSort
    input: Source array and Array Length
    output:function call
    Usage: we use this function to make calling the _mergeSort function to count inversions easier.
           Since the _mergeSort function takes in more arguments, it is easier to call mergeSort with only 2 arguments."""

def mergeSort(array, arrayLen):

	# create a temporary array of arrayLenght(10000) size
	temp_array =  np.empty([arrayLen], dtype="int")

	return _mergeSort(array, temp_array, 0, arrayLen - 1)



"""Function: _mergeSort
    Input: array(array to be sorted), temp_Array, left(starting Index), right(last index)
    Output: inversion count
    Usage: sorts the combinedArray and counts inversions."""

def _mergeSort(array, temp_array, left, right):

	# variable inv_count is used to store inversion counts in each recursive call
	inv_count = 0

	# condition check to make the recursive call
     # only if we have more than one element.
	if left < right:

		#dividing the array into two subarrays
		mid = (left + right)//2


		inv_count += _mergeSort(array, temp_array, left, mid)         #counting/calculating inversions in the left subarray


		inv_count += _mergeSort(array, temp_array, mid + 1, right)    #counting/calculating inversions in the right subarray


		inv_count += merge(array, temp_array, left, mid, right)       #calling the merge function to join the left and right subarrays.
	return inv_count




"""
    Function: merge
    Input: array to be sorted, temp_array, left(starting index), mid, right.
    Output: inversion count.
    Usage: This function will merge two subarrays in a single sorted subarray. """

def merge(array, temp_array, left, mid, right):

	# Starting index of left subarray
	i = left

	# Starting index of right subarray
	j = mid + 1

	# Starting index of the subarray to be sorted
	k = left

	inv_count = 0


    # a while loop that runs while the leftIndex and rightIndex
    # do not exceed the length of the divided subarray

	while i <= mid and j <= right:


          # we do not count inversions if the left element is less than the right element
		if array[i] <= array[j]:
			temp_array[k] = array[i]
			k = k + 1
			i = i + 1
		else:

			# increment inversionCount if the check above is false
			temp_array[k] = array[j]
			inv_count += (mid-i + 1)
			k = k + 1
			j = j + 1

	# Copy the remaining elements of left
	# subarray into temporary array
	while i <= mid:
		temp_array[k] = array[i]
		k = k + 1
		i = i + 1

	# Copy the remaining elements of right
	# subarray into temporary array
	while j <= right:
		temp_array[k] = array[j]
		k = k + 1
		j = j + 1

	# Copy the sorted subarray into original array
	for x in range(left, right + 1):
		array[x] = temp_array[x]

    #print(arr)
	return inv_count






"""Function: Insertion Sort
    Input: an array to be sorted
    Output: the inversion count
    Usage: sorts the Source arrays and counts the number of inversions.

        """

def insertionSort(array):

    #get the length of the array
    arrayLen = len(array)

    #declare the variable to hold the inversion count
    inv = 0

    #a for loop to iterate over the array and compare each element to the previous element
    for n in range(arrayLen):
        currentValue = array[n]     #store the current value. start at index 0
        compare = n - 1             #get the previous element in the array by subtracting 1 from current Index



        #while loop that swaps array elements when the previous element is greater than the next element
        #while counting inversions at every iteration.
        while (compare >= 0 and array[compare] > currentValue):
            inv += 1

            array[compare + 1] = array[compare] #copy the current element to the previous elements position

            compare = compare - 1

        array[compare + 1] = currentValue #replace the element at the current value that we replaced

    return inv







"""
    Function: QuickSort
    Input: array
    Output: sorted array with Inversion Count
    Usage: sorts the source files while counting the number of inversions


    """

def quickSort(array):

    global q_inv_count

    # If the input array contains fewer than two elements,
    # then return it as the result of the function
    if len(array) < 2:
        return array

    #picking the first element of the array as the pivot
    pivot = array[0]

    #creating empty arrays for our 3 subarrays
    low, equal, high = [], [], []



    #sorts the array by iterating over the content of the array
    #and moving each element into one of the 3 arrays(low, equal, high)
    for item in array:

        if item < pivot:
            low.append(item)
            q_inv_count = q_inv_count + len(equal) + len(high)
        elif item == pivot:
            equal.append(item)
            q_inv_count = q_inv_count + len(high)
        elif item > pivot:
            high.append(item)

    # recursive call of quickSort to sort each of the 3 arrays
    # and then add them back together.
    return quickSort(low) + equal + quickSort(high)



print("***********************************************************************************")
print("***********************************************************************************")
print("*******************************INVERSIONS COUNT************************************")
print("***********************************************************************************")
print("***********************************************************************************")

print('\n')

print("Counting Inversions using Merge Sort:")

result1 = mergeSort(source1, arrayLen)
print("Number of inversions for source 1 is ", result1)
result2 = mergeSort(source2, arrayLen)
print("Number of inversions for source 2 is ", result2)
result3 = mergeSort(source3, arrayLen)
print("Number of inversions for source 3 is ", result3)
result4 = mergeSort(source4, arrayLen)
print("Number of inversions for source 4 is ", result4)
result5 = mergeSort(source5, arrayLen)
print("Number of inversions for source 5 is ", result5)

print('\n')


print("Counting Inversions using Insertion Sort:")
result6= insertionSort(newS1)
print("Number of inversions for source 1 is ", result6)
result7 = insertionSort(newS2)
print("Number of inversions for source 2 is ", result7)
result8 = insertionSort(newS3)
print("Number of inversions for source 3 is ", result8)
result9 = insertionSort(newS4)
print("Number of inversions for source 4 is ", result9)
result10 = insertionSort(newS5)
print("Number of inversions for source 5 is ", result10)

print('\n')

print("Counting Inversions using Quick Sort:")
result11 = quickSort(newS11)
print("Number of inversions for source 1 is ", q_inv_count)
q_inv_count = 0
result12 = quickSort(newS12)
print("Number of inversions for source 2 is ", q_inv_count)
q_inv_count = 0
result13 = quickSort(newS13)
print("Number of inversions for source 3 is ", q_inv_count)
q_inv_count = 0
result14 = quickSort(newS14)
print("Number of inversions for source 4 is ", q_inv_count)
q_inv_count = 0
result15 = quickSort(newS15)
print("Number of inversions for source 5 is ", q_inv_count)

print('\n')

print("***********************************************************************************")
print("***********************************************************************************")
print("*********************************************END***********************************")
print("***********************************************************************************")
print("***********************************************************************************")
