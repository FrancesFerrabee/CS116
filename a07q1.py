## Make sure to follow question 1 as directed.

# Question 1. 
#
# Determine the worst-case runtime of the following functions. 
# The answer will be stated in terms of the size of the problem.
# Some bounds may appear more than once.
#
# Note. In all cases, choose the 'tightest' bound.
#
# Choose 
# A. O(1)
# B. O(log n)
# C. O(n)
# D. O(n log n)
# E. O(n**2)
# F. O(2**n)

# (a)
# Let n = len(L)
def fn_a(L):
    def helper(M, m):
        n = 0 #O(1)
        for x in M: #O(1)
            if x == m:
                n = n + 1 # O(n )
        return n
    L1 = list(filter(lambda x: x > helper(L, x), L))
    return len(L1)

# (b)
# let n = len(s), c is a string of length 1
def fn_b(s, c):
    if s[0] == c or s[-1] == c:# O(1)
        print('The begins or ends with {0}'.format(c))

# (c)
# n is a natural number
def fn_c(n):
    if n == 0:
        return 1 #O(1)
    elif n % 2 == 0:
        return fn_c(n - 1) + fn_c(n - 1) ** 2
    else:
        return 2 * fn_c(n - 1)

# (d)
# let n = len(L)
def fn_d(L, x):
    for i in range(len(L)): # O(n)
        j = i
    while j < len(L): # O(n)
        if L[i] + L[j] == x:
            return i + j # O(1)
        j = j + 1
    return -1

# (e)
# let n = len(s)
def fn_e(s):
    s1 = list(filter(lambda c: c.isdigit(), s))
    s2 = list(filter(lambda c: c.isupper(), s))
    s3 = list(filter(lambda c: c.islower(), s))
  
    return s1 + s2 + s3

# (f)
# let n = len(L)
def fn_f(L):
    def helper(M, n):
        m = n // 2
        if n >= len(M):
            return 1
        if M[n] > M[0]:
            return M[0] + helper(M, m)
        return M[0] + M[n] #O(1)
    return helper(L, len(L) - 1)

# Place one of A,B,C,D,E or F inside the string quotes;
#e.g., if you think fn_a has a running time of O(2**n),
#then change a_answer = "" to a_answer = "F".
#
# Choose:
# A. O(1)
# B. O(log n)
# C. O(n)
# D. O(n log n)
# E. O(n**2)
# F. O(2**n)

a_answer = "E"
b_answer = "A"
c_answer = "F"
d_answer = "E"
e_answer = "C"
f_answer = "C"