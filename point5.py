'''
This program adds up the elements of a given row.
'''
def sumRow(matrix:list, row:int) -> float: # the function takes a matrix and an integer.
    return sum(matrix[row-1]) # the sum of the elements of the given row is returned (row 1 in the input is equivalent to 0).

# the matrix is built and the function's result is returned.
if __name__ == "__main__":
    matrix = []
    rows = int(input("Enter the number of rows the matrix will contain: "))
    columns = int(input("Enter the number of columns the matrix will contain: "))
    row = int(input("Enter the number of the row whose elements are to be added: "))
    for x in range(rows):
        matrix.append([])
        for y in range(columns):
            num = int(input(f"Enter a number for matrix 1, row {x+1}, column {y+1}: "))
            matrix[-1].append(num)

res = sumRow(matrix, row)
print(res)