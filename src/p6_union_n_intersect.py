class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        if not cur_head:
            return '<Empty>'
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value)
            cur_head = cur_head.next
            if cur_head:
                out_string += ' -> '
        return out_string

    def append(self, value):
        if self.head is None:
            self.head = Node(value)
            return
        node = self.head
        while node.next:
            node = node.next
        node.next = Node(value)

    def prepend(self, value):
        if self.head is None:
            self.head = Node(value)
            return
        node = self.head
        new_head = Node(value)
        new_head.next = node
        self.head = new_head

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next
        return size


def union(llist_1, llist_2):
    # Your Solution Here
    value_dict = {}
    node = llist_1.head
    while node:
        value_dict[node.value] = node.value
        node = node.next
    node = llist_2.head
    while node:
        value_dict[node.value] = node.value
        node = node.next
    linked_list = LinkedList()
    union_values = list(value_dict.values())
    for val in union_values:
        linked_list.prepend(val)
    return linked_list


def intersection(llist_1, llist_2):
    value_dict = {}
    intersect_dict = {}
    node = llist_1.head
    while node:
        value_dict[node.value] = node.value
        node = node.next
    node = llist_2.head
    while node:
        if node.value in value_dict:
            intersect_dict[node.value] = node.value
        node = node.next
    linked_list = LinkedList()
    intersect_values = list(intersect_dict.values())
    for val in intersect_values:
        linked_list.prepend(val)
    return linked_list


# Test case 1

linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,21]
element_2 = [6,32,4,9,6,1,11,21,1]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

print(union(linked_list_1,linked_list_2))  # 11 -> 1 -> 9 -> 32 -> 21 -> 65 -> 6 -> 35 -> 4 -> 2 -> 3
print(intersection(linked_list_1,linked_list_2))  # 21 -> 4 -> 6


# Test case 2

linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,23,234,55,33,44,22,11]
element_2 = [13,8,9,21,1,3]

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

print(union(linked_list_3, linked_list_4))  # 1 -> 21 -> 9 -> 8 -> 13 -> 11 -> 22 -> 44 -> 33 -> 55 -> 234 -> 23 -> 65 -> 6 -> 35 -> 4 -> 2 -> 3
print(intersection(linked_list_3, linked_list_4))  # 3


# Test case 3

linked_list_5 = LinkedList()
linked_list_6 = LinkedList()

element_1 = [23,42,4,35,9,5,3]
element_2 = []

for i in element_1:
    linked_list_5.append(i)

for i in element_2:
    linked_list_6.append(i)

print(union(linked_list_5, linked_list_6))  # 3 -> 5 -> 9 -> 35 -> 4 -> 42 -> 23
print(intersection(linked_list_5, linked_list_6))  # Emoty intersect
