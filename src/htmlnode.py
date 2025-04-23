from textnode import TextNode, TextType


class HTMLNode:
	def __init__(self, tag=None, value=None, children=None, props=None):
		self.tag = tag
		self.value = value
		self.children = children 
		self.props = props if props is not None else {}

	def to_html(self):
		raise NotImplementedError("Not Implemented")

	def props_to_html(self):
		return ''.join(f' {key}="{value}"' for key, value in self.props.items()) 

	def __repr__(self):
		return (
			f"HTMLNode(tag={repr(self.tag)}, "
			f"value={repr(self.value)}, "
			f"children={repr(self.children)}, "
			f"props={repr(self.props)})"
		)

class LeafNode(HTMLNode):
	def __init__(self, tag, value, props=None):
		super().__init__(tag, value, [], props)

	def to_html(self):
		if self.value == None:
			raise ValueError("no value")
		if self.tag == None:
			return f"{self.value}"
		html = f"<{self.tag}"
		if self.props:
			for key, value in self.props.items():
				html += f' {key}="{value}"'

		html += f">{self.value}</{self.tag}>"

		return html

class ParentNode(HTMLNode):
	def __init__(self, tag, children, props=None):
		super().__init__(tag, props)
		if not isinstance(children, list) or not children:
			raise ValueError("Children argument must be a non-empty list of nodes.")
		if not tag:
			raise ValueError("Tag argument must have a value.")
		self.children = children

	def to_html(self):
		# Generate the HTML string for properties(if they exist)
		props_html = ""
		if self.props:
			props_html =" " + " ".join(f"{key}='{value}'" for key, value in self.props.items())
		opening_tag = f"<{self.tag}{props_html}>"
		closing_tag = f"</{self.tag}>"
		child_html = "".join(child.to_html() for child in self.children)	
		return f"{opening_tag}{child_html}{closing_tag}"


def text_node_to_html_node(text_node):
	if text_node.text_type == TextType.TEXT:
		new_leaf = LeafNode(None, text_node.text, props = {})
	elif text_node.text_type == TextType.BOLD:
		new_leaf = LeafNode("b", text_node.text, props = {})
	elif text_node.text_type == TextType.ITALIC:
		new_leaf = LeafNode("i", text_node.text, props = {})
	elif text_node.text_type == TextType.CODE:
		new_leaf = LeafNode("code", text_node.text, props = {})
	elif text_node.text_type == TextType.LINK:
		new_leaf = LeafNode("a", text_node.text, props = {"href": text_node.url})
	elif text_node.text_type == TextType.IMAGE:
		new_leaf = LeafNode("img", "", props = {"src": text_node.url, "alt": text_node.text})
	else:
		raise Exception("Incorrect Text Type") 
	return new_leaf
