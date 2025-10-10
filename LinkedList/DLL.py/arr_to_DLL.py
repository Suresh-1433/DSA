class Node:
    def __init__(self, data, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev

def array_to_DLL(arr):
    if not arr:
        return None
    head = Node(arr[0])
    cur = head
    for value in arr[1:]:
        temp = Node(value)
        temp.prev = cur
        cur.next = temp
        cur = temp
    return head

def print_DLL(head):
    while head:
        print(head.data, end=" ")
        head = head.next

def main():
    n = int(input("enter n: "))
    arr = []
    if n > 0:
        arr = list(map(int, input("enter arr: ").split()))
    head = array_to_DLL(arr)
    print_DLL(head)

if __name__ == "__main__":
    main()