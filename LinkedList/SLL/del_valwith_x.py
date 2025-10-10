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

def delete_x(head, x):
    if head is None:
        return head
    if x == head.data:
        temp = head
        head = head.next
        return head
    temp = head
    while temp.next is not None:
        if x == temp.next.data:
            n = temp.next
            temp.next = temp.next.next
            break
        temp = temp.next
    return head

if __name__ == "__main__":
    n, x = map(int, input().split())
    arr = []
    if n > 0:
        arr = list(map(int, input().split()))
    head = array_to_LL(arr)
    head = delete_x(head, x)
    printLL(head)
    
    #5 20
    #10 20 30 40 50 output = 10 30 40 50