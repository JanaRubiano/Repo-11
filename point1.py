'''
This code calculates the sum/substraction of two matrices.
'''


def matrixAddition(m1:list, m2:list) -> list: # the function takes two matrices.
    m_sum = [] # a matrix is created to store the result of the matrix addition.
    for i in range(len(m1)): # matrix one is iterated.
        m_sumx = [] # a list is created to store the rows.
        for j in range(len(m1[0])): # the elements of each row in the matrix are iterated.
            sumat = m1[i][j] + m2[i][j] # the elements at the same indices in both matrices are added.
            m_sumx.append(sumat) # the result of the sum is added to the row.
        m_sum.append(m_sumx) # the row is appended to the resutl matrix.
        
    return m_sum


# the same process is done when substracting matrices. The only change is the operation (-).
def matrixSubstraction(m1:list, m2:list) -> list:
    m_sum = []
    for i in range(len(m1)):
        m_sumx = []
        for j in range(len(m1[i])):
            sumat = m1[i][j] - m2[i][j]
            m_sumx.append(sumat)
        m_sum.append(m_sumx)
    return m_sum

if __name__ == "__main__":
    list1 = []
    list2 = []
    rows = int(input("Enter the number of rows both matrices will contain: "))
    columns = int(input("Enter the number of columns both matrices will contain: "))
    for x in range(rows):
        list1.append([])
        for y in range(columns):
            num = int(input(f"Enter a number for matrix 1, row {x+1}, column {y+1}: "))
            list1[-1].append(num)

    for x in range(rows):
        list2.append([])
        for y in range(columns):
            num = int(input(f"Enter a number for matrix 2, row {x+1}, column {y+1}: "))
            list2[-1].append(num)

    operation = input("Enter the sign (+/-) of the operation: ")
    if operation == "-":
        res = matrixSubstraction(list1, list2)
    if operation == "+":
        res = matrixAddition(list1, list2)
    print(*res, sep='\n')