#importing library
import sys

#Declaring the satic list
#Can be changed to dynamic in further modification easily
A = [64, 25, 12, 22, 11]

#Tansversing through the list
for i in range(len(A)):
#Here we need to find the smallest element in the defined range
    minimum_index = i
    for j in range(i+1, len(A)):
 #checking the test condition
        if A[minimum_index] >A[j]:
            minimum_index = j
            
 #Swapping the elements
    A[i], A[minimum_index] = A[minimum_index], A[i]
  
  #printing the results
print("Initial array is: ")
print(A)
print("The sorted array is: ")
print(A)
