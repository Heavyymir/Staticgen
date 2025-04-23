import unittest

from delimiter import split_nodes_delimiter
from textnode import TextNode, TextType

class test_delimeter(unittest.TestCase):
	def test_bold_delimeter(self):
		node = TextNode("This is text with a **bold phrase** in it", TextType.TEXT)
		result = split_nodes_delimiter([node], "**", TextType.BOLD)
		self.assertEqual(len(result), 3)
		self.assertEqual(result[0].text, "This is text with a ")
		self.assertEqual(result[0].text_type, TextType.TEXT)
		self.assertEqual(result[1].text, "bold phrase")
		self.assertEqual(result[1].text_type, TextType.BOLD)
		self.assertEqual(result[2].text, " in it")
		self.assertEqual(result[2].text_type, TextType.TEXT)

	def test_code_delimeter(self):
		node = TextNode("This is text with a `code block` word", TextType.TEXT)
		result = split_nodes_delimiter([node], "`", TextType.CODE)
		self.assertEqual(len(result), 3)
		self.assertEqual(result[0].text, "This is text with a ")
		self.assertEqual(result[0].text_type, TextType.TEXT)
		self.assertEqual(result[1].text, "code block")
		self.assertEqual(result[1].text_type, TextType.CODE)
		self.assertEqual(result[2].text, " word")
		self.assertEqual(result[2].text_type, TextType.TEXT)

	def test_no_delimeter(self):
		node = TextNode("This text has no delimeter", TextType.TEXT)
		result = split_nodes_delimiter([node], "**", TextType.TEXT)
		self.assertEqual(len(result), 1)
		self.assertEqual(result[0].text, "This text has no delimeter")
		self.assertEqual(result[0].text_type, TextType.TEXT)
		
if __name__ == "__main__":
	unittest.main()
