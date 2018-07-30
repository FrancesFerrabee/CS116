import check
import math
####################################
## Frances Ferrabee 20712523
## CS 116 Winter 2018
## Assignment 08 Problem 04
####################################
acute_cat = 'ACUTE'
obtuse_cat = 'OBTUSE'
right_cat = 'RIGHT'
par_cat = 'PARALLEL'

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

## classify_angles(lov, vec): returns a dictionary where all the vectors 
##   are placed into a category based on the angle between the vector and vec.
## classify_angles: (listof Vector) Vector -> 
##         (dicof (anyof "ACUTE" "PARALLEL" "RIGHT" "OBTUSE") Vector)
## Examples: 
##  vecs= [Vector(-4,0), Vector(0,-7), Vector(10,5), Vector(-1,7), Vector(-5,-3), Vector(4,-6), Vector(-1,7), Vector(-9,3)]
## classify_angles(vecs, Vector(3,0)) -> {"ACUTE": [Vector(10,5), Vector(4,-6)], "OBTUSE": [Vector(-1,7), Vector(-5,-3), Vector(-9,3)],"RIGHT": [Vector(0,-7)],"Parallel": [Vector(-4,0)] }
## classify_angles(vecs, Vector(-2,3)) -> {"ACUTE": [Vector(-4,0), Vector(-1,7), Vector(-5,-3), Vector(-9,3)], "OBTUSE": [Vector(0,-7), Vector(10,5)], "RIGHT":[], "PARALLEL": [Vector(4,-6)]}
def classify_angles(lov,vec):
    vals={}
    acute_so_far= []
    obtuse_so_far=[]
    right_so_far= []
    parallel_so_far=[]
    i= 0

    
    while i< len(lov):
        top = lov[i].x* vec.x+ lov[i].y* vec.y
        vec_length = math.sqrt(pow(vec.x,2)+ pow(vec.y,2))
        lov_length = math.sqrt(pow(lov[i].x, 2) + pow(lov[i].y,2))
        angle= top/ (vec_length * lov_length)
        if pow(top,2) == (pow(vec.x,2)+ pow(vec.y,2))*(pow(lov[i].x, 2) + pow(lov[i].y,2)) :
            if lov[i] in parallel_so_far:
                pass
            else:
                parallel_so_far= parallel_so_far + [lov[i]]
        elif top== 0:
            if lov[i] in right_so_far:
                pass
            else:
                right_so_far= right_so_far+ [lov[i]]
        elif angle> 0 and angle < 90:
            if lov[i] in acute_so_far:
                pass
            else:
                acute_so_far = acute_so_far+ [lov[i]]
                
        else:
            if lov[i] in obtuse_so_far:
                pass
            else:
                obtuse_so_far = obtuse_so_far + [lov[i]]
        i = i+1
    vals["ACUTE"] = acute_so_far
    vals['OBTUSE']= obtuse_so_far
    vals['RIGHT'] = right_so_far
    vals['PARALLEL'] = parallel_so_far

    return vals


  ##Tests:
vecs= [Vector(2,3), Vector(1,1), Vector(1,3), Vector(2,2), Vector(3,4), Vector(1,0)]
  
check.expect("Test 1", classify_angles(vecs, Vector(2,3)),{'ACUTE': [Vector(1,1), Vector(1,3), Vector(2,2), Vector(3,4), Vector(1,0)], 'OBTUSE': [], 'RIGHT': [], 'PARALLEL': [Vector(2,3)]})
check.expect("Test 2", classify_angles(vecs, Vector(0,3)),{'ACUTE': [Vector(2,3), Vector(1,1), Vector(1,3), Vector(2,2), Vector(3,4)], 'OBTUSE': [], 'RIGHT': [Vector(1,0)], 'PARALLEL': []}) 
check.expect("Test 3", classify_angles(vecs, Vector(1,1)),{'ACUTE': [Vector(2,3), Vector(1,3), Vector(3,4), Vector(1,0)], 'OBTUSE': [], 'RIGHT': [], 'PARALLEL': [Vector(1,1), Vector(2,2)]})

vec2= [Vector(3,4), Vector(-1,-4), Vector(0,2), Vector(2,4)]
check.expect("Test 4", classify_angles(vec2, Vector(-2,3)),{'ACUTE': [Vector(3,4), Vector(0,2), Vector(2,4)], 'OBTUSE': [Vector(-1,-4)], 'RIGHT': [], 'PARALLEL': []})
check.expect("Test 5", classify_angles(vec2, Vector(1,0)),{'ACUTE': [Vector(3,4), Vector(2,4)], 'OBTUSE': [Vector(-1,-4)], 'RIGHT': [Vector(0,2)], 'PARALLEL': []}) 
check.expect("Test 6", classify_angles(vec2, Vector(1,-2)),{'ACUTE': [Vector(-1,-4)], 'OBTUSE': [Vector(3,4), Vector(0,2), Vector(2,4)], 'RIGHT': [], 'PARALLEL': []})
    
vec3= []
check.expect("Test 7", classify_angles(vec3, Vector(1,1)),{'ACUTE': [], 'OBTUSE': [], 'RIGHT': [], 'PARALLEL': []})