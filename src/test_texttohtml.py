import unittest

from htmlnode import LeafNode, text_node_to_html_node
from textnode import TextNode, TextType

class TestTextToHTMLNode(unittest.TestCase):
	def test_text(self):
		node = TextNode("This is a text node", TextType.TEXT)
		html_node = text_node_to_html_node(node)
		self.assertEqual(html_node.tag, None)
		self.assertEqual(html_node.value, "This is a text node")

	def test_bold(self):
		node = TextNode("This is bold text", TextType.BOLD)
		html_node = text_node_to_html_node(node)
		self.assertEqual(html_node.tag, "b")
		self.assertEqual(html_node.value, "This is bold text")
		self.assertEqual(html_node.props, {})

	def test_italic(self):
		node = TextNode("This is italic text", TextType.ITALIC)
		html_node = text_node_to_html_node(node)
		self.assertEqual(html_node.tag, "i")
		self.assertEqual(html_node.value, "This is italic text")
		self.assertEqual(html_node.props, {})

	def test_code(self):
		node = TextNode("const x = 10;", TextType.CODE)
		html_node = text_node_to_html_node(node)
		self.assertEqual(html_node.tag, "code")
		self.assertEqual(html_node.value, "const x = 10;")
		self.assertEqual(html_node.props, {})

	def test_link(self):
		node = TextNode("Click me", TextType.LINK, "https://example.com")
		html_node = text_node_to_html_node(node)
		self.assertEqual(html_node.tag, "a")
		self.assertEqual(html_node.value, "Click me")
		self.assertEqual(html_node.props, {"href": "https://example.com"})

	def test_image(self):
		node = TextNode("Alt text", TextType.IMAGE, "image.jpg")
		html_node = text_node_to_html_node(node)
		self.assertEqual(html_node.tag, "img")
		self.assertEqual(html_node.value, "")
		self.assertEqual(html_node.props, {"src": "image.jpg", "alt": "Alt text"})

if __name__ == "__main__":
	unittest.main()
