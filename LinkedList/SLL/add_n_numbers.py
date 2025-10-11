class Node:
    def __init__(self, data=0, next=None):
        self.data = data
        self.next = next

class Solution:
    def addNumbers(self, lists):
        if not lists:
            return None
        
        # Helper function to add two linked lists
        def add_two_lists(l1, l2):
            dummy = Node(0)
            current = dummy
            carry = 0
            
            while l1 or l2 or carry:
                total = carry
                
                if l1:
                    total += l1.data
                    l1 = l1.next
                if l2:
                    total += l2.data
                    l2 = l2.next
                
                current.next = Node(total % 10)
                carry = total // 10
                current = current.next
            
            return dummy.next
        
        # Start with first list and add all others to it
        result = lists[0]
        
        for i in range(1, len(lists)):
            result = add_two_lists(result, lists[i])
        
        return result

# Helper function to create linked list from array
def create_linked_list(arr):
    if not arr:
        return None
    head = Node(arr[0])
    current = head
    for i in range(1, len(arr)):
        current.next = Node(arr[i])
        current = current.next
    return head

# Helper function to print linked list
def print_linked_list(head):
    result = []
    current = head
    while current:
        result.append(str(current.data))
        current = current.next
    return " -> ".join(result)

# Main code to handle the input format

# Read number of lists
num_lists = int(input().strip())
lists = []

# Read each list
for _ in range(num_lists):
    length = int(input().strip())
    data = list(map(int, input().strip().split()))
    lists.append(create_linked_list(data))

# Create solution and compute result
sol = Solution()
result = sol.addNumbers(lists)

# Print the result
print(print_linked_list(result))