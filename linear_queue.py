def enqueue(val,queue,front,rear):
    if front==-1 and rear==-1:
        front+=1
        rear+=1
        queue[rear]=val
    else:
        rear+=1
        queue[rear]=val
    return front,rear

def dequeue(queue,front,rear):
    val=queue[front]
    if front == rear:
        front=-1
        rear=-1
    else:
        front+=1
    return front,val,rear

MAX_SIZE=int(input('Enter the maximum size of the queue: '))
front,rear=-1,-1
queue=[0]*MAX_SIZE
while True:
    op=int(input('Enter the operation to perform (1-> Enqueue(insert), 2->Dequeue(pop), 3->Exit): '))
    if op==1:
        if rear>=MAX_SIZE-1:
            print("Queue is full!!")
        else:
            val=int(input('Enter the value to insert: '))
            front,rear=enqueue(val,queue,front,rear)
    elif op==2:
        if front==-1:
            print('Queue is empty!!')
        else:
            front,val,rear=dequeue(queue,front,rear)
            print(f'Popped element: {val}')
    elif op==3:
        break
    else:
        print("Invalid Operation!!")