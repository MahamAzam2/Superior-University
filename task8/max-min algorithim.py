import math

score = [1,2,3,4]
Tree_depth =(math.log(len(score),2))


def minmax(curr_depth,curr_index, is_Max):
    
    if(curr_depth == Tree_depth):
        return score[curr_index]
    
    if(is_Max):
        return max(minmax(curr_depth+1,curr_index*2,False),minmax(curr_depth+1,curr_index*2+1,False))
    
    else:
        return min(minmax(curr_depth+1,curr_index*2,True),minmax(curr_depth+1,curr_index*2+1,True))

print(minmax(0,0,True))