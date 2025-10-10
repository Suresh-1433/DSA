class Node:
    def __init__(self, value=0, next_node=None):
        self.data = value
        self.next = next_node

p1 = Node(5, None)
p2 = Node(7)
p3 = Node()

print(p1.data)  # 5
print(p2.data)  # 7
print(p3.data)  # 0

#Explanation:
#
#The Node class has three constructors:
#
#The first constructor takes two parameters: value and address, initializing the node with the given value and the address of the next node.
#
#The second constructor takes one parameter: value, initializing the node with the given value and setting the next pointer to nullptr.
#
#The third constructor is a default constructor with no parameters, initializing the node with default values.
#
#In the main function:
#
#p1 is created using the first constructor with parameters (5, nullptr).
#
#p2 is created using the second constructor with one parameter (7).
#
#p3 is created using the default constructor.