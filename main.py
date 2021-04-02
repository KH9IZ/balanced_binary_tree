class AVLTree:
    key = None
    left = None
    right = None
    height = 1

    def __str__(self):
        return str(self.key)

    def __init__(self, obj):
        if type(obj) is AVLTree:
            self.key = obj.key
            self.left = AVLTree(obj.left) if obj.left else obj.left
            self.right = AVLTree(obj.right) if obj.right else obj.right
            self.height = obj.height
            return
        self.key = obj

    def __iadd__(self, obj):
        self.insert(obj)

    def balance_factor(self):
        left_h = self.left.height if self.left else 0
        right_h = self.right.height if self.right else 0
        return right_h - left_h

    def reheight(self):
        left_h = self.left.height if self.left else 0
        right_h = self.right.height if self.right else 0
        self.height = max(left_h, right_h) + 1
        return self.height

    def left_rot(self):
        tmp = self.right
        self.right = tmp.left
        tmp.left = self
        self.reheight()
        tmp.reheight()
        return tmp

    def right_rot(self):
        tmp = self.left
        self.left = tmp.right
        tmp.right = self
        self.reheight()
        tmp.reheight()
        return tmp

    def balance(self):
        self.reheight()
        bf = self.balance_factor()
        bf_right = self.right.balance_factor() if self.right else 0
        bf_left = self.left.balance_factor() if self.left else 0
        if bf == 2:
            if bf_right < 0:
                self.right = self.right.right_rot()
            return self.left_rot()
        if bf == -2:
            if bf_left > 0:
                self.left = self.left.left_rot()
            return self.right_rot()
        return self

    def insert(self, obj):
        if obj < self.key:
            self.left = self.left.insert(obj) if self.left else AVLTree(obj)
        else:
            self.right = self.right.insert(obj) if self.right else AVLTree(obj)
        tmp = self.balance()
        self.__init__(tmp)
        return self

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
my_tree.insert(5)
my_tree.insert(2)
print(my_tree)



print(my_tree.search_min())
print(my_tree.find(0))

my_tree += 12
