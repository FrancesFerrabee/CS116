import check
####################################
## Frances Ferrabee 20712523
## CS 116 Winter 2018
## Assignment 08 Problem 03
####################################

#q3

class Vector:
    '''Fields: x(Int), y(Int)'''
    def __init__(self,xVal,yVal):
        self.x = xVal
        self.y = yVal
        
    def __eq__(self,other):
        if isinstance(other,Vector):
            return self.x == other.x and self.y == other.y
        else:
            return False
        
    def __repr__(self):
        return "Vector({0},{1})".format(self.x,self.y)
          
    
    
    #q3b

    ## __add__(self, others): returns the Vector obtained by adding 2 Vectors together
    ## __add__: Vector Vector -> Vector
    ##Examples:
    ## Vector(2,3)+ Vector(4,-1) -> Vector(6,2)
    ## Vector(0,-5)+ Vector(-2,1) -> Vector(-2,-4)    
    def __add__(self,other):
        return  Vector(self.x+ other.x, self.y+ other.y)
    ## __mul__(self, other): returns the dot product of 2 Vectors
    ## __mul__: Vector Vector -> Int
    ## Examples:
    ## Vector(2,3) * Vector (4, -1)) -> 5
    ## Vector(0, -5)* Vector(-2, 1) -> -5    
    def __mul__(self,other):
        return self.x* other.x+ self.y* other.y
    ## length(): returns the length of the vector
    ## length: Vector -> Float
    ## Examples:
    ## Vector(1,1).length() -> about 1.41
    ## Vector(2,1).length() -> about 2.23    
    def length(self):
        return (self.x**2+ self.y**2)**.5
    ## scale(self,k): returns nothing
    ## Effects: It will mutate vec so that both the x and y coordinates are
    ##* multiplied by k
    ## scale: Vector Int -> None
    ## Examples: 
    ## Vector(2,2).scale(2) mutates Vector(2,2) so it is Vector(4,4)
    ## Vector(-1,0).scale(1) mutates Vector(-1,0) so it is Vector(-1,0)    
    def scale(self,k):
        self.x= self.x* k
        self.y= self.y*k
    
    
    
## Tests for B
check.expect("Test1", Vector(1,1) + Vector(2,1), Vector(3,2))
check.expect("Test2", Vector(0,0) + Vector(2,1), Vector(2,1))
check.expect("Test3", Vector(1,2) + Vector(0,0), Vector(1,2))
check.expect("Test4", Vector(0,0) + Vector(0,0), Vector(0,0))
check.expect("Test5", Vector(-3,-3) + Vector(2,1), Vector(-1,-2))

check.expect("Test1", Vector(1,1) * Vector(2,1), 3)
check.expect("Test2", Vector(0,0) * Vector(2,1), 0)
check.expect("Test3", Vector(1,2) * Vector(0,0), 0)
check.expect("Test4", Vector(0,0) * Vector(0,0), 0)
check.expect("Test5", Vector(-3,-3) * Vector(2,1), -9)

check.within("Test1", Vector(1,2).length(), 2.23, 0.1)
check.within("Test2", Vector(-2,4).length(), 4.47, 0.1)
check.within("Test3", Vector(-3,-1).length(), 3.16, 0.1)
check.within("Test4", Vector(2,2).length(), 2.83, 0.1)

c= Vector(1,2)
check.expect("Test1", c.scale(2), None)
check.expect("Test1", c, Vector(2,4))

d= Vector(3,4)
check.expect("Test2", d.scale(0), None)
check.expect("Test2", d, Vector(0,0))

d= Vector(1,0)
check.expect("Test3", d.scale(2), None)
check.expect("Test3", d, Vector(2,0))

#q3a





## add_vectors(v1, v2): returns the Vector obtained by adding 2 Vectors together
## add_vectors: Vector Vector -> Vector
##Examples:
## add_vectors(Vector(2,3), Vector(4,-1)) -> Vector(6,2)
## add_vectors(Vector(0,-5), Vector(-2,1)) -> Vector(-2,-4)
def add_vectors(v1,v2):
    return Vector(v1.x+ v2.x, v1.y+ v2.y)

check.expect("Test1", add_vectors(Vector(1,1), Vector(2,1)), Vector(3,2))
check.expect("Test2", add_vectors(Vector(0,0), Vector(2,1)), Vector(2,1))
check.expect("Test3", add_vectors(Vector(1,2), Vector(0,0)), Vector(1,2))
check.expect("Test4", add_vectors(Vector(0,0), Vector(0,0)), Vector(0,0))
check.expect("Test5", add_vectors(Vector(-3,-3), Vector(2,1)), Vector(-1,-2))

## dot_product(v1, v2): returns the dot product of 2 Vectors
## dot_product: Vector Vector -> Int
## Examples:
## dot_product(Vector(2,3), Vector (4, -1)) -> 5
## dot_product(Vector(0, -5), Vector(-2, 1)) -> -5
def dot_product(v1,v2):
    return v1.x* v2.x+ v1.y* v2.y

check.expect("Test1", dot_product(Vector(1,1), Vector(2,1)), 3)
check.expect("Test2", dot_product(Vector(0,0), Vector(2,1)), 0)
check.expect("Test3", dot_product(Vector(1,2), Vector(0,0)), 0)
check.expect("Test4", dot_product(Vector(0,0), Vector(0,0)), 0)
check.expect("Test5", dot_product(Vector(-3,-3), Vector(2,1)), -9)

## length(vec): returns the length of the vector
## length: Vector -> Float
## Examples:
## length(Vector(1,1)) -> about 1.41
## length(Vector(2,1)) -> about 2.23
def length(vec):
    return (vec.x**2+ vec.y**2)**.5

check.within("Test1", length(Vector(1,2)), 2.23, 0.1)
check.within("Test2", length(Vector(-2,4)), 4.47, 0.1)
check.within("Test3", length(Vector(-3,-1)), 3.16, 0.1)
check.within("Test4", length(Vector(2,2)), 2.83, 0.1)

## scale(vec,k): returns nothing
## Effects: It will mutate vec so that both the x and y coordinates are
##* multiplied by k
## scale: Vector Int -> None
## Examples: 
## scale(Vector(2,2), 2) mutates Vector(2,2) so it is Vector(4,4)
## scale(Vector(-1,0), 1) mutates Vector(-1,0) so it is Vector(-1,0)
def scale(vec,k):
    vec.x= vec.x* k 
    vec.y= vec.y * k 

c= Vector(1,2)

check.expect("Test1", scale(c, 2), None)
check.expect("Test1", c.x, 2 )
check.expect("Test1", c.y, 4)

d= Vector(3,4)

check.expect("Test2", scale(d, 0), None)
check.expect("Test2", d.x, 0)
check.expect("Test2", d.y, 0)

d= Vector(1,0)

check.expect("Test3", scale(d, 2), None)
check.expect("Test3", d.x, 2 )
check.expect("Test3", d.y, 0)


  

        



    
    
        