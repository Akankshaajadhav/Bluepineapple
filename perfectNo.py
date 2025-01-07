#To print all the perfect numbers between 1 to num

num=int(input("Enter number"))
perfectNum=[]
divSum=0
for i in range(1,num):
    divSum=0
    for j in range(1,i//2+1):
        if i%j==0:
            divSum+=j
    if(divSum==i):
        perfectNum.append(i)
print(perfectNum)

        

