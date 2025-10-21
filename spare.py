def readMatrix():
    rows =int(input("Enter number of rows: "))
    cols =int(input("Enter number of columns: "))
    #initialize matrix
    matrix=[[0 for i in range(cols)] for j in range(rows)]
        #reading data fore the matrix
    for i in range(rows):
        for j in range(cols):
            print("entere matric element",i,j,":  ",end="" )
            matrix[i][j]=int(input())
    return matrix
def showMatrix(matrix):
    print("The matrix is:")
    for col in matrix:
        for val in col:
            print(val, end=" ")
        print()   
def toSpareMatrix(matrix):
   spareMatrix=[]
   for i in range (len (matrix)):
       for j in range (len (matrix [0])):
           if matrix [i][j] != 0:
                remp=[]
                #append row index
                remp.append(i)
                #append column index
                remp.append(j)
                #append value
                remp.append(matrix[i][j])
                spareMatrix.append(remp)
   return spareMatrix
# Tüm fonksiyon tanımlarınız burada bitiyor...

mq=readMatrix()
showMatrix(mq)