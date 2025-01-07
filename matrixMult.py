r1=int(input("No. of rows of first matrix : "))
c1=int(input("No. of columns of first matrix : "))
r2=int(input("No. of rows of second matrix : "))
c2=int(input("No. of columns of second matrix : "))

matrix1=[]
matrix2=[]
multMatrix=[]
if c1==r2:
    print("Enter matrix elements : ")
    for i in range(r1):
        row=[]
        for j in range(c1):
            row.append(int(input()))
        matrix1.append(row)

    for i in range(r2):
        row=[]
        for j in range(c2):
            row.append(int(input()))
        matrix2.append(row)

    for i in range(r1):
        row=[]
        for j in range(c2):
            sum=0
            for k in range(c1):
                sum+=matrix1[i][k]*matrix2[k][j]
            row.append(sum)
        multMatrix.append(row)
    
    print("Multiplication of above matrices is : ")
    print(multMatrix)
    
else:
    print("Enter appropriate matrix dimensions")

