class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

head=None
while True:
    op=int(input('Enter the operation to be performed: '))
    