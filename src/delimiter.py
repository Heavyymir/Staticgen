from textnode import TextNode, TextType


def split_nodes_delimiter(old_nodes, delimeter, text_type):
	new_nodes = []
	for old_node in old_nodes:
		if old_node.text_type != TextType.TEXT:
			new_nodes.append(old_node)
			continue
		text = old_node.text
		while delimeter in text:
			opening_index = text.find(delimeter)
			closing_index = text.find(delimeter, opening_index + len(delimeter))
			if closing_index == -1:
				raise Exception(f"No closing delimiter found for {delimiter}")
			before_text = text[:opening_index]
			delimeted_text = text[opening_index + len(delimeter):closing_index]
			after_text = text[closing_index + len(delimeter):]
			if before_text:
				new_nodes.append(TextNode(before_text, TextType.TEXT))
			new_nodes.append(TextNode(delimeted_text, text_type))
			
			text = after_text
		
		if text:
			new_nodes.append(TextNode(text, TextType.TEXT))

	return new_nodes
