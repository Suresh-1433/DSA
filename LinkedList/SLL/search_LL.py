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

def search_LL(head, k):
    temp = head
    while temp != None:
        if temp.data == k:
            return True
        temp = temp.next
    return False
  
n, k = map(int, input().split())
arr = []
if n > 0:
    arr = list(map(int, input().split()))
head = array_to_LL(arr)
print(search_LL(head, k))


#Example 2
#
#Input : head = 6 -> 21 -> 17 -> 30 -> 10 -> 8, K = 13
#
#Output : False
#
#Explanation: 13 is not present in the linked list.
#
#Algorithm
#
#1.Create a temporary pointer variable and set it to the head of the linked list.
#
#2.Check if the temporary pointer is not null (to handle an empty list).
#
#3.Check if current temp->data is equal to k or not. Move the temporary pointer to the next node in the list.
#
#