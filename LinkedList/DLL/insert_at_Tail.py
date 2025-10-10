class Node:
    def __init__(self, value, next_address=None, prev_address=None):
        self.data = value
        self.next = next_address
        self.prev = prev_address

def array_to_DLL(arr):
    if len(arr) == 0:
        return None
    head = Node(arr[0])
    cur = head
    for value in arr[1:]:
        temp = Node(value)
        temp.prev = cur
        cur.next = temp
        cur = temp
    return head

def print_DLL(head):
    while head:
        print(head.data, end=" ")
        head = head.next

def insert_tail(head, a):
    if head is None:
        return Node(a)
    tail = head
    while tail.next:
        tail = tail.next
    temp = Node(a, None, tail)
    tail.next = temp
    return head


n, data = map(int, input("Enter n and Data : ").split())
arr = []
if n > 0:
    arr = list(map(int, input("Enter Arr : ").split()))
head = array_to_DLL(arr)
head = insert_tail(head, data)
print_DLL(head)