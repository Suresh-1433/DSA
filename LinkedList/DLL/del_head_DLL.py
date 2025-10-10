class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

def print_dll(head):
    while head:
        print(head.data, end=" ")
        head = head.next
    print()

def delete_head(head):
    if not head:
        return None
    if not head.next:
        return None
    head = head.next
    head.prev = None
    return head

def array_to_dll(arr):
    if not arr:
        return None
    head = Node(arr[0])
    current = head
    for data in arr[1:]:
        new_node = Node(data)
        current.next = new_node
        new_node.prev = current
        current = new_node
    return head


n = int(input("enter n: "))
arr = []
if n > 0:
    arr = list(map(int, input("enter array: ").split()))
head = array_to_dll(arr)
head = delete_head(head)
print_dll(head)