class AVLTree:
    key = None
    left = None
    right = None
    height = 1

    def __str__(self):
        return str(self.key)

    def __init__(self, obj=None):
        if obj is None:
            self.key = None
            self.height = 0
        if type(obj) is AVLTree:
            self.key = obj.key
            self.left = AVLTree(obj.left) if obj.left else obj.left
            self.right = AVLTree(obj.right) if obj.right else obj.right
            self.height = obj.height
            return
        self.key = obj

    def __iadd__(self, obj):
        self.insert(obj)
        return self

    def __isub__(self, obj):
        self.delete(obj)
        return self

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
        self.reheight()
        tmp.left = AVLTree(self)
        tmp.reheight()
        return tmp

    def right_rot(self):
        tmp = self.left
        self.left = tmp.right
        self.reheight()
        tmp.right = AVLTree(self)
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
        if self.key is None:
            self.key = obj
            return self
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

    def find_min(self):
        return self if self.left is None else self.left.find_min()

    def delete_min(self):
        if self.left == None:
            return self.right
        self.left = self.left.delete_min()
        return self.balance()

    def delete(self, obj):
        if self.key is None:
            return
        if self.key == obj:
            if self.right is None:
                self.__init__(self.left)
                return
            min_obj = self.right.find_min()
            min_obj.right = self.right.delete_min()
            min_obj.left = self.left
            self.__init__(min_obj)
        elif obj < self.key and self.left is not None:
            self.left.delete(obj)
        elif obj >= self.key and self.right is not None:
            self.right.delete(obj)
        else:  # if no such object in tree
            return
        self.balance()
