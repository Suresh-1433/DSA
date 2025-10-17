class Node:
    def __init__(self, value, address=None):
        self.data = value
        self.next = address


def array_to_LL(arr):
    if not arr:
        return None
    head = Node(arr[0])
    cur = head
    for value in arr[1:]:
        temp = Node(value)
        cur.next = temp
        cur = cur.next
    return head

def print_LL(head):
    temp = head
    while temp:
        print(temp.data, end=" ")
        temp = temp.next


def deleteKthNodeFromEnd(head, k):
    back = head
    front = head
    for i in range(k + 1):
        front = front.next
    if front is None:
        return head.next
    while front.next:
        front = front.next
        back = back.next
    n = back.next
    back.next = back.next.next
    del n
    return head


if __name__ == "__main__":
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    head = array_to_LL(arr)
    head = deleteKthNodeFromEnd(head, k)
    print_LL(head)
