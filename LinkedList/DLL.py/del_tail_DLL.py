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

def delete_tail(head):
    if head is None:
        return head
    if head.next is None:
        del head
        return None
    temp = head
    while temp.next.next is not None:
        temp = temp.next
    tail = temp.next
    temp.next = None
    tail.prev = None
    del tail
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

n = int(input("Enter num n: "))
arr = []
if n > 0:
    arr = list(map(int, input("Enter arr: ").split()))
head = array_to_dll(arr)
head = delete_tail(head)
print_dll(head)