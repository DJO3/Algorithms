# O(N**2) - Avoid
class Quickfind_Eager:
    def __init__(self, nodes):
        self.array = [num for num in range(nodes)]

    # Joins two nodes into a component
    def union(self, first_node, second_node):
        print(self.array)
        for pos, val in enumerate(self.array):
            if self.array[pos] == self.array[first_node]:
                self.array[pos] = self.array[second_node]
        print(self.array)
        return '{0} is now joined to {1}'.format(first_node, second_node)

    # Checks if two nodes are in the same component
    def connected(self, first_node, second_node):
        return self.array[first_node] == self.array[second_node]


v = Quickfind_Eager(5)
print(v.union(1,2))
print(v.connected(1,2))
print(v.union(4,2))
print(v.union(3,4))
print(v.connected(0,2))
print(v.connected(1,4))
print(v.union(0,3))
