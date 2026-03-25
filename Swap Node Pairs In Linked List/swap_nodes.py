from preloaded import Node

def swap_pairs(head):
    if not head or not head.next:
        return head

    new = Node(0)
    new.next = head
    prev = new

    while prev.next and prev.next.next:
        first = prev.next
        second = prev.next.next

        prev.next = second
        first.next = second.next
        second.next = first
        prev = first

    return new.next
