#5,7,9,6,8,4,10

list = [5,7,9,6,8,4,10]
listNew= []
for i in range(len(list)-1,1, -1):
    temp=list[i]
    nextValue=temp
    if(nextValue<=list[i]):
        if(list[0]==list[i] | list[0]<list[i] ):
            listNew[i].append(list[i])

print(listNew)




