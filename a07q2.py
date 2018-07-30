
import check
    ####################################
    ## Frances Ferrabee 20712523
    ## CS 116 Winter 2018
    ## Assignment 07 Problem 02
    ####################################
## count_longest_asc(L): returns the length of the longest run of ascending 
##      numbers in L
## count_longest_asc: (listof Int) -> Nat
## Requires: len(L)>0
## Examples:
# count_longest_acs([1,2,3,4])-> 4
# count_longest_asc([9,1,7,8])-> 3
def count_longest_asc(L):
    counter=0
    ind=0
    greatest_counter= 1
    
    while ind< len(L)-1:

        if L[ind+1]> L[ind] :
            counter = counter +1
            
        elif L[ind+1]< L[ind]:
            counter=0 
        else:
            pass
        if counter+1> greatest_counter:
            greatest_counter= counter+1 
            ind= ind+1
        else:
            ind= ind+1  
    return greatest_counter

check.expect("Test1", count_longest_asc([1,6,2,4,7]), 3)
check.expect("Test2", count_longest_asc([6,6,6,6]),1)
check.expect("Test3", count_longest_asc([9,6,3,1,0, 0]),1)
check.expect("Test4", count_longest_asc([1,3,5,7,99]), 5)
check.expect("Test5", count_longest_asc([34,64,1,67,21,7,2]),2)
check.expect("Test6", count_longest_asc([1,2,34,6,36,13,5]),3)
check.expect("Test7", count_longest_asc([3]), 1)