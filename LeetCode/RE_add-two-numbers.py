"""
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.
"""
#RUNTIME ERROR
#CORRECT OUTPUTS
class Node:
    # Singly linked node
    def __init__(self, data=None):
        self.data = data
        self.next = None
class singly_linked_list:
    def __init__(self):
        # Createe an empty list
        self.tail = None
        self.head = None
        self.count = 0

    def iterate_item(self):
        # Iterate the list.
        current_item = self.tail
        while current_item:
            val = current_item.data
            current_item = current_item.next
            yield val

    def append_item(self, data):
        #Append items on the list
        node = Node(data)
        if self.head:
            self.head.next = node
            self.head = node
        else:
            self.tail = node
            self.head = node
        self.count += 1

for _ in range(int(input())):
    l1 = list(map(int, input().split(' ')))
    l2 = list(map(int, input().split(' ')))
    l1 = l1[::-1]
    l2 = l2[::-1]
    #if l1==l2:
        #addList = [int(l1[i])+int(l2[i]) for i in range(len(l2)-1)]
    #else:
       # addList = [int(l1[i])+int(l2[i]) for i in range(len(l1)-1)]
    #print(int(l1), int(l2))
    #print(l1)
    #print(l2)
    for i in l1:
        val1=''.join(map(str, l1))
    #print(val1)
    for j in l2:
        val2=''.join(map(str,l2))
    #print(val2)
    addedNums = int(val1)+int(val2)
    lis = list(str(addedNums)[::-1])
    ints = [int(i) for i in lis]
    print(ints)
    items= singly_linked_list()
    for i in ints:
        items.append_item(i)
    for val in items.iterate_item():
        print(val)
