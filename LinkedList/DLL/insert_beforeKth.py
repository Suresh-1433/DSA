class Node:
    def __init__(self, value, next_address=None, prev_address=None):
        self.data = value
        self.next = next_address
        self.prev = prev_address

def array_to_DLL(arr):
    if not arr:
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

def insert_head(head, a):
    if head is None:
        return Node(a)
    temp = Node(a, head)
    head.prev = temp
    return temp

def insert_kth(head, k, a):
    temp = head
    count = 0
    while temp:
        if count == k:
            break
        count = count + 1
        temp = temp.next
    if k == 0:
        return insert_head(head, a)
    if count >= k:
        return head
    back = temp.prev
    n = Node(a, temp, back)
    back.next = n
    temp.prev = n
    return head

n, k, data = map(int, input("Enter n and Data :").split())
arr = []
if n > 0:
    arr = list(map(int, input("Enter Arr : ").split()))
head = array_to_DLL(arr)
head = insert_kth(head, k, data)
print_DLL(head)