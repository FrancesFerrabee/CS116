import check
####################################
## Frances Ferrabee 20712523
## CS 116 Winter 2018
## Assignment 06 Problem 01
####################################

# Question 1 part a
# nat2bin(n): returns a list of the binary digits of n
# nat2bin: Nat-> (listof (anyof 0 1))
# Examples:
## nat2bin(12)-> [1,1,0,0]
## nat2bin(0) -> [0]
## nat2bin(3) -> [1,1]

def nat2bin (n):
    q= [n%2]
    while n//2!=0 :
        n= n//2
        q. extend([n%2])

    q.reverse() 
    return q
check.expect("Test1", nat2bin(0), [])
check.expect("Test2", nat2bin(2), [])
check.expect("Test3", nat2bin(3), [])
check.expect("Test4", nat2bin(5), [])
check.expect("Test5", nat2bin(8), [])
check.expect("Test6", nat2bin(17), [])
#b
def nat2base(n, base):
    q= [n%base]
    while n//base!=0 :
        n= n//base
        q. extend([n%base])

    q.reverse() 
    return q    