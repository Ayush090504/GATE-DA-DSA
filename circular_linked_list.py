class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

def insert_at_the_beginning(head):
    val=int(input('Enter the new value to be inserted: '))
    newNode=Node(val)
    if head is None:
        head=newNode
        head.next=head
        return head
    newNode.next=head
    temp=head
    while temp.next != head:
        temp=temp.next
    temp.next=newNode
    head=newNode
    return head

def insert_at_the_end(head):
    val=int(input('Enter the value to be inserted: '))
    newNode=Node(val)
    if head is None:
        head=newNode
        head.next=head
        return head
    temp=head
    while temp.next != head:
        temp=temp.next
    temp.next=newNode
    newNode.next=head
    return head

def traversal(head):
    if head is None:
        print('The linked list is empty!!')
        return head
    temp=head
    while True:
        print(temp.data, end=' ')
        temp=temp.next

        if temp == head:
            break
    print()
    return head

def delete_at_beginning(head):
    if head is None:
        print('The linked list is empty!!')
        return head
    elif head.next==head:
        head=None
        return head
    temp=head
    while temp.next != head:
        temp=temp.next
    head=head.next
    temp.next=head
    return head

def delete_at_end(head):
    if head is None:
        print('The linked list is empty!!')
        return head
    elif head.next == head:
        head=None
        return head
    temp=head
    while temp.next.next != head:
        temp = temp.next
    temp.next=head
    return head

head=None
while True:
    op=int(input('Enter the operation to be performed: '))
    if op == 1:
        head=insert_at_the_beginning(head)
    elif op == 2:
        head=insert_at_the_end(head)
    elif op == 3:
        head=traversal(head)
    elif op == 4:
        head=delete_at_beginning(head)
    elif op == 5:
        head=delete_at_end(head)