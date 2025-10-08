class Node:
    def __init__(self, value, address=None):
        self.data = value
        self.next = address

def array_to_LL(arr):
    if n == 0:
        return None
    head = Node(arr[0])
    cur = head
    for i in range(1, len(arr)):
        temp = Node(arr[i])
        cur.next = temp
        cur = cur.next
    return head

def print_LL(head):
    temp = head
    while temp != None:
        print(temp.data, end=" ")
        temp = temp.next

def length_LL(head):
    temp = head
    count = 0
    while temp != None:
        count = count + 1
        temp = temp.next
    return count
  
n = int(input())
arr = []
if n > 0:
    arr = list(map(int, input().split()))
head = array_to_LL(arr)
print(length_LL(head))


#Example 2
#
#Input : head = 2 -> 4 -> 1 -> 9 -> 5 -> 3 -> 6
#
#Output : 7
#
#Algorithm
#
#1.Create a temporary pointer variable and set it to the head of the linked list and initialize a count variable with zero.
#
#2.Check if the temporary pointer is not null (to handle an empty list).
#
#3.Increment the count and move the temporary pointer to the next node in the list.

