# Heavily inspired by medium article: https://medium.aisultan.xyz/@jacob.d.moore1/coding-the-simplex-algorithm-from-scratch-using-python-and-numpy-93e3813e6e70
import numpy as np 

# Generates matrix based on the constraints and variables
def generate_matrix(variables,constraints):    
    table = np.zeros((constraints+1, variables+constraints+2))    
    return table

# Checks furthest right column for negative values. If found, another pivot is required 
def next_round_r(table):    
    minimum_value = min(table[:-1,-1])    
    if minimum_value >= 0:        
        return False    
    else:        
        return True

# Checks bottom row for negative values. If found, another pivot is required
def next_round(table):    
    length_row = len(table[:,0])   
    minimum_value = min(table[length_row-1,:-1])    
    if minimum_value>=0:
        return False
    else:
        return True

# Shows index of negative value of furtherst right column
def find_neg_r(table):
    length_column = len(table[0,:])
    minimum_value = min(table[:-1,lc-1])
    if minimum_value<=0:        
        n = np.where(table[:-1,lc-1] == m)[0][0]
    else:
        n = None
    return n

# Shows index of negative value of bottom row
def find_neg(table):
    length_row = len(table[:,0])
    minimum_value = min(table[length_row-1,:-1])
    if minimum_value<=0:
        n = np.where(table[length_row-1,:-1] == minimum_value)[0][0]
    else:
        n = None
    return n

# Locate pivot element in the furthest column
def loc_piv_r(table):
    total = []        
    r = find_neg_r(table)
    row = table[r,:-1]
    minimum_value = min(row)
    c = np.where(row == minimum_value)[0][0]
    col = table[:-1,c]
    for i, b in zip(col,table[:-1,-1]):
        if i**2>0 and b/i>0:
            total.append(b/i)
        else:                
            total.append(10000)
    index = total.index(min(total))        
    return [index,c]

# Locate pivot element in the row
def loc_piv(table):
    if next_round(table):
        total = []
        n = find_neg(table)
        for i,b in zip(table[:-1,n],table[:-1,-1]):
            if b/i >0 and i**2>0:
                total.append(b/i)
            else:
                total.append(10000)
        index = total.index(min(total))
        return [index,n]

# Pivots table so that negative elements are removed from last row and column
def pivot(row,col,table):
    lr = len(table[:,0])
    lc = len(table[0,:])
    t = np.zeros((lr,lc))
    pr = table[row,:]
    if table[row,col]**2>0:
        e = 1/table[row,col]
        r = pr*e
        for i in range(len(table[:,col])):
            k = table[i,:]
            c = table[i,col]
            if list(k) == list(pr):
                continue
            else:
                t[i,:] = list(k-r*c)
        t[row,:] = list(r)
        return t
    else:
        print('Cannot pivot on this element.')

# Converts the sign (e.g. <=) of constraint into required tabular form 
def convert(eq):
    eq = eq.split(',')
    if 'G' in eq:
        g = eq.index('G')
        del eq[g]
        eq = [float(i)*-1 for i in eq]
        return eq
    if 'L' in eq:
        l = eq.index('L')
        del eq[l]
        eq = [float(i) for i in eq]
        return eq
        
# For a minimization problem, last row of elements should be multiplied by factor of -1
def convert_min(table):
    table[-1,:-2] = [-1*i for i in table[-1,:-2]]
    table[-1,-1] = -1*table[-1,-1]    
    return table

# Generates variables x1, x2... based on the inputted table 
def gen_var(table):
    length_column = len(table[0,:])
    length_row = len(table[:,0])
    var = length_column - length_row -1
    v = []
    for i in range(var):
        v.append('x'+str(i+1))
    return v

# Check whether you can add another constraint to a linear function
def add_cons(table):
    length_row = len(table[:,0])
    empty = []
    for i in range(length_row):
        total = 0
        for j in table[i,:]:                       
            total += j**2
        if total == 0: 
            empty.append(total)
    if len(empty)>1:
        return True
    else:
        return False

# Add Constraint to a matrix
def constrain(table,eq):
    if add_cons(table) == True:
        length_column = len(table[0,:])
        length_row = len(table[:,0])
        var = length_column - length_row -1      
        j = 0
        while j < length_row:            
            row_check = table[j,:]
            total = 0
            for i in row_check:
                total += float(i**2)
            if total == 0:                
                row = row_check
                break
            j +=1
        eq = convert(eq)
        i = 0
        while i<len(eq)-1:
            row[i] = eq[i]
            i +=1        
        row[-1] = eq[-1]
        row[var+j] = 1    
    else:
        print('Cannot add another constraint.')

# Check whether objective function can be added
def add_obj(table):
    lr = len(table[:,0])
    empty = []
    for i in range(lr):
        total = 0        
        for j in table[i,:]:
            total += j**2
        if total == 0:
            empty.append(total)    
    if len(empty)==1:
        return True
    else:
        return False

# Add objective function to a matrix
def obj(table,eq):
    if add_obj(table):
        eq = [float(i) for i in eq.split(',')]
        length_row = len(table[:,0])
        row = table[length_row-1,:]
        i = 0        
        while i<len(eq)-1:
            row[i] = eq[i]*-1
            i +=1
        row[-2] = 1
        row[-1] = eq[-1]
    else:
        print('You must finish adding constraints before the objective function can be added.')

# Maximixation optimization function 
def maxz(table):
    while next_round_r(table):
        table = pivot(loc_piv_r(table)[0],loc_piv_r(table)[1],table)
    while next_round(table):
        table = pivot(loc_piv(table)[0],loc_piv(table)[1],table)        
    length_column = len(table[0,:])
    length_row = len(table[:,0])
    var = length_column - length_row -1
    i = 0
    val = {}
    for i in range(var):
        col = table[:,i]
        s = sum(col)
        m = max(col)
        if float(s) == float(m):
            loc = np.where(col == m)[0][0]            
            val[gen_var(table)[i]] = table[loc,-1]
        else:
            val[gen_var(table)[i]] = 0
    val['max'] = table[-1,-1]
    return val


def minz(table):
    table = convert_min(table)
    while next_round_r(table):
        table = pivot(loc_piv_r(table)[0],loc_piv_r(table)[1],table)    
    while next_round(table):
        table = pivot(loc_piv(table)[0],loc_piv(table)[1],table)       
    length_column = len(table[0,:])
    length_row = len(table[:,0])
    var = length_column - length_row -1
    i = 0
    val = {}
    for i in range(var):
        col = table[:,i]
        s = sum(col)
        m = max(col)
        if float(s) == float(m):
            loc = np.where(col == m)[0][0]             
            val[gen_var(table)[i]] = table[loc,-1]
        else:
            val[gen_var(table)[i]] = 0 
            val['min'] = table[-1,-1]*-1
    return val

''' My function: 
        z = x + 2y
        2x + y ≤ 10
        -4x + 5y ≤ 8
        x - 2y ≤ 3
        x, y ≥ 0 
'''
if __name__ == "__main__":
    m = generate_matrix(2,3)
    constrain(m,'2,1,L,10')
    constrain(m,'-4,5,L,8')
    constrain(m,'1,-2,L,3')
    obj(m,'1,2,0')
    print(maxz(m))