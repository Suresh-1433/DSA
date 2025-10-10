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

def insert_kth(head, k, value):
    if head is None:
        if k == 0:
            return Node(value)
        else:
            return None
    if k == 0:
        return Node(value, head)
    
    temp = head
    for _ in range(k - 1):
        if temp is None:
            return head
        temp = temp.next
    
    if temp is None:
        return head
    new_node = Node(value)
    new_node.next = temp.next
    temp.next = new_node
    return head


n, k, data = map(int, input().split())
arr = []
if n > 0:
    arr = list(map(int, input().split()))
head = array_to_LL(arr)
head = insert_kth(head, k, data)
print_LL(head)