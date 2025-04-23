from textnode import (
	TextType,
	TextNode,
)

def main():
	text_node = TextNode("Bla Bla", TextType.LINK, "http://www.boot.dev")
	text_node2 = TextNode("Bla Bla bla", TextType.BOLD, "http://www.boot.dev")
	print(text_node)

main()