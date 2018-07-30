import check
####################################
## Frances Ferrabee 20712523
## CS 116 Winter 2018
## Assignment 06 Problem 03
####################################

#Question 3A
# is_palindrome(s): Returns True if s is a palindrome
# is_palindrome: Str-> Bool
# Examples:
## is_palindrome("racecar") -> True
## is_palindrome ("sata") -> False

def is_palindrome(s):
    q=0
    c=0
    while c < len(s):
        if s[c]== s[len(s)-1-c]:
            q= q+0
            c= c+1
        else:
            q= q+1
            c= c+1
    if q>0:
        return False
    else:
        return True

check.expect("Test1", is_palindrome(""), True)
check.expect("Test2", is_palindrome ("jdakdj"), False)
check.expect("Test3", is_palindrome("lpl"), True)
check.expect("Test4", is_palindrome("qmwemq"), False)
check.expect("Test5", is_palindrome("ommo"), True)
check.expect("Test6", is_palindrome("sateetaw"), False)
check.expect("Test7", is_palindrome("tacocat"), True)
check.expect("Test8", is_palindrome("asdda"), False)
check.expect("Test9", is_palindrome("s"), True)

    
#Question 3B
# longest_subpalindrome(s): returns the longest palindrome in s
# longest_subpalindrome: Str -> Str
##Examples:
## longest_subpalindrome("racecar") -> "racecar"
## longest_subpalindrome ("sata") -> "ata"
def longest_subpalindrome(s):
    while is_palindrome(s)==False:
        if is_palindrome(s[:-1]) == True:
            s= s[:-1]
            return s
        if is_palindrome(s[1:]) == True:
            s= s[1:]
            return s
        s= s[:-1]
    return s


check.expect("Test1", longest_subpalindrome(""), "")
check.expect("Test2", longest_subpalindrome ("jdakdj"), "j")
check.expect("Test3", longest_subpalindrome("lpl"), "lpl")
check.expect("Test4", longest_subpalindrome("qmwemq"), "q")
check.expect("Test5", longest_subpalindrome("ommo"), "ommo")
check.expect("Test6", longest_subpalindrome("sateetaw"), "ateeta")
check.expect("Test7", longest_subpalindrome("tacocat"), "tacocat")
check.expect("Test8", longest_subpalindrome("asdda"), "a")
check.expect("Test9", longest_subpalindrome("s"), "s")
check.expect("Test10", longest_subpalindrome("eatautu"), "ata")