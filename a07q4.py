import check
####################################
## Frances Ferrabee 20712523
## CS 116 Winter 2018
## Assignment 07 Problem 04
####################################

# Question 4 part A

## merge3(L1, L2,L): returns 1 sorted list
## merge3: (listof Int) (listof Int) (listof Int)-> (listof Int)
## Requires: L1, L2, to be sorted lists. len(L) = len(L1)+ len(L2)
def merge(L1, L2, L):
    pos1= 0
    pos2=0
    posL=0
    while (pos1< len(L1)) and (pos2< len (L2)):
        if L1[pos1]< L2[pos2]:
            L[posL]= L1[pos1]
            pos1+= 1
        else:
            L[posL]= L2[pos2]
            pos2 += 1
        posL += 1
    while(pos1< len(L1)):
        L[posL]= L1[pos1]
        pos1= pos1+1
        posL= posL+1
    while (pos2< len(L2)):
        L[posL]= L2[pos2]
        pos2= pos2+1
        posL = posL+1
    return L

## merge3(L1, L2,L3): returns 1 sorted list
## merge3: (listof Int) (listof Int) (listof Int)-> (listof Int)
## Requires: L1, L2, L3 to be sorted lists
# Examples:
## merge3([1,2,3],[3,4,6], [3,4,6])=> [1,2,3,3,3,4,4,6,6]
## merge3([], [1,2,6], [2,6,9])=> [1,2,2,6,6,9]
def merge3(L1, L2, L3):
    if L2 ==[] and L1==[]:
        return L3
    elif L2==[] and L3==[]:
        return L1
    elif L3==[] and L1==[]:
        return L2
    elif L3==[]:
        return merge(L1, L2, L1+L2)
    elif L2==[]:
        return merge(L3, L1, L1+L3)
    elif L1==[]:
        return merge(L2, L3, L2+L3)
    else:
        return merge( merge(L2, L3, L2+L3), L1, merge(L2, L3, L2+L3) + L1)


## Tests:
check.expect("Test1", merge3([], [], []), [])
check.expect("Test2", merge3([1,2,4,5], [], []), [1,2,4,5])
check.expect("Test3", merge3([2,4,6], [3,5,7,9], []), [2,3,4,5,6,7,9])
check.expect("Test4", merge3([1,5,6,7], [2,3,4,5], [1,2]),[1,1,2,2,3,4,5,5,6,7])
check.expect("Test5", merge3([],[7], []), [7])
check.expect("Test6", merge3([1,5], [4,7,8], [3,5]), [1,3,4,5,5,7,8])


# Question 4B
## mergesort(L): returns a sorted list
## mergesort: (listof Int)-> (listof Int)
## Examples:
# mergesort3([1,5,2,7,1]) -> [1,1,2,5,7]
# mergesort3([9,1,6,2]) -> [1,2,6,9]

def mergesort3(L):
    if len(L) < 2: 
        return L
    elif len(L)==2:
        m1= mergesort3([L[0]]) 
        m2= mergesort3([L[1]])
        return merge3(m1, m2, [])
    else:
        third = len(L)//3
        L1= L[:third]
        L2= L[third:third*2]
        L3= L[third*2:]
        m1= mergesort3(L1)
        m2= mergesort3(L2)
        m3= mergesort3(L3)
        return merge3(m1,m2,m3)
    
check.expect("Test1", mergesort3([]), [])
check.expect("Test2", mergesort3([1,3,2]), [1,2,3])
check.expect("Test3", mergesort3([1,2,3,4]), [1,2,3,4])
check.expect("Test4", mergesort3([7,6,5,3]), [3,5,6,7])
check.expect("Test5", mergesort3([1,8,2,6,3]), [1,2,3,6,8])
check.expect("Test6", mergesort3([2]), [2])