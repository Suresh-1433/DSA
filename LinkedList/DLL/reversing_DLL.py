class Node:
    def __init__(self, value, next_address=None, prev_address=None):
        self.data = value
        self.next = next_address
        self.prev = prev_address


def array_to_DLL(arr):
    head = Node(arr[0])
    cur = head
    for i in range(1, len(arr)):
        temp = Node(arr[i])
        temp.prev = cur
        cur.next = temp
        cur = temp
    return head

def print_DLL(head):
    while head is not None:
        print(head.data, end=" ")
        head = head.next


def reverse_DLL(head):
    if head is None or head.next is None:
        return head
    back = None
    cur = head
    while cur is not None:
        back = cur.prev
        cur.prev = cur.next
        cur.next = back
        cur = cur.prev
    return back.prev


n = int(input("Enter the Num : "))
arr = list(map(int, input("Enter the Arr: ").split()))
head = array_to_DLL(arr)
head = reverse_DLL(head)
print_DLL(head)
