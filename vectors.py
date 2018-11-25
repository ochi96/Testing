def add_vectors(vector1,vector2):
    '''takes two lists of numbers of the same length
    and returns a new list containing the sums of the
    corresponding elements of each'''
    if type(vector1)!=list:
        print('enter a list')
    elif type(vector2)!=list:
        print('enter a list')
    else:
        a=[]
        for i in range(len(vector1)):
            b=vector1[i]+vector2[i]
            a.append(b)
        return(a)

def scalar_mult(scalar,vector2):
    '''takes a scalar and multiplies it with a vector and
    returns the result'''
    a=[]
    for i in range(len(vector2)):
        c=scalar*vector2[i]
        a.append(c)
    return(a)

def dot_product(vector1,vector2):
    '''takes 2 vectors of the same length and gives their
    dot product'''
    if type(vector1)!=list:
        print('enter a list')
    elif type(vector2)!=list:
        print('enter a list')
    else:
        a=[]
        for i in range(len(vector1)):
            b=vector1[i]*vector2[i]
            a.append(b)
            c=sum(a)
        return(c)
        
    
    
