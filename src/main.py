from textnode import TextNode, TextType


def main():
	fresh_node = TextNode("This is some anchor text", TextType.LINK, "https://www.boot.dev")
	print(fresh_node)

if __name__ == "__main__":
	main()
