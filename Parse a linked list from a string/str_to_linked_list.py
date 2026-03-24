from preloaded import Node

def linked_list_from_string(list_repr: str) -> Node | None:
    lst = list_repr.split(" -> ")

    lst.pop()
    head = None
    for i in lst[::-1]:
        head = Node(int(i), head)

    return head
