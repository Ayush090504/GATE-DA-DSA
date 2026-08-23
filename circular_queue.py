def enqueue(front,rear,queue,val):
    if front==rear==-1:
        front,rear=0,0
        queue[rear]=val
    else:
        rear=(rear+1)%MAX_SIZE
        queue[rear]=val
    return front,rear

def dequeue(front,rear,queue):
    print(f"Popped value: {queue[front]}")
    front=(front+1)%MAX_SIZE
    if front==rear:
        front,rear=-1,-1
    return front,rear

def display(queue):
    for i in queue:
        print(i,end=' ')
    print()

MAX_SIZE=int(input('Enter the maximum size of queue: '))
front=-1
rear=-1
queue=[0]*MAX_SIZE
while True:
    op=int(input('Enter the operation to be performed: (1->Enqueue, 2->Dequeue, 3->Display, 4->Exit): '))
    if op==1:
        if (rear+1)%MAX_SIZE==front:
            print('Queue is full!!!')
        else:
            val=int(input('Enter the value: '))
            front,rear=enqueue(front,rear,queue,val)
    elif op==2:
        if front==-1:
            print('The queue is empty!!')
        else:
            front,rear=dequeue(front,rear,queue)
    elif op==3:
        if front==-1:
            print('The queue is empty!!')
        else:
            display(queue)
    elif op==4:
        break
    else:
        print('Invalid operation!!')