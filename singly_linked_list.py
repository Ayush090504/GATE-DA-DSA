class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

def insertion_beginning(head,val):
    newNode=Node(val)
    newNode.next=head
    head=newNode
    return head

def insertion_end(head,val):
    newNode=Node(val)
    if head is None:
        head=newNode
        return head
    temp=head
    while temp.next!=None:
        temp=temp.next
    temp.next=newNode
    return head


def deletion_beginning(head):
    if head is None:
        print('Linked List is empty!!')
        return head
    temp=head
    head=head.next
    temp.next=None
    return head

def deletion_end(head):
    if head is None:
        print('Linked List is empty!!')
        return head
    elif head.next is None:
        head=None
        return head
    temp=head
    while temp.next.next is not None:
        temp=temp.next
    temp.next=None
    return head

def traversal(head):
    if head is None:
        print('Linked List is empty!!')
    else:
        temp=head
        while temp is not None:
            print(temp.data)
            temp=temp.next

def insert_at_position(head):
    position=int(input('Enter the position at which you want to inser the new node: '))
    val=int(input('Enter the value to be inserted: '))
    newNode=Node(val)
    if position==1:
        head=insertion_beginning(head,val)
        return head
    elif head==None:
        print('Invalid Position')
        return head
    temp=head
    for i in range(position-2):
        if temp.next is None:
            print('Invalid position!!')
            return head
        temp=temp.next
    loc=temp.next
    temp.next=newNode
    newNode.next=loc
    return head

head=None
while True:
    op=int(input('Enter the operation to be performed (1-> Insert in the beginning, 2-> Insert in end, 3->Insert at a given position 4->Delete at start, 5->Delete at end, 6->Traverse, 7->Exit): '))
    if op==1:
        val=int(input('Enter the value to be inserted: '))
        head=insertion_beginning(head,val)
    elif op==2:
        val=int(input('Enter the value to be inserted: '))
        head=insertion_end(head,val)
    elif op==3:
        head=insert_at_position(head)
    elif op==4:
        head=deletion_beginning(head)
    elif op==5:
        head=deletion_end(head)
    elif op==6:
        traversal(head)
    elif op==7:
        break
    else:
        print('Invalid Option!!!')