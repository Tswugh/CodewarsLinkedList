class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None

class Context(object):
    def __init__(self, first, second):
        self.first = first
        self.second = second

def alternating_split(head):
    if head is None or head.next is None:
        raise Exception("The list has to contain at least two nodes")

    first_head = head
    second_head = head.next

    first = first_head
    second = second_head

    curr = second.next

    while curr is not None:
        first.next = curr
        first = first.next
        curr = curr.next

        if curr is not None:
            second.next = curr
            second = second.next
            curr = curr.next
        else:
            second.next = None

    first.next = None

    return Context(first_head, second_head)
