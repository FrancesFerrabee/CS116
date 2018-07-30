import check
####################################
## Frances Ferrabee 20712523
## CS 116 Winter 2018
## Assignment 08 Problem 02
####################################

row_win = "Winner: Row {0}."
column_win = "Winner: Column {0}."
no_win = "Not a winner."

## update_card(crd, lon): returns the updated card where each
##   value of lon in card is replaced with "XX"
## update_card: Bingocard
##         (listof Nat)->Bingocard

def update_card(crd, lon):
    count= 0
    while count < len(lon):
        for row in list(crd.values()):
            col= 0
            while col < len(row):
                if row[col]== lon[count]:
                    if row == crd["O"]:
                        val ="O"
                    elif row == crd["B"]:
                        val = "B"
                    elif row == crd["I"]:
                        val = "I"
                    elif row == crd["G"]:
                        val = "G"
                    else:
                        val = "N"
                    crd[val][col] = "XX"   
                col = col+1
        count=count+1
                      
    return crd      
## rows(crd): returns which row has all "XX" if no row has
##    all "XX" returns False
## rows: Bingocard->(anyof Str False)
def rows(crd):
    count =0
    ind= 0
    while ind < 5:
        for row in list(crd.values()):
                if row[ind] == "XX":
                    count = count+1
                    if count == 5:
                        return row_win.format(ind+1)
                else:
                    count= 0
        ind= ind+1
    return False

## columns(crd): returns which row has all "XX" if no row has
##    all "XX" returns False
## columns: Bingocard-> (anyof Str False)
def columns(crd):
    count = 0
    col= 0
    for row in list(crd.values()):
            ind= 0
            while ind < 5:
                if row[ind]== "XX":
                    count= count+1
                    if count== 5:
                        
                        return column_win.format(list(crd.keys())[col])
                else:
                    count = 0
                ind = ind+1
            col=col+1    
    return False

## play_bingo(crd, lon): returns whether the bingo card has a column win
##   a row win or no win and in which column or row the win is in.
## Effects: Mutates crd
## play_bingo: (dictof Str(listof(anyof Nat "XX"))) (listof Nat) 
##                      -> (dictof Str(listof(anyof Nat "XX")))
# Examples
# my_card= {'O': [65, 62, 'XX', 64, 74], 'I': ['XX', 25, 'XX', 20, 26], 'N': [41, 45, 'XX', 33, 43], 'B': ['XX', 'XX', 14, 'XX', 'XX'], 'G': ['XX', 60, 'XX', 53, 56]}

# play_bingo(my_card,[14]) -> "Winner: Column B."
# Mutates list: {'O': [65, 62, 'XX', 64, 74], 'I': ['XX', 25, 'XX', 20, 26], 'N': [41, 45, 'XX', 33, 43], 'B': ['XX', 'XX', 14, 'XX', 'XX'], 'G': ['XX', 60, 'XX', 53, 56]}
#

# bcard= {'O': [65, 62, 63, 64, 74], 'I': [21, 25, 22, 20, 26], 'N': [41, 45, 34, 33, 43], 'B': [15, 12, 14, 11, 16], 'G': [59, 60, 55, 53, 56]}

# play_bingo(my_card, [14]) -> "Not a winner."
# Mutates list: {'O': [65, 62, 63, 64, 74], 'I': [21, 25, 22, 20, 26], 'N': [41, 45, 34, 33, 43], 'B': [15, 12, "XX", 11, 16], 'G': [59, 60, 55, 53, 56]}

#bcard = {'O': [61, 72, 'XX', 67, 74], 'I': [25, 23, 'XX', 20, 26], 'N': [43, 38, 'XX', 36, 40], 'B': ['XX', 'XX', 6, 'XX', 10], 'G': [56, 53, 'XX', 47, 52]}

# play_bingo(bcard, [6]) -> "Winner: Row 3."
# Mutates list: {'O': [61, 72, 'XX', 67, 74], 'I': [25, 23, 'XX', 20, 26], 'N': [43, 38, 'XX', 36, 40], 'B': ['XX', 'XX', 'XX', 'XX', 10], 'G': [56, 53, 'XX', 47, 52]}


def play_bingo(crd,lon):
    i=0
    while i< len(lon):
        crd = update_card(crd,[lon[i]])
        if columns(crd)== False:
            if rows(crd) == False:
                i= i+1
            else:
                return rows(crd)
                
        else:
            return columns(crd)
    return no_win

bcard = {'O': [61, 72, 'XX', 67, 74], 'I': [25, 23, 'XX', 20, 26], 'N': [43, 38, 'XX', 36, 40], 'B': ['XX', 'XX', 6, 'XX', 10], 'G': [56, 53, 'XX', 47, 52]}


check.expect("Test 1", play_bingo(bcard, [6,3]), "Winner: Row 3.")
check.expect("Test 1", bcard,{'O': [61, 72, 'XX', 67, 74], 'I': [25, 23, 'XX', 20, 26], 'N': [43, 38, 'XX', 36, 40], 'B': ['XX', 'XX', 'XX', 'XX', 10], 'G': [56, 53, 'XX', 47, 52]} )


my_card = {'O': [65, 62, 'XX', 64, 74], 'I': ['XX', 25, 'XX', 20, 26], 'N': [41, 45, 'XX', 33, 43], 'B': ['XX', 'XX', 14, 'XX', 'XX'], 'G': ['XX', 60, 'XX', 53, 56]}

check.expect("Test 2", play_bingo(my_card, [55,50,22]), "Not a winner.")
check.expect("Test 2", my_card,{'O': [65, 62, 'XX', 64, 74], 'I': ['XX', 25, 'XX', 20, 26], 'N': [41, 45, 'XX', 33, 43], 'B': ['XX', 'XX', 14, 'XX', 'XX'], 'G': ['XX', 60, 'XX', 53, 56]} )

my_card = {'O': [65, 62, 'XX', "XX", 74], 'I': ['XX', 25, 'XX', 20, 26], 'N': [41, 45, 'XX', 33, 43], 'B': ['XX', 'XX', 14, 'XX', 'XX'], 'G': ['XX', 60, 'XX', 53, 56]}

check.expect("Test 3", play_bingo(my_card, [14,65,20]), "Winner: Column B.")
check.expect("Test 3", my_card, {'O': [65, 62, 'XX', 'XX', 74], 'I': ['XX', 25, 'XX', 20, 26], 'N': [41, 45, 'XX', 33, 43], 'B': ['XX', 'XX', 'XX', 'XX', 'XX'], 'G': ['XX', 60, 'XX', 53, 56]})

bcard = {'O': ["XX", "XX", 'XX', "XX", "XX"], 'I': ["XX", "XX", 'XX', "XX", "XX"], 'N': ["XX", 38, 'XX', 36, 40], 'B': ['XX', 'XX', 6, 'XX', 10], 'G': ["XX", 53, 'XX', 47, 52]}

check.expect("Test 4", play_bingo(bcard, [6,49,40]), "Winner: Column O.")
check.expect("Test 4", bcard, {'O': ['XX', 'XX', 'XX', 'XX', 'XX'], 'I': ['XX', 'XX', 'XX', 'XX', 'XX'], 'N': ['XX', 38, 'XX', 36, 40], 'B': ['XX', 'XX', 'XX', 'XX', 10], 'G': ['XX', 53, 'XX', 47, 52]})

bcard = {'O': ["XX", "XX", 66, "XX", "XX"], 'I': [23, "XX", 'XX', "XX", "XX"], 'N': ["XX", 38, 'XX', 36, 40], 'B': ['XX', 'XX', 6, 'XX', 10], 'G': ["XX", 53, 'XX', 47, 52]}

check.expect("Test 5", play_bingo(bcard, []), "Not a winner.")
check.expect("Test 5", bcard, {'O': ['XX', 'XX', 66, 'XX', 'XX'], 'I': [23, 'XX', 'XX', 'XX', 'XX'], 'N': ['XX', 38, 'XX', 36, 40], 'B': ['XX', 'XX', 6, 'XX', 10], 'G': ['XX', 53, 'XX', 47, 52]})

bcard = {'O': ["XX", "XX", 66, "XX", "XX"], 'I': [23, "XX", 'XX', "XX", "XX"], 'N': ["XX", 38, 'XX', 36, 40], 'B': ['XX', 'XX', 6, 'XX', 10], 'G': ["XX", 53, 'XX', 47, 52]}

check.expect("Test 6", play_bingo(bcard, [66,23]), "Winner: Column O.")
check.expect("Test 6", bcard,{'O': ['XX', 'XX', 'XX', 'XX', 'XX'], 'I': [23, 'XX', 'XX', 'XX', 'XX'], 'N': ['XX', 38, 'XX', 36, 40], 'B': ['XX', 'XX', 6, 'XX', 10], 'G': ['XX', 53, 'XX', 47, 52]})

bcard = { 'I': [25, 23, 'XX', 20, 26],'O': [61, 72, 'XX', 67, 74],  'N': [43, 38, 'XX', 36, 40], 'B': ['XX', 'XX', 6, 'XX', 10], 'G': [56, 53, 'XX', 47, 52]}


check.expect("Test 7", play_bingo(bcard, [6]), "Winner: Row 3.")
check.expect("Test 7", bcard,{'O': [61, 72, 'XX', 67, 74], 'I': [25, 23, 'XX', 20, 26], 'N': [43, 38, 'XX', 36, 40], 'B': ['XX', 'XX', 'XX', 'XX', 10], 'G': [56, 53, 'XX', 47, 52]} )


