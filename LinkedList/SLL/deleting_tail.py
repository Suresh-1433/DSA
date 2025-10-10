class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

def array_to_LL(arr):
    if not arr:
        return None
    head = Node(arr[0])
    cur = head
    for data in arr[1:]:
        cur.next = Node(data)
        cur = cur.next
    return head

def printLL(head):
    while head:
        print(head.data, end=" ")
        head = head.next

def delete_tail(head):
    if not head or not head.next:
        return None
    temp = head
    while temp.next.next:
        temp = temp.next
    temp.next = None
    return head

n = int(input())
arr = []
if n > 0:
    arr = list(map(int, input().split()))
head = array_to_LL(arr)
head = delete_tail(head)
printLL(head)