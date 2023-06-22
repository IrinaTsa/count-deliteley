x=int(input('Введите число '))
count=0
for i in range(1,x+1):
    if  x%i==0:
        print(i)
        count+=1
print('количество делителей  ',count)
