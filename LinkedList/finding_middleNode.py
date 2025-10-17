class Node:
    def __init__(self, value, address=None):
        self.data = value
        self.next = address


def array_to_LL(arr):
    n = len(arr)
    if n == 0:
        return None
    head = Node(arr[0])
    cur = head
    for i in range(1, n):
        temp = Node(arr[i])
        cur.next = temp
        cur = cur.next
    return head

def print_LL(head):
    temp = head
    while temp is not None:
        print(temp.data, end=" ")
        temp = temp.next


def middleNode(head):
    slow = head
    fast = head
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
    return slow


if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().split()))
    head = array_to_LL(arr)
    head = middleNode(head)
    print_LL(head)
