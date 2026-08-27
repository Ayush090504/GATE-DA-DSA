class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None

def insert_at_beginning(head):
    val=int(input('Enter the value to be inserted: '))
    newNode=Node(val)
    if head is None:
        head=newNode
        return head
    newNode.next=head
    head.prev=newNode
    head=newNode
    return head

def insertion_at_the_end(head):
    val=int(input('Enter the new value to be inserted: '))
    newNode=Node(val)
    if head is None:
        head=newNode
        return head
    temp=head
    while temp.next is not None:
        temp=temp.next
    temp.next=newNode
    newNode.prev=temp
    return head

def delete_at_the_beginning(head):
    if head is None:
        print('The linked list is empty!!')
        return head
    elif head.next is None:
        head=None
        return head
    head=head.next
    head.prev=None
    return head

def delete_at_the_end(head):
    if head is None:
        print('Linked List is empty!!')
        return head
    elif head.next is None:
        head=None
        return head
    temp=head
    while temp.next is not None:
        temp=temp.next
    temp=temp.prev
    temp.next=None
    return head

def forward_traversal(head):
    if head is None:
        print('The linked list is empty!!')
        return head
    temp=head
    while temp is not None:
        print(temp.data, end=' ')
        temp=temp.next
    print()
    return head

def backward_traversal(tail):
    temp=tail
    while temp is not None:
        print(temp.data)
        temp=temp.prev
    print()

head=None
while True:
    op=int(input('Enter the operation: '))
    if op==1:
        head=insert_at_beginning(head)
    elif op == 2:
        head=insertion_at_the_end(head)
    elif op == 3:
        head=delete_at_the_beginning(head)
    elif op == 4:
        head=delete_at_the_end(head)
    elif op == 5:
        head=forward_traversal(head)
    elif op == 6:
        if head is None:
            print('Linked list is empty!!')
        else:
            tail=head
            while tail.next is not None:
                tail=tail.next
            backward_traversal(tail)
    elif op == 7:
        break