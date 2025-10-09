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

def insert_at_tail(head, data):
    if head is None:
        new_node = Node(data)
        return new_node
    temp = head
    while temp.next:
        temp = temp.next
    new_node = Node(data)
    temp.next = new_node
    return head

n, a = map(int, input().split())
arr = []
if n > 0:
    arr = list(map(int, input().split()))
head = array_to_LL(arr)
head = insert_at_tail(head, a)
print_LL(head)