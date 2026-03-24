from preloaded import Node

# class Node(object):
#     """Node class for reference"""
#     def __init__(self, data, next=None):
#         self.data = data
#         self.next = next

def get_nth(node, index):
    if node is None:
        raise ExeptionError("Linked list cannot be None")

    if index < 0:
        raise ExeptionError("Index must be a positive integer")

    curr = node
    i = 0
    while curr:
        if i == index:
            return curr
        curr = curr.next
        i+=1

    raise ExeptionError("Index cannot be longer than linked list")
