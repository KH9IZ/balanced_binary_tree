import unittest
from main import AVLTree


class TestAVLTree(unittest.TestCase):

    def setUp(self) -> None:
        self.empty_tree = AVLTree()
        self.big_tree = AVLTree(0)
        self.big_tree += 0
        self.big_tree += 21
        self.big_tree += 15
        self.big_tree += 100
        self.big_tree += -2
        self.big_tree += -8
        self.big_tree += 89
        self.big_tree += 33

    def test_init(self):
        with self.subTest("empty init"):
            self.assertEqual(AVLTree().key, None)
        with self.subTest("int init"):
            self.assertEqual(AVLTree(5).key, 5)
        with self.subTest("AVLTree init"):
            self.assertEqual(AVLTree(AVLTree(2)).key, 2)

    def test_insert(self):
        self.empty_tree.insert(1)
        self.assertEqual(self.empty_tree.key, 1)

    def test_insert_by_operator(self):
        self.empty_tree += 0
        self.assertEqual(self.empty_tree.key, 0)

    def test_right_rotation(self):
        self.empty_tree += 2
        self.empty_tree += 1
        self.empty_tree += 0
        self.empty_tree.reheight()
        self.assertEqual(self.empty_tree.height, 2)
        self.assertEqual(self.empty_tree.key, 1)
        self.assertEqual(self.empty_tree.left.key, 0)
        self.assertEqual(self.empty_tree.right.key, 2)

    def test_left_rotation(self):
        self.empty_tree += 0
        self.empty_tree += 1
        self.empty_tree += 2
        self.assertEqual(self.empty_tree.height, 2)
        self.assertEqual(self.empty_tree.key, 1)
        self.assertEqual(self.empty_tree.left.key, 0)
        self.assertEqual(self.empty_tree.right.key, 2)

    def test_big_right_rotation(self):
        self.empty_tree += 0
        self.empty_tree += 2
        self.empty_tree += 1
        self.assertEqual(self.empty_tree.height, 2)
        self.assertEqual(self.empty_tree.key, 1)
        self.assertEqual(self.empty_tree.left.key, 0)
        self.assertEqual(self.empty_tree.right.key, 2)

    def test_big_left_rotation(self):
        self.empty_tree += 2
        self.empty_tree += 0
        self.empty_tree += 1
        self.assertEqual(self.empty_tree.height, 2)
        self.assertEqual(self.empty_tree.key, 1)

    def test_find(self):
        self.assertIsNone(self.big_tree.find(7))
        self.assertTrue(self.big_tree.find(100))

    def test_search_min(self):
        self.assertEqual(self.big_tree.find_min().key, -8)
        self.assertIsNone(self.empty_tree.find_min().key)

    def test_delete(self):
        self.big_tree.delete(0)
        self.assertEqual(self.big_tree.right.left.key, 21)
        self.big_tree -= 21
        self.assertEqual(self.big_tree.right.left.key, 33)
        self.empty_tree.delete(1000000)
        self.assertIsNone(self.empty_tree.key)


if __name__ == '__main__':
    unittest.main()
