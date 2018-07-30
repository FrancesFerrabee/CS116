
import check
####################################
## Frances Ferrabee 20712523
## CS 116 Winter 2018
## Assignment 06 Problem 02
####################################

## find_bigger(ints): returns in order the numbers in ints that are bigger
##     than all the numbers that came before in ints.
## find_bigger: (listof int) -> (listof int)
## Examples:
# find_bigger([0,4,5,4]) -> [0,4,5]
# find_bigger([1,2,4,4]) -> [1,2,4]
# find_bigger ([-2,-4,-4,-1]) -> [-2,-1]


def find_bigger(ints):
  q= []
  if ints==[]:
    return q
  else:
    d= ints[0]-1
    for c in ints:
      if c> d:
        q.extend([c])
        d=c
      else:
        d=c  
    return q 
    
  check.expect("Test1", find_bigger([1,1,1,1]), [])
  check.expect("Test2", find_bigger([1,2,3,5]), [])  
  check.expect("Test3", find_bigger([]), [])
  check.expect("Test4", find_bigger([-1,-2,-4,-1]), [])
  check.expect("Test5", find_bigger([-5,-2,1,0]), [])
  check.expect("Test6", find_bigger([1,2,7,1]), [])
  check.expect("Test7", find_bigger([0,0,0,0]), [])
  check.expect("Test8", find_bigger([0,-1,1,2,4,1,-22,4,2]), [])
  check.expect("Test9", find_bigger([1]), [])
  
  