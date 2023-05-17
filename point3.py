'''
This code transposes a matrix.
'''
def transposedMatrixPro(matrix:list) -> list: # the function takes a matrix.
    return list(zip(*matrix)) # it transposes the matrix using zip, beeing the iterable the lists contained in the matrix list.


# this is another way to solve the same task.
def transposedMatrix(matrix:list) -> list: 
    tr_matrix = []
    for j in range(len(matrix[0])):
        row = [matrix[i][j] for i in range(len(matrix))]
        tr_matrix.append(row)
    return tr_matrix


if __name__ == "__main__":
    matrix = []
    rows = int(input("Enter the number of rows the matrix will contain: "))
    columns = int(input("Enter the number of columns the matrix will contain: "))
    for x in range(rows):
        matrix.append([])
        for y in range(columns):
            num = int(input(f"Enter a number for matrix 1, row {x+1}, column {y+1}: "))
            matrix[-1].append(num)

res1 = transposedMatrix(matrix)
res2 = transposedMatrixPro(matrix)
print(*res1, sep='\n')
print(*res2, sep='\n')