import unittest

from htmlnode import ParentNode, LeafNode


class Test_Node(unittest.TestCase):
	def test_to_html_with_children(self):
		child_node = LeafNode("span", "child")
		parent_node = ParentNode("div", [child_node])
		self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

	def test_to_html_with_grandchildren(self):
		grandchild_node = LeafNode("b", "grandchild")
		child_node = ParentNode("span", [grandchild_node])
		parent_node = ParentNode("div", [child_node])
		self.assertEqual(
			parent_node.to_html(),
			"<div><span><b>grandchild</b></span></div>",
    		)

	def test_empty_children(self):
		with self.assertRaises(ValueError) as e:
			ParentNode("div", [])
		self.assertEqual(str(e.exception), "Children argument must be a non-empty list of nodes.")

	def test_no_tag(self):
		with self.assertRaises(ValueError) as e:
			ParentNode(None, [LeafNode("span", "child")])
		self.assertEqual(str(e.exception), "Tag argument must have a value.")

	def nested_nodes(self):
		grandchild_node = LeafNode("i", "grandchild")
		child_node = ParentNode("span", [grandchild_node])
		parent_node = ParentNode("div", [child_node, LeafNode("p", "simple text")])
		self.assertEqual(
			parent_node.to_html(),
			"<div><span><i>grandchild</i></span><p>simple text</p></div>",
		)
	
