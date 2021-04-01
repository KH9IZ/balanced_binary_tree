class AVLTree:
    key = None
    left = None
    right = None

    def __str__(self):
        return f"AVL Tree node {self.key}"

    def __init__(self, obj):
        self.key = obj

    def insert(self, obj):
        if obj < self.key:
            if self.left is None:
                self.left = AVLTree(obj)
            else:
                self.left.insert(obj)
        else:
            if self.right is None:
                self.right = AVLTree(obj)
            else:
                self.right.insert(obj)

    def __iadd__(self, obj):
        self.insert(obj)

    def find(self, obj):
        if obj == self.key:
            return self
        elif obj < self.key and self.left is not None:
            return self.left.find(obj)
        elif obj > self.key and self.right is not None:
            return self.right.find(obj)
        else:
            return None

    def search_min(self):
        if self.left is not None:
            return self.left.search_min()
        return self


my_tree = AVLTree(10)
print(my_tree.find(10))
my_tree.insert(5)
print(my_tree.find(5))
my_tree.insert(2)
print(my_tree.find(10))

print(my_tree.find(2))
my_tree.find(1)

my_tree.insert(8)
my_tree.insert(0)
my_tree.insert(1)
my_tree.insert(11)
my_tree.insert(12)

print(my_tree.search_min())
print(my_tree.find(0))

my_tree += 12
