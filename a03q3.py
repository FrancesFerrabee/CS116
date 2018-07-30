import math
import check

####################################
## Frances Ferrabee 20712523
## CS 116 Winter 2018
## Assignment 03 Problem 03
####################################


error_msg = 'That is not correct.'

step1_msg = 'Think of a number. Multiply your number by 4:'
step2_msg = 'Add 9:'
step3_msg = 'Subtract the original number:'
step4_msg = 'Divide by 3:'
step5_msg = 'Subtract 3:'
final_msg = 'Your original number is {0}'


## step2(msg1): consumes a number, and determines if the number read is the 
##   9 bigger than the number consumed. If it is 9 bigger than the function will
##   move on to the next stage. Otherwise the function will print an error and
##   will call itself until to user enters the right number.
## Effects:
##* reads a number from the user
##* prints an error if that number is not 9 more than the number consumed
## step2: Nat -> None

def step2 (msg1):
    msg2= int(input(step2_msg))
    if msg2 == msg1 +9:
        return (step3(msg2, msg1))
    else:
        print (error_msg)
        return (step2(msg1))
    
## step3(msg2,msg1): consumes 2 numbers, and determines if the number read is 
##   equal to the second number consumed minus 1/4 the first number consumed.
##   If this is true than the function will move on to the next stage.
##   Otherwise the function will print an error and
##   will call itself until to user enters the right number.
## Effects:
##* reads a number from the user
##* prints an error if that number is not equal to the second number consumed 
##    minus 1/4 the first number consumed.
## step2: Nat Nat-> None    
        
def step3 ( msg2, msg1):
    msg3= int (input(step3_msg))
    if (msg3== msg2- (msg1/4)):
        return(step4(msg3))
    else:
        print(error_msg)
        return(step3( msg2, msg3))
        
## step4(msg3): consumes a number, and determines if the number read is the 
##   1/3 the number consumed. If this is true than the function will
##   move on to the next stage. Otherwise the function will print an error and
##   will call itself until to user enters the right number.
## Effects:
##* reads a number from the user
##* prints an error if that number is 1/3 the number consumed
## step2: Nat -> None

def step4 (msg3):
    msg4= int (input(step4_msg))
    if( msg4== msg3/3):
        return(step5(msg4)) 
    else:
        print(error_msg)
        return(step4(msg3))
        
## step5(msg4): consumes a number, and determines if the number read is the 
##   3 smaller than the number consumed. If it is 3 smaller than the function 
##   will move on to the next stage. Otherwise the function will print an error 
##   and will call itself until to user enters the right number.
## Effects:
##* reads a number from the user
##* prints an error if that number is not 3 less than the number consumed
## step2: Nat -> None

def step5(msg4):
    msg5= int (input(step5_msg))
    if(msg5== msg4-3):
        return (final_msg.format(msg5))
    else:
        print(error_msg)
        return(step5(msg4))
    
    
## number_game(): reads a number in the form of a string
##   and does calculations to get the original number, the user was thinking 
##   of. It prints out this number.
## Effects: 
##* one value is read in 
##* A string is printed
##* If the number is correctly entered another string will be printed
##* The final string printed will give the original number
## number_game: Null -> Null

## Examples:
# If the user enters 32 when the program is run. The program will guide the user
# to do a few calculations though prints. The program will then print the number
# the user was originally thinking of, which is 8


def number_game():
    msg1=int (input(step1_msg))
    print (step2(msg1))
        
        
## Tests:

check.set_input(["32", "41", "33", "11", "8"])
check.set_screen("PROMPTS THEN: Your original number is 8")
check.expect("Test1", number_game(), None)

check.set_input(["24","0", "45", "33","27", "9", "6"])
check.set_screen("PROMPTS AND ERROR MESSAGES THEN: Your original number is 6")
check.expect("Test2", number_game(), None)

check.set_input(["28","37", "30", "10", "7"])
check.set_screen("PROMPTS THEN: Your original number is 7")
check.expect("Test3", number_game(), None)