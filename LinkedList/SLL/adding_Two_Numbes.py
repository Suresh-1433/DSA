class Node:
    def __init__(self, value, next_node=None):
        self.data = value
        self.next = next_node


def array_to_ll(arr):
    if not arr:
        return None
    head = Node(arr[0])
    cur = head
    for value in arr[1:]:
        cur.next = Node(value)
        cur = cur.next
    return head

def print_ll(head):
    while head:
        print(head.data, end=" ")
        head = head.next
    print()


def add_two_numbers(a, b):
    temp1 = a
    temp2 = b
    carry = 0
    ans = Node(-1)
    cur = ans
    while temp1 or temp2:
        total = carry
        if temp1:
            total += temp1.data
            temp1 = temp1.next
        if temp2:
            total += temp2.data
            temp2 = temp2.next
        cur.next = Node(total % 10)
        carry = total // 10
        cur = cur.next
    if carry:
        cur.next = Node(1)
    return ans.next


# Input
m, n = map(int, input(" enter m,n:").split()) #3 3
a_arr = list(map(int, input("Enter 1st Arr:").split())) #4 5 6
b_arr = list(map(int, input("Enter 2nd Arr").split()))# 5 6 3

# Convert arrays to linked lists
a = array_to_ll(a_arr)
b = array_to_ll(b_arr)

# Add two numbers represented by linked lists
c = add_two_numbers(a, b)

# Print the result linked list
print_ll(c)