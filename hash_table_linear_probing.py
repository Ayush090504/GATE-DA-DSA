
SIZE=int(input('Enter the maximum size of the Hash table: '))
table=[None]*SIZE
index=0
while True:
    op=int(input('Enter the operation you want to perform (1-> Insert, 2->Display, 3->Exit): '))
    if op==1:
        val=int(input("Enter the value to be inserted: "))
        index=val%SIZE
        while table[index]!=None:
            if index<SIZE-1:
                index+=1
            else:
                index=0
        table[index]=val
    elif op==2:
        for element in table:
            print(element,end=' ')
        print()
    elif op==3:
        break
    else:
        print('Invalid option!!')
