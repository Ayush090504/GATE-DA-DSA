SIZE=int(input("Enter the maximum size of hash table: "))
table=[None]*SIZE
index=0
while True:
    op=int(input("Enter the operation to be performed (1-> Insertion, 2-> Display, 3->Exit): "))
    if op==1:
        key=int(input("Enter the key to be inserted: "))
        for i in range(SIZE):
            index=(key+i**2)%SIZE
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