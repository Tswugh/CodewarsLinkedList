def stringify(node):
    res = ""
    if node is None:
        return "None"
    if node.next is None:
        return res + str(node.data) + " -> None"
    res = str(node.data) + " -> "
    return res + stringify(node.next)
