###############################################################################
#                              List of Depths                                 #
#                                                                             #
#   Given a binary tree, design an algorithm which creates a linked list of   #
#   the nodes at each depth (e.g., if you have a tree with depth D, you'll    #
#   have D linked lists).                                                     #
###############################################################################


class BNode(object):
    """Node in binary tree with data and left, right nodes (optional)."""

    def __init__(self, data, left=None, right=None):
        assert left is None or isinstance(left, BNode)
        assert right is None or isinstance(right, BNode)

        self.data = data
        self.left = left
        self.right = right

    def __repr__(self):
        """Debugging-friendly representation of node."""

        return "<BNode data=%s>" % (self.data)


class LLNode(object):
    """Node in singly linked list."""

    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        """Debugging-friendly representation of node."""

        return "<LLNode data=%s>" % (self.data)


class LinkedList(object):
    """Linked list with head and tail."""

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def add_node(self, data):
        """Add node with given data."""

        new_node = LLNode(data)

        if self.head is None:
            self.head = new_node

        if self.tail is not None:
            self.tail.next = new_node

        self.tail = new_node
        self.size += 1

    def print_list(self):
        """Print all items in linked list."""

        current = self.head

        while current is not None:
            print current.data
            current = current.next


def create_level_ll_DFS(root, lists=None, level=0):
    """Using DFS, store nodes in each level of tree as linked lists in list."""

    if root is None:            # base case
        return

    if not lists:
        lists = []

    lst = None

    if len(lists) == level:     # if first time on level, create LL
        lst = LinkedList()
        lists.append(lst)
    else:
        lst = lists[level]      # else, get LL at that level

    lst.add_node(root)          # add current node to appropriate LL
    create_level_ll_DFS(root.left, lists, level + 1)
    create_level_ll_DFS(root.right, lists, level + 1)

    return lists

################################# FIXME #######################################
# def create_level_ll_BFS(root):
#     """Using BFS, store nodes in each level of tree as a list in a list."""

#     if root is None:
#         return None

#     lists = []
#     current = []
#     parents = []

#     current.append(root)

#     while len(current) > 0:
#         result.append(current)
#         parents = current
#         current = []
#         for parent in parents:
#             if parent.left is not None:
#                 current.append(parent.left)
#             if parent.right is not None:
#                 current.append(parent.right)

#     for lst in lists:
#         for i, item in enumerate(lst):
#             lst[i] = Node(item)

#     return lists


###############################################################################
if __name__ == '__main__':

    harry = BNode("Harry")
    hermione = BNode("Hermione")
    draco = BNode("Draco")
    pansy = BNode("Pansy")

    gryffindor = BNode("Gryffindor", harry, hermione)
    slytherin = BNode("Slytherin", draco, pansy)

    root = hogwarts = BNode("Hogwarts", gryffindor, slytherin)

    lists_DFS = create_level_ll_DFS(root)
    # lists_BFS = create_level_ll_BFS(root)

    print "DFS at index 0:"
    lists_DFS[0].print_list()

    print "\nDFS at index 1:"
    lists_DFS[1].print_list()

    print "\nDFS at index 2:"
    lists_DFS[2].print_list()

    # print "BFS at index 0:", lists_BFS[0].print_list()
    # print "BFS at index 1:", lists_BFS[1].print_list()
    # print "BFS at index 2:", lists_BFS[2].print_list()
