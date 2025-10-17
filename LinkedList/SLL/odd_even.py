#Optimal  
#n = 6 
#input = 1,2,3,4,5,6
#output = 1,3,5,2,4,6
class Node:
    def __init__(self, value, next_node=None):
        self.data = value
        self.next = next_node

def array_to_LL(arr):
    if not arr:
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
    while temp:
        print(temp.data, end=" ")
        temp = temp.next


def even_odd_list(head):
    even = head
    odd = head.next
    odd_head = head.next

    while odd and odd.next:
        even.next = even.next.next
        odd.next = odd.next.next
        even = even.next
        odd = odd.next

    even.next = odd_head
    return head


n = int(input("Enter Num: "))
arr = list(map(int, input("Enter the Arr: ").split()))
head = array_to_LL(arr)
head = even_odd_list(head)
print_LL(head)


#Brute Force Solution  

#class Node:
#    def __init__(self, value, next_node=None):
#        self.data = value
#        self.next = next_node
#
#"""
#def array_to_LL(arr):
#    if not arr:
#        return None
#    head = Node(arr[0])
#    cur = head
#    for i in range(1, len(arr)):
#        temp = Node(arr[i])
#        cur.next = temp
#        cur = cur.next
#    return head
#
#def print_LL(head):
#    temp = head
#    while temp:
#        print(temp.data, end=" ")
#        temp = temp.next
#"""
#
#def even_odd_list(head):
#    temp = head
#    v = []
#
#    # Even Indexes
#    while temp and temp.next:
#        v.append(temp.data)
#        temp = temp.next.next
#    if temp:
#        v.append(temp.data)
#
#    temp = head.next
#    # Odd Indexes
#    while temp and temp.next:
#        v.append(temp.data)
#        temp = temp.next.next
#    if temp:
#        v.append(temp.data)
#
#    # Updation of Linked list
#    temp = head
#    for i in range(len(v)):
#        temp.data = v[i]
#        temp = temp.next
#    return head
#
#"""
#if __name__ == "__main__":
#    n = int(input())
#    arr = list(map(int, input().split()))
#    head = array_to_LL(arr)
#    head = even_odd_list(head)
#    print_LL(head)
#"""