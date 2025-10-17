class Node:
    def __init__(self, value=0, next_node=None):
        self.data = value
        self.next = next_node


def array_to_LL(arr):
    if not arr:
        return None
    head = Node(arr[0])
    cur = head
    for value in arr[1:]:
        cur.next = Node(value)
        cur = cur.next
    return head

def print_LL(head):
    temp = head
    while temp:
        print(temp.data, end=" ")
        temp = temp.next
    print()


def reverse_LL(head):
    prev = None
    cur = head
    while cur:
        front = cur.next
        cur.next = prev
        prev = cur
        cur = front
    return prev

def palindromeLL(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    rhead = reverse_LL(slow)
    temp = head
    rtemp = rhead
    while rtemp:
        if temp.data != rtemp.data:
            reverse_LL(rhead)  # Restore the list
            return False
        temp = temp.next
        rtemp = rtemp.next

    reverse_LL(rhead)  # Restore the list
    return True


n = int(input())
arr = list(map(int, input().split()))
head = array_to_LL(arr)
print("true" if palindromeLL(head) else "false")





# class Node:
#     def __init__(self, value=0, next_node=None):
#         self.data = value
#         self.next = next_node

# """
# def array_to_LL(arr):
#     if not arr:
#         return None
#     head = Node(arr[0])
#     cur = head
#     for value in arr[1:]:
#         cur.next = Node(value)
#         cur = cur.next
#     return head

# def print_LL(head):
#     temp = head
#     while temp:
#         print(temp.data, end=" ")
#         temp = temp.next
#     print()
# """

# def palindromeLL(head):
#     temp = head
#     stack = []
#     while temp:
#         stack.append(temp.data)
#         temp = temp.next
#     temp = head
#     while temp:
#         if temp.data != stack.pop():
#             return False
#         temp = temp.next
#     return True

# """
# n = int(input())
# arr = list(map(int, input().split()))
# head = array_to_LL(arr)
# print("true" if palindromeLL(head) else "false")
# """
