'''
This code returns the product of two matrices.
'''
def prodMatrix(m1:list, m2:list) -> list: # the functions takes two matrices.
    prod_matrix = [] # an empty list is created for later storing the product matrix.
    t_matrix = list(zip(*m2)) # one of the lists is transposed for the operation to be easier.
    for i in range(len(m1)): # the first matrix is iterated.
        x_row = [] # a list is created to store the rows.
        for x in range(len(m1)): # the same list is iterated for a second time, this is done to optain the required matrix indices.
            x_value = sum([m1[x][j]*t_matrix[i][j] for j in range(len(m2))]) # the j value in the first list is multiplied by the j value of the second list.
            x_row.append(x_value) # the resulting value of the multiplication is added to the x_row list.
        prod_matrix.append(x_row) # the x_row list is appended to the prod_matrix.
        

    return list(zip(*prod_matrix)) # prod_matrix is transposed at the end to return it correctly. 

if __name__ == "__main__":
    m1 = []
    m2 = []
    d1 = int(input("Enter the number of rows matrix 1 will contain and the number of columns matrix 2 will contain: "))
    d2 = int(input("Enter the number of columns matrix 1 will contain and the number of rows matrix 2 will contain: "))
    for x in range(d1):
        m1.append([])
        for y in range(d2):
            num = int(input(f"Enter a number for matrix 1, row {x+1}, column {y+1}: "))
            m1[-1].append(num)

    for x in range(d2):
        m2.append([])
        for y in range(d1):
            num = int(input(f"Enter a number for matrix 2, row {x+1}, column {y+1}: "))
            m2[-1].append(num)
    
    res = prodMatrix(m1, m2)
    print(*res, sep='\n')