class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

def print_dll(head):
    current = head
    while current:
        print(current.data, end=" ")
        current = current.next
    print()

def delete_head(head):
    if head is None:
        return None
    if head.next is None:
        return None

    new_head = head.next
    new_head.prev = None
    return new_head

def delete_tail(head):
    if head is None:
        return None
    if head.next is None:
        return None

    temp = head
    while temp.next.next:
        temp = temp.next

    temp.next = None
    return head

def delete_kth(head, k):
    if head is None:
        return None

    temp = head
    count = 0
    while temp:
        if count == k:
            break
        count += 1
        temp = temp.next

    if temp is None:
        return head

    back = temp.prev
    front = temp.next

    if back is None and front is None:
        return None
    elif back is None:
        return delete_head(head)
    elif front is None:
        return delete_tail(head)
    else:
        back.next = front
        front.prev = back
        return head

def array_to_dll(arr):
    if len(arr) == 0:
        return None

    head = Node(arr[0])
    current = head
    for data in arr[1:]:
        new_node = Node(data)
        current.next = new_node
        new_node.prev = current
        current = new_node
    return head

n, k = map(int, input("Enter Num of El: ").split())
arr = []
if n > 0:
    arr = list(map(int, input("Enter Arr: ").split()))
head = array_to_dll(arr)
head = delete_kth(head, k)
print_dll(head)