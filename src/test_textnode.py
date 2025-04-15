import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
	def test_eq_identical_nodes(self):
    		node1 = TextNode("This is a text node", TextType.BOLD)
    		node2 = TextNode("This is a text node", TextType.BOLD)
    		self.assertEqual(node1, node2)

	def test_not_eq_different_text_type(self):
    		node1 = TextNode("This is a text node", TextType.BOLD)
    		node2 = TextNode("This is a text node", TextType.ITALIC)
    		self.assertNotEqual(node1, node2)

	def test_not_eq_different_text(self):
    		node1 = TextNode("This is a text node", TextType.BOLD)
    		node2 = TextNode("Different text", TextType.BOLD)
    		self.assertNotEqual(node1, node2)


	def test_not_eq_differnt_url(self):
		node1 = TextNode("This is a test", TextType.BOLD, "www.google.com")
		node2 = TextNode("This is a test", TextType.BOLD, "www.amazon.com")
		self.assertNotEqual(node1, node2)


if __name__ == "__main__":
        unittest.main()
