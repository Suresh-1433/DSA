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

def delete_kth(head, k):
    if head is None:
        return head
    if k == 0:
        temp = head
        head = head.next
        return head
    temp = head
    count = 0
    while temp.next is not None:
        if count == k - 1:
            n = temp.next
            temp.next = temp.next.next
            break
        temp = temp.next
        count += 1
    return head

if __name__ == "__main__":
    n, k = map(int, input().split())
    arr = []
    if n > 0:
        arr = list(map(int, input().split()))
    head = array_to_LL(arr)
    head = delete_kth(head, k)
    printLL(head)
    
#5 2
#10 20 4 50 45  
# output = 10 20 50 45