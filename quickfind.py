# O(N**2) - Avoid
class QuickFind_Eager:
    def __init__(self, nodes):
        self.array = [num for num in range(nodes)]

    # Joins two nodes into a component
    def union(self, first_node, second_node):
        for pos, val in enumerate(self.array):
            if self.array[pos] == self.array[first_node]:
                self.array[pos] = self.array[second_node]
        return '{0} is now joined to {1}'.format(first_node, second_node)

    # Checks if two nodes are in the same component
    def connected(self, first_node, second_node):
        return self.array[first_node] == self.array[second_node]


# O(N) - Still too slow - Avoid
class QuickUnion_Lazy:
    def __init__(self, nodes):
        self.array = [num for num in range(nodes)]

    # Follows parent pointers to actual root
    def root(self, parent):
        while parent != self.array[parent]:
            parent = self.array[parent]
        return parent

    # Joins two nodes into a component
    def union(self, first_node, second_node):
        self.array[first_node] = self.array[second_node]
        return '{0} is now joined to {1}'.format(first_node, second_node)

    # Checks if two nodes are in the same component
    def connected(self, first_node, second_node):
        return self.root(first_node) == self.root(second_node)


def test_quickfind(quickfind):
    t = quickfind(100)
    t.union(1,2)
    print('1) OK!' if True == t.connected(1,2) else False)
    t.union(4,2)
    t.union(3,4)
    print('2) OK!' if False == t.connected(0,2) else False)
    print('3) OK!' if True == t.connected(1,4) else False)
    t.union(0,3)
    print('4) OK!' if True == t.connected(0,4) else False)
    print('------')

test_quickfind(QuickFind_Eager)
test_quickfind(QuickUnion_Lazy)
