import check

import math
####################################
## Frances Ferrabee 20712523
## CS 116 Winter 2018
## Assignment 05 Problem 01
####################################


# Question 1 - Part a

# remember_product( product, A, B): returns the value of taking the dot product of A and B
#     , that is multiplying the element of A and B together at the same index
#     and then adding these numbers all together. 
# remember_product: Float (listof Float) (listof Float) -> Float
# requires: len(A)== len(B)
def remember_product ( product, A, B):
   if len(A)==0:
      return product
   else:
      return remember_product( product+A[0]* B[0], A[1:], B[1:])


# dot_product( A, B): Returns the value of taking the dot product of A and B
#     , that is multiplying the element of A and B together at the same index
#     and then adding these numbers all together. 
# dot_product: (listof Float) (listof Float) -> Float
# requires: len(A) == len(B)
# Examples:
# dot_product([-1.0, 2.0], [2.0, 1.0]) => 0.0
# dot_product([1.0, 2.0, 3.0], [1.0, 1.0, 1.0]) => 6.0

def dot_product(A, B):
   return remember_product(0.0, A, B)

check.expect("Test1", dot_product([1,2,3,4], [1,2,3,4]), 2)
check.expect("Test2", dot_product([-2,-3,-4], [2,3,4]), 2)
check.expect("Test3", dot_product([], []), 2)
check.expect("Test4", dot_product([-1,7,3,5,6], [8, 0,2,-3,6]), 2)
    
                    
# Question 1 - Part b

# remember_positive( positive_list, L): Returns a list with only the positive
#    numbers
# remember_positive: (listof Int) (listof Int) -> (listof Int)
def remember_positive (positive_list, L):
   if len(L)==0:
      return positive_list
   else:
      if L[0]>0:
         return remember_positive(positive_list+ [L[0]], L[1:])
      else:
         return remember_positive( positive_list, L[1:])
      
# keep_positive(L): Returns a list with only the positive numbers of the
#    original list.
# keep_positive: (listof Int) -> (listof Int)
# Examples:
# keep_positive([1, 2]) => [1, 2]
# keep_positive([3, -1, 2, 0, 1]) => [3, 2, 1]

def keep_positive(L):
   return remember_positive( [], L)      

check.expect("Test1", keep_positive([1,2,3,1]), [1,2,3,1])
check.expect("Test2", keep_positive([-2, -3,4]), [4])
check.expect("Test3", keep_positive([-2, -4, -2]), [])
check.expect("Test4", keep_positive([]), [])
