
import check
####################################
## Frances Ferrabee 20712523
## CS 116 Winter 2018
## Assignment 07 Problem 03
####################################
# binary_search(L, target, index): returns the updated index position of target 
#   in L given index ( old index).  
# binary_search: (listof Int) Int Nat -> Bool
def binary_search(L, target, index):
    beginning= 0
    end= len(L)-1
    while beginning <= end:
        middle= beginning+ (end-beginning)
        if L[middle]== target:
            x=0
            while x< len(L):
                if L[x]== target:
                    return x + index
                else:
                    x=x+1
        elif L[middle]> target:
            end= middle-1
        else:
            beginning = middle+1
    return False
    
## galloping_search(n,L): returns the index value of n in L
## galloping_search: Int (listof Nat) -> Nat
## Effects: prints "Galloping search from index x" where x is the value of the 
##    index each time the index value changes. Or "Binary search from index 
##    w to index y" where y and w is the range in which the possible index is
## Requires: L to be non-empty and sorted
##Examples
# galloping_search(14,[1,2,5,7,9,14,15,23,29]) -> 5
# and prints  "Galloping search from index 0
#              Galloping search from index 1
#              Galloping search from index 3
#              Galloping search from index 7
#              Binary search from index 4 to 6"
# galloping_search(100, [1,2,3,4,5,6,7,8,9,100]) -> 9
# and prints  "Galloping search from index 0 
#              Galloping search from index 1
#              Galloping search from index 3
#              Galloping search from index 7
#              Galloping search from index 9"
# galloping_search(3, [1,2,5,7,9]) -> False
# and prints  "Galloping search from index 0 
#              Galloping search from index 1
#              Galloping search from index 3
#              Binary search from index 2 to 2"
def galloping_search(n,L):
    index=1
    while index< len(L)+1 :
    
        print("Galloping search from index " + str(index-1))
        if L[index-1]==n:
            return index-1
        elif L[index-1]<n:
            if index!= len(L) and index* 2> len(L):
                index= len(L)
            else:
                index=2* index
            
        else:
            print("Binary search from index "+ str(index//2) + " to " + str(index-2))
            return binary_search( L[index//2: index-2], n, index//2)

    return False
# Test
check.set_screen("Galloping search from index 0\nGalloping search from index 1\nBinary search from index 1 to 0" )
check.expect("Test1", galloping_search(3, [1,4,7,9,12]), False)

check.set_screen("Galloping search from index 0")
check.expect("Test2", galloping_search(4, [4,5,6,82,88]), 0)

check.set_screen("Galloping search from index 0\nGalloping search from index 1")
check.expect("Test3", galloping_search(13, [12, 13,44,67,98,123,456]), 1)

check.set_screen("Galloping search from index 0\nGalloping search from index 1\nGalloping search from index 3\nGalloping search from index 5")
check.expect("Test4", galloping_search(45,[1,2,5,23,24,45]), 5)

check.set_screen("Galloping search from index 0\nGalloping search from index 1\nBinary search from index 1 to 0")
check.expect("Test5", galloping_search(3, [1,4,6,7,8]), False)

check.set_screen("Galloping search from index 0")
check.expect("Test6", galloping_search(5, [0]), False)

check.set_screen("Galloping search from index 0")
check.expect("Test7", galloping_search(5, [5]), 0)

