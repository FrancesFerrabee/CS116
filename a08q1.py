import check
####################################
## Frances Ferrabee 20712523
## CS 116 Winter 2018
## Assignment 08 Problem 01
####################################

# Question 1 A

## common_letter(s): returns the maximum number of times a 
##     letter appears in s
## common_letter: Str-> Str
def common_letter(s):
    count= 0
    maximum= 0
    while count< len(s):
        if s[count].isalpha():
            if s.count(str.lower(s[count]))+ s.count(str.upper(s[count])) > maximum:
                maximum= s.count(str.lower(s[count])) + s.count(str.upper(s[count]))
            
        count=count+1
    return maximum

## shift_encode(s): shifts each letter in s up by the maximum number 
##    of times a letter appears in s
## shift_encode: Str -> Str
## Examples:
# shift_encode("Hey! Where you at?") -> "KHB! Zkhuh brx dw?"
# shift_encode("Q"* (26*2 +3) + "w") -> "T"* (26*2+3) + "z"
def shift_encode(s):
    alpha= {"a": 1, "b": 2, "c": 3, "d":4, "e":5, "f":6, "g":7, "h":8, "i":9, "j":10, "k": 11, "l": 12, "m":13, "n":14, "o": 15, "p":16, "q": 17, "r": 18, "s":19, "t": 20, "u":21, "v": 22,"w": 23, "x":24, "y":25, "z":0}
    string = ""
    
    for letter in s:
        if letter.isalpha():
            if letter. islower():
                for ind in list(alpha.keys()):
                        if alpha[ind]== ((alpha [letter] + common_letter(s)) % 26):
                            string = string+ ind                        
                    
            else:
                for ind in list(alpha.keys()):
                        if alpha[ind]== ((alpha[letter. lower()]+common_letter(s)) % 26):
                            string = string+ ind. upper()                        
        else:
            string = string+ letter
    
    return string

check.expect("Test 1", shift_encode("efw 23 pl 2"), "fgx 23 qm 2")
check.expect("Test 2", shift_encode("HellO FrieNd"), "JgnnQ HtkgPf")
check.expect("Test 3", shift_encode("/? hey Yo"), "/? jga Aq")
check.expect("Test 4",shift_encode("HhHhHhUuUuHhHh"), "RrRrRrEeEeRrRr")
check.expect("Test 5", shift_encode(""), "")
check.expect("Test 6", shift_encode("3468"), "3468")
check.expect("Test 7", shift_encode("H"*(45+1)+ "n"), "B"*(45+1)+ "h")
check.expect("Test 8", shift_encode("HIIII"), "LMMMM")





# Question 1 B
## shift_decode(s): shifts each letter in s down by the maximum
##     number of times a letter appears in s
## shift_decode: Str -> Str
## Examples:
# shift_decode("KHB! Zkhuh brx dw?") -> "HEY! Where you at?"
# shift_decode("Q"* 26 ) -> "Q" * 26
def shift_decode(s):
    alpha= {"a": 1, "b": 2, "c": 3, "d":4, "e":5, "f":6, "g":7, "h":8, "i":9, "j":10, "k": 11, "l": 12, "m":13, "n":14, "o": 15, "p":16, "q": 17, "r": 18, "s":19, "t": 20, "u":21, "v": 22,"w": 23, "x":24, "y":25, "z":0}
    string = ""
    
    for letter in s:
        if letter.isalpha():
            if letter. islower():
                for ind in list(alpha.keys()):
                        if alpha[ind]== ((alpha [letter] - common_letter(s)) % 26):
                            string = string+ ind                        
                    
            else:
                for ind in list(alpha.keys()):
                        if alpha[ind]== ((alpha[letter. lower()]- common_letter(s)) % 26):
                            string = string+ ind. upper()                        
        else:
            string = string+ letter
    
    return string

check.expect("Test 1", shift_decode("efw 23 pl 2"), "dev 23 ok 2")
check.expect("Test 2", shift_decode("HellO FrieNd"), "FcjjM DpgcLb")
check.expect("Test 3", shift_decode("/? hey Yo"), "/? fcw Wm")
check.expect("Test 4",shift_decode("HhHhHhUuUuHhHh"),"XxXxXxKkKkXxXx")
check.expect("Test 5", shift_decode(""), "")
check.expect("Test 6", shift_decode("3468"), "3468")
check.expect("Test 7", shift_decode("H"*(45+1)+ "n"), "N"*(45+1)+ "t")
check.expect("Test 8", shift_decode("HIIII"), "DEEEE")
