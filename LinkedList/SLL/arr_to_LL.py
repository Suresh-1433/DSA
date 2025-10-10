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
        
n = int(input())
arr = []
if n > 0:
    arr = list(map(int, input().split()))
head = array_to_LL(arr)
print_LL(head)

#Example 2
#
#Input : head = 200 -> 100 -> 300
#
#Output : 200 100 300
#
#Algorithm
#
#1.Create a temporary pointer variable and set it to the head of the linked list.
#
#2.Check if the temporary pointer is not null (to handle an empty list).
#
#3.Print the data and move the temporary pointer to the next node in the list.
#
#Repeat steps 2 and 3 until the end of the linked list is reached.
#
#Code Implementation