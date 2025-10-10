class Node:
    def __init__(self, data=0, next=None):
        self.data = data
        self.next = next

def array_to_LL(arr):
    if not arr:
        return None
    head = Node(arr[0])
    temp = head
    for value in arr[1:]:
        temp.next = Node(value)
        temp = temp.next
    return head

def print_LL(head):
    temp = head
    while temp:
        print(temp.data, end=" ")
        temp = temp.next
    print()

def insert_x(head, x, a):
    if head is None:
        return None
    if head.data == x:
        return Node(a, head)
    temp = head
    while temp.next:
        if temp.next.data == x:
            new_node = Node(a)
            new_node.next = temp.next
            temp.next = new_node
            break
        temp = temp.next
    return head
    
n, x, data = map(int, input().split())
arr = []
if n > 0:
    arr = list(map(int, input().split()))
head = array_to_LL(arr)
head = insert_x(head, x, data)
print_LL(head)