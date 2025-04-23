import unittest

from htmlnode import LeafNode

class TestLeafNode(unittest.TestCase):
	def test_leaf_to_html_p(self):
		node = LeafNode("p", "Hello, world!")
		self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

	def test_leaf_to_html_a(self):
		node = LeafNode("a", "abc 123")
		self.assertEqual(node.to_html(), "<a>abc 123</a>")

	def test_leaf_to_html_b(self):
		node = LeafNode("b", "Geralt")
		self.assertEqual(node.to_html(), "<b>Geralt</b>")

if __name__ == "__main__":
	unittest.main()
