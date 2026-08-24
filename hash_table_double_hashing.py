SIZE=int(input('Enter the maxium size of table: '))
r=int(input('Enter the Prime limit of second hash function: '))
index=0
table=[None]*SIZE
while True:
    op=int(input('Enter the operation to be performed (1->Insert, 2->Display, 3->Exit): '))
    if op==1:
        key=int(input('Enter the Key to be inserted: '))
        h1=key%SIZE
        h2=r-(key%r)
        for i in range(SIZE):
            index=(h1+i*h2)%SIZE
            if table[index] is None:
                table[index]=key
                break
    elif op==2:
        for element in table:
            print(element,end=' ')
        print()
    elif op==3:
        break
    else:
        print('Invalid Operation!!!')   
