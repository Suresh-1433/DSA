class Node:
    def __init__(self, value, next=None):
        self.data = value
        self.next = next

def array_to_LL(arr):
    head = Node(arr[0]) if arr else None
    cur = head
    for i in range(1, len(arr)):
        cur.next = Node(arr[i])
        cur = cur.next
    return head

def print_LL(head):
    temp = head
    while temp:
        print(temp.data, end=" ")
        temp = temp.next

def reverse_LL(head):
    prev = None
    cur = head
    while cur:
        front = cur.next
        cur.next = prev
        prev = cur
        cur = front
    return prev


if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().split()))
    head = array_to_LL(arr)
    head = reverse_LL(head)
    print_LL(head)
