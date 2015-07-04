# O(N**2) - Avoid
class QuickFind_Eager:
    def __init__(self, nodes):
        self.array = [num for num in range(nodes)]

    # Joins two nodes into a component
    def union(self, first_node, second_node):
        for pos, val in enumerate(self.array):
            if self.array[pos] == self.array[first_node]:
                self.array[pos] = self.array[second_node]

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

    # Checks if two nodes are in the same component
    def connected(self, first_node, second_node):
        return self.root(first_node) == self.root(second_node)

# O(log N) - Pretty darn fast
class WeightedQuickUnion:
    def __init__(self, nodes):
        self.array = [num for num in range(nodes)]
        self.weight = [num for num in range(nodes)]

    # Follows parent pointers to actual root
    def root(self, parent):
        while parent != self.array[parent]:
            parent = self.array[parent]
        return parent

    # Joins two nodes into a component
    def union(self, first_node, second_node):
        if self.root(first_node) == self.root(second_node):
            return

        if (self.weight[first_node] < self.weight[second_node]):
            self.array[first_node] = self.root(second_node)
            self.weight[second_node] += self.weight[first_node]
        else:
            self.array[second_node] = self.root(first_node)
            self.weight[first_node] += self.weight[second_node]

    # Checks if two nodes are in the same component
    def connected(self, first_node, second_node):
        return self.root(first_node) == self.root(second_node)


# O(N + M lg* N) - wicked fast - use this
class WeightedQuickUnion_PathCompression:
    def __init__(self, nodes):
        self.array = [num for num in range(nodes)]
        self.weight = [num for num in range(nodes)]

    # Follows parent pointers to actual root
    def root(self, parent):
        while parent != self.array[parent]:
            self.array[parent] = self.array[self.array[parent]]
            parent = self.array[parent]
        return parent

    # Joins two nodes into a component
    def union(self, first_node, second_node):
        if self.root(first_node) == self.root(second_node):
            return

        if self.weight[first_node] < self.weight[second_node]:
            self.array[first_node] = self.root(second_node)
            self.weight[second_node] += self.weight[first_node]
        else:
            self.array[second_node] = self.root(first_node)
            self.weight[first_node] += self.weight[second_node]

    # Checks if two nodes are in the same component
    def connected(self, first_node, second_node):
        return self.root(first_node) == self.root(second_node)


def test_quickfind(quickfind):
    print('---{0}---').format(quickfind.__name__)
    t = quickfind(100)
    t.union(1,2)
    print('1) OK!' if True == t.connected(1,2) else "Not OK!")
    t.union(4,2)
    t.union(3,4)
    print('2) OK!' if False == t.connected(0,2) else "Not OK!")
    print('3) OK!' if True == t.connected(1,4) else "Not OK!")
    t.union(0,3)
    print('4) OK!' if True == t.connected(0,4) else "Not OK!")
    t.union(50,0)
    t.union(34, 8)
    print('5) OK!' if True == t.connected(8,34) else "Not OK!")
    t.union(48, 5)
    t.union(54, 17)
    t.union(17, 83)
    print('6) OK!' if False == t.connected(17,1) else "Not OK!")
    t.union(17, 48)
    t.union(9, 6)
    t.union(57, 63)
    print('7) OK!' if False == t.connected(2,34) else "Not OK!")
    t.union(64, 65)
    t.union(72, 83)
    t.union(63, 83)
    print('8) OK!' if False == t.connected(6,34) else "Not OK!")
    print('9) OK!' if False == t.connected(17,1) else "Not OK!")
    print('===END===')

# Accuracy Checks
test_quickfind(QuickFind_Eager)
test_quickfind(QuickUnion_Lazy)
test_quickfind(WeightedQuickUnion)
test_quickfind(WeightedQuickUnion_PathCompression)

# test run time
import timeit

t = timeit.timeit(stmt="test_quickfind(QuickFind_Eager)", setup="from __main__ import QuickFind_Eager; from __main__ import test_quickfind", number=100000)
print(t)
t = timeit.timeit(stmt="test_quickfind(QuickUnion_Lazy)", setup="from __main__ import QuickUnion_Lazy; from __main__ import test_quickfind", number=100000)
print(t)
t = timeit.timeit(stmt="test_quickfind(WeightedQuickUnion)", setup="from __main__ import WeightedQuickUnion; from __main__ import test_quickfind", number=100000)
print(t)
t = timeit.timeit(stmt="test_quickfind(WeightedQuickUnion_PathCompression)", setup="from __main__ import WeightedQuickUnion_PathCompression; from __main__ import test_quickfind", number=100000)
print(t)
